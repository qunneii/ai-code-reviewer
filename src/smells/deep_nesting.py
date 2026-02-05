import ast
from smells.base import CodeSmellAnalyzer

MAX_NESTING = 3


class DeepNestingAnalyzer(CodeSmellAnalyzer):
    def __init__(self):
        super().__init__()
        self.depth = 0

    def generic_visit(self, node):
        if isinstance(node, (ast.If, ast.For, ast.While)):
            self.depth += 1
            if self.depth > MAX_NESTING:
                self.issues.append({
                    "type": "Deep Nesting",
                    "line": node.lineno,
                    "depth": self.depth
                })
            super().generic_visit(node)
            self.depth -= 1
        else:
            super().generic_visit(node)

    def get_issues(self):
        return self.issues
