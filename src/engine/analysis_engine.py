import ast


class AnalysisEngine:
    def __init__(self, analyzers):
        self.analyzers = analyzers

    def analyze(self, source_code: str):
        tree = ast.parse(source_code)
        results = []

        for analyzer in self.analyzers:
            analyzer.visit(tree)
            results.extend(analyzer.get_issues())

        return results
