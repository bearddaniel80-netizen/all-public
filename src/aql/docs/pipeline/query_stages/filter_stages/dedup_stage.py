from ..base import StageBase

class DedupStage(StageBase):
    def create(self, ctx):
        queries = []
        query_map = {}

        for q in ctx.queries:
            q_hash = hash(q)
            if q_hash not in query_map.keys():
                queries.append(q)
                query_map[q_hash] = q

        ctx.queries = queries
