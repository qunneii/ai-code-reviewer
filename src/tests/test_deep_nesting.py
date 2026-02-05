from engine.analysis_engine import AnalysisEngine
from smells.deep_nesting import DeepNestingAnalyzer


def test_deep_nesting():
    code = """
def test():
    for i in range(3):
        if i > 0:
            for j in range(3):
                if j > 1:
                    print(i, j)
"""
    engine = AnalysisEngine([DeepNestingAnalyzer()])
    issues = engine.analyze(code)

    assert len(issues) >= 1
