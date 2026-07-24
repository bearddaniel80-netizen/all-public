from elftools.elf.elffile import ELFFile

from aql_link.core.base import StdinSource
from aql_link.core.builder import build_model, infer_schema
from aql_link.core.dataset import Dataset

# SELECT * FROM elf('/bin/ls')

class ELFSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename: str):

        rows = []

        with open(filename, "rb") as f:

            elf = ELFFile(f)

            for section in elf.iter_sections():

                rows.append({
                    "name": section.name,
                    "type": section["sh_type"],
                    "addr": section["sh_addr"],
                    "offset": section["sh_offset"],
                    "size": section["sh_size"],
                    "flags": int(section["sh_flags"]),
                    "entropy": cls._entropy(
                        section.data()
                    ),
                })

        return cls(rows)

    @staticmethod
    def _entropy(data: bytes):

        if not data:
            return 0.0

        from math import log2
        from collections import Counter

        counts = Counter(data)

        total = len(data)

        entropy = 0.0

        for count in counts.values():

            p = count / total

            entropy -= p * log2(p)

        return entropy

    def as_rows(self):
        return self._rows

    def to_dataset(self):

        return Dataset(
            self._rows,
            self.infer_model(self._rows[0])
        )

    def infer_model(self, sample):

        schema = infer_schema(sample)

        return build_model(
            "ELFRow",
            schema
        )

    def schema(self):
        return infer_schema(self._rows[0])

from elftools.elf.elffile import ELFFile

from aegis_prime.aql.adapter.dataset import Dataset

# Example AQL usage
# List all functions
# SELECT name, type
# FROM elf_symbols('binary')
# WHERE type = 'FUNC'
# Find suspicious imports (malware hunting style)
# SELECT name
# FROM elf_symbols('sample')
# WHERE name ~ 'system|exec|dlopen'
# Find stripped binaries (heuristic)
# SELECT COUNT(*)
# FROM elf_symbols('binary')
# If near zero → likely stripped.
# Find dynamically linked dependencies
# SELECT name
# FROM elf_symbols('binary')
# WHERE bind = 'GLOBAL'

class ELFSymbolsSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename: str):

        rows = []

        with open(filename, "rb") as f:

            elf = ELFFile(f)

            # Try both symbol tables
            sections = [
                s for s in elf.iter_sections()
                if hasattr(s, "iter_symbols")
            ]

            for section in sections:

                for sym in section.iter_symbols():

                    rows.append({
                        "name": sym.name,
                        "bind": sym["st_info"]["bind"],
                        "type": sym["st_info"]["type"],
                        "visibility": sym["st_other"]["visibility"],
                        "size": sym["st_size"],
                        "value": sym["st_value"],
                        "shndx": sym["st_shndx"],
                    })

        return cls(rows)

    def as_rows(self):
        return self._rows

    def to_dataset(self):
        return Dataset(self._rows, None)

# Example AQL usage
# List shared library dependencies
# SELECT library
# FROM elf_imports('binary')
# WHERE type = 'DT_NEEDED'
# Find libc dependencies
# SELECT symbol
# FROM elf_imports('binary')
# WHERE library = 'libc.so.6'
# Suspicious system calls (malware-style analysis)
# SELECT symbol
# FROM elf_imports('sample')
# WHERE symbol ~ 'ptrace|exec|system|dlopen'
# Count dependencies
# SELECT COUNT(*)
# FROM elf_imports('binary')
# WHERE type = 'DT_NEEDED'

class ELFImportsSource:

    def __init__(self, rows):
        self._rows = rows

    @classmethod
    def from_file(cls, filename: str):

        rows = []

        with open(filename, "rb") as f:

            elf = ELFFile(f)

            # 1. Shared libraries (DT_NEEDED)
            dynamic = elf.get_section_by_name(".dynamic")

            needed_libs = []

            if dynamic:

                for tag in dynamic.iter_tags():

                    if tag.entry.d_tag == "DT_NEEDED":

                        needed_libs.append(tag.needed)

                        rows.append({
                            "library": tag.needed,
                            "type": "DT_NEEDED",
                            "symbol": None
                        })

            # 2. Dynamic symbols (imports)
            dynsym = elf.get_section_by_name(".dynsym")

            if dynsym:

                for sym in dynsym.iter_symbols():

                    if sym["st_shndx"] == "SHN_UNDEF":

                        rows.append({
                            "library": None,
                            "symbol": sym.name,
                            "type": "SYMBOL_IMPORT",
                            "bind": sym["st_info"]["bind"],
                            "version": None
                        })

        return cls(rows)

    def as_rows(self):
        return self._rows

    def to_dataset(self):
        return Dataset(self._rows, None)