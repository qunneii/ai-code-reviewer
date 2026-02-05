import ast
from smells.base import CodeSmellAnalyzer

MAX_FUNCTION_LENGTH = 40


class LongFunctionAnalyzer(CodeSmellAnalyzer):
    def visit_FunctionDef(self, node):
        if hasattr(node, "end_lineno"):
            length = node.end_lineno - node.lineno + 1
            if length > MAX_FUNCTION_LENGTH:
                self.issues.append({
                    "type": "Long Function",
                    "function": node.name,
                    "line": node.lineno,
                    "length": length
                })
        self.generic_visit(node)

    def get_issues(self):
        return self.issues
