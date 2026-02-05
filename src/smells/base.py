import ast
from abc import ABC, abstractmethod


class CodeSmellAnalyzer(ast.NodeVisitor, ABC):
    def __init__(self):
        self.issues = []

    @abstractmethod
    def get_issues(self):
        pass
