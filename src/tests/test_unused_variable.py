from engine.analysis_engine import AnalysisEngine
from smells.unused_variable import UnusedVariableAnalyzer


def test_unused_variable():
    code = """
def test():
    x = 10
    return 5
"""
    engine = AnalysisEngine([UnusedVariableAnalyzer()])
    issues = engine.analyze(code)

    assert len(issues) == 1
    assert issues[0]["type"] == "Unused Variable"
