class CombineTemplates:

    def operator(
        self,
        source_template,
        operator_template,
    ):
        return f"{source_template} {operator_template}"

    def _groupby_queries(self, func, query, example):
        results = []
        clause = "GROUP BY"

        for input_type in func["input_type"]:
            result_query = (
                f"{query} "
                f"{clause} "
                f"{example.fields[f'<field:{input_type.value}>']}"
            )
            results.append(result_query)

        return results

    def function(
        self,
        source_template,
        function_template,
        func,
        example,
    ):
        if function_template.startswith("SELECT"):

            query = source_template.replace(
                "SELECT *",
                function_template,
            )

            if func["needs_groupby_clause"] == 'True':
                query = self._groupby_queries(func, query, example)

            return query

        if function_template.startswith("HAVING"):

            query = source_template

            if func["needs_groupby_clause"] == 'True':
                query = self._groupby_queries(func, query, example)
                return [
                   f"{q} {function_template}" for q in query 
                ]

            return f"{query} {function_template}"

        if function_template.startswith("ORDER BY"):

            query = source_template

            if func["needs_groupby_clause"] == 'True':
                query = self._groupby_queries(func, query, example)
                return [
                   f"{q} {function_template}" for q in query 
                ]

            return f"{query} {function_template}"

        return f"{source_template} {function_template}"
    
