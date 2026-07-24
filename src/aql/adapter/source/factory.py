from ...engine.package_loader import load

class StdinSourceFactory:
    @staticmethod
    def from_raw(raw: str):
        raw = raw.strip()

        # JSON (fast path)
        if raw.startswith("{") or raw.startswith("["):
            return StdinSourceFactory.from_json(raw)

        # CSV (simple heuristic)
        if "," in raw and "\n" in raw:
            return StdinSourceFactory.from_csv(raw)

        # YAML
        if raw.endswith(":\n"):
            try:
                return StdinSourceFactory.from_yaml(raw)
            except Exception:
                pass

        # XML
        if raw.startswith("<"):
            return StdinSourceFactory.from_xml(raw)

        # fallback
        return StdinSourceFactory.from_log(raw)

    @staticmethod
    def from_json(raw):
        load("json")
        from aql_json.adaptor.json_source import JsonStdinSource
        return JsonStdinSource(raw)

    @staticmethod
    def from_csv(raw):
        load("csv")
        from aql_csv.adaptor.csv_source import CsvSource
        return CsvSource(raw)

    @staticmethod
    def from_yaml(raw):
        load("yaml")
        from aql_yaml.adaptor.yaml_source import YamlSource
        import yaml
        yaml.safe_load(raw)
        return YamlSource(raw)

    @staticmethod
    def from_xml(raw):
        load("xml")
        from aql_xml.adaptor.xml_source import XmlSource
        return XmlSource(raw)

    @staticmethod
    def from_log(raw):
        load("log")
        from aql_log.adaptor.log_source import LogStdinSource
        return LogStdinSource(raw)