import importlib
from google.protobuf.message import Message

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset


# Protocol Buffers is a binary serialization format designed for:
# compact storage
# fast transport
# strict schema contracts
# backward/forward compatibility
# distributed systems
#
# It is heavily used with:
# gRPC
# Kafka (protobuf encoding)
# microservices
# event-driven architectures
# ETL pipelines
#
# Think of it as:
# strongly-typed binary JSON
# but compiled + versioned + extremely fast


class ProtobufSource:

    def __init__(self, rows, message_type=None, schema_module=None):
        self._rows = rows
        self._message_type = message_type
        self._schema_module = schema_module


    # -----------------------------
    # FILE LOADING (binary stream)
    # -----------------------------
    @classmethod
    def from_file(
        cls,
        filename: str,
        message_class: type[Message],
        framed: bool = False,
    ):
        """
        Reads a protobuf stream from a file.

        NOTE:
        Protobuf has no native file container format like Avro.
        So this assumes either:
        - length-prefixed messages (common in Kafka / logs)
        - or one-message-per-file (rare)
        """

        rows = []

        with open(filename, "rb") as f:

            if framed:
                # length-delimited stream (recommended)
                while True:
                    size_bytes = f.read(4)
                    if not size_bytes:
                        break

                    size = int.from_bytes(size_bytes, "little")
                    raw = f.read(size)

                    msg = message_class()
                    msg.ParseFromString(raw)

                    rows.append(msg)

            else:
                # single message file
                raw = f.read()
                msg = message_class()
                msg.ParseFromString(raw)
                rows.append(msg)

        return cls(rows, message_type=message_class.__name__)


    # -----------------------------
    # ROW ACCESS
    # -----------------------------
    def as_rows(self):
        return self._rows


    # -----------------------------
    # AQL DATASET CONVERSION
    # -----------------------------
    def to_dataset(self):
        return Dataset(
            self._rows,
            self.infer_model(self._rows[0]),
        )


    # -----------------------------
    # MODEL INFERENCE (AQL schema)
    # -----------------------------
    def infer_model(self, sample: Message):
        """
        Converts protobuf message → AQL model
        (structural inference layer)
        """
        schema = infer_schema(sample)
        return build_model("ProtobufRow", schema)


    # -----------------------------
    # SCHEMA INTROSPECTION
    # -----------------------------
    def schema(self):
        """
        Uses protobuf descriptors instead of file schema.

        This is still reflection-based,
        but ONLY at schema build time, not scan time.
        """
        sample = self._rows[0]
        descriptor = sample.DESCRIPTOR

        return infer_schema(descriptor)


    # -----------------------------
    # FUTURE: compiled decoder hook
    # -----------------------------
    def compiled_decoder(self):
        """
        Placeholder for zero-reflection version.

        In compiled mode this would return:
        - generated decode function
        - or module-level static extractor
        """
        return None