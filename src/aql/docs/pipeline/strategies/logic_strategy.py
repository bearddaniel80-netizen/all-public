class LogicStrategy:
    def create_query(self, lst):
        logic_operator = []
        for item in lst:
            name = item["name"]
            logic_template = []
            
            for left in item["template"]:
                for right in item["template"]:

                    if (
                            left is right
                            or right.startswith("SELECT")
                            or right.startswith("ORDER BY")
                            or left.startswith("SELECT")
                            or left.startswith("ORDER BY")
                        ):
                        continue

                    logic_template.append(
                        self._combine_predicates(
                            left,
                            right,
                            "AND",
                        )
                    )

                    logic_template.append(
                        self._combine_predicates(
                            left,
                            right,
                            "OR",
                        )
                    )


            entry = item

            entry["name"] = f"Logic {name}"
            entry["template"] = logic_template

            logic_operator.append(entry)
        
        lst.extend(logic_operator)

    def _combine_predicates(self, left, right, operator):
        for word in ["WHERE", "HAVING"]:
            right = right.replace(word, "")
            right = right.lstrip()
        return f"{left} {operator} {right}"

