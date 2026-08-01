from ..registry import (
    CategoryType,
    register_function_call,
    SMEType,
    SourceFunc,
    FuncType
)

from aql_link.managers.package_loader import load

@register_function_call(
        name="pcap",
        printable=SourceFunc(
            catagory_type=[CategoryType.NETWORK, CategoryType.STREAM],
            description="Reads network trafic.",
            requirements=["scapy"],
            sme_type=SMEType.SECURITY,
            func_type=FuncType.ADAPTER,
            template="SELECT * FROM pcap(<stream>)",
            enabled=False
        )
    )
class PcapTableFunction:

    def execute(self, *args):
        raise NotImplementedError("coming soon")
        path = args[0]
        load("pcap")
        from aql_pcap.adaptor.pcap_source import PcapSource

        source = PcapSource.from_file(path)

        return source.to_dataset()