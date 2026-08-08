class NegationStrategy:
    def create_query(self, lst):
        negation_operator = []

        for item in lst:
            name = item["name"]
            negation_template = []

            for operator_template in item["template"]:
                if "BETWEEN" in operator_template:
                    t = operator_template.replace("BETWEEN", "NOT BETWEEN")
                
                elif "IN" in operator_template and "CONTAINS" not in operator_template:
                    t = operator_template.replace("IN", "NOT IN")
                
                t = operator_template.replace("WHERE", "WHERE NOT")
                    
                negation_template.append(t)

            entry = item

            entry["name"] = f"NOT {name}"
            entry["template"] = negation_template

            negation_operator.append(entry)

        return negation_operator