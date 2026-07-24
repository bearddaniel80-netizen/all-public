from scapy.all import rdpcap, IP, TCP, UDP

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

# Example AQL queries
# All DNS traffic
# SELECT *
# FROM pcap('capture.pcap')
# WHERE dst_port = 53
# Suspicious outbound traffic
# SELECT *
# FROM pcap('capture.pcap')
# WHERE dst_ip NOT LIKE '192.168.%'
# Top talkers
# SELECT src_ip, COUNT(*)
# FROM pcap('capture.pcap')
# GROUP BY src_ip
# Port scan detection
# SELECT src_ip, COUNT(DISTINCT dst_port)
# FROM pcap('capture.pcap')
# GROUP BY src_ip
# HAVING COUNT(DISTINCT dst_port) > 100
# Large packets
# SELECT *
# FROM pcap('capture.pcap')
# WHERE length > 1500

class PcapSource:
    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename):
        from scapy.all import PcapReader

        def gen():
            with PcapReader(filename) as pcap:
                for pkt in pcap:
                    yield cls._packet_to_row(pkt)

        return cls(list(gen()))

    @classmethod
    def from_stream(cls, packet_iterable):
        """
        Accepts ANY iterable of packets:
        - Scapy packets
        - generator
        - live capture stream
        - async bridge later
        """

        def gen():
            for pkt in packet_iterable:
                row = cls._packet_to_row(pkt)
                if row:
                    yield row

        return cls(gen())

    @staticmethod
    def _packet_to_row(pkt):

        if IP not in pkt:
            return None

        proto = None
        sport = dport = None

        if TCP in pkt:
            proto = "TCP"
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport

        elif UDP in pkt:
            proto = "UDP"
            sport = pkt[UDP].sport
            dport = pkt[UDP].dport

        return {
            "timestamp": float(pkt.time),
            "src_ip": pkt[IP].src,
            "dst_ip": pkt[IP].dst,
            "src_port": sport,
            "dst_port": dport,
            "protocol": proto,
            "length": len(pkt),
        }

    def as_rows(self):
        return self._rows

    def to_dataset(self):

        return Dataset(
            self._rows,
            self.infer_model(self._rows[0]) if self._rows else None
        )

    def infer_model(self, sample):
        schema = infer_schema(sample)
        return build_model("PcapRow", schema)

    def schema(self):
        return infer_schema(self._rows[0]) if self._rows else {}