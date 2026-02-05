import ast
from smells.base import CodeSmellAnalyzer


class UnusedVariableAnalyzer(CodeSmellAnalyzer):
    def __init__(self):
        super().__init__()
        self.assigned = {}
        self.used = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.assigned[node.id] = node.lineno
        elif isinstance(node.ctx, ast.Load):
            self.used.add(node.id)

    def get_issues(self):
        for name, line in self.assigned.items():
            if name not in self.used:
                self.issues.append({
                    "type": "Unused Variable",
                    "variable": name,
                    "line": line
                })
        return self.issues
