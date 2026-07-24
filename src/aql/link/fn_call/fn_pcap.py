from ..registry import (
    CatagoryType,
    register_function_call,
    SMEType,
    SourceFunc
)

from ...engine.package_loader import load

@register_function_call(
        name="pcap",
        printable=SourceFunc(
            catagory_type=[CatagoryType.NETWORK, CatagoryType.STREAM],
            description="Reads network trafic.",
            requirements=["scapy"],
            sme_type=SMEType.SECURITY
        )
    )
class PcapTableFunction:

    def execute(self, *args):
        path = args[0]
        load("pcap")
        from aql_pcap.adaptor.pcap_source import PcapSource

        source = PcapSource.from_file(path)

        return source.to_dataset()