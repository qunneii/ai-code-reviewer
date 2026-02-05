from engine.analysis_engine import AnalysisEngine
from smells.long_function import LongFunctionAnalyzer
from smells.unused_variable import UnusedVariableAnalyzer
from smells.deep_nesting import DeepNestingAnalyzer


if __name__ == "__main__":
    with open("example.py") as f:
        code = f.read()

    engine = AnalysisEngine([
        LongFunctionAnalyzer(),
        UnusedVariableAnalyzer(),
        DeepNestingAnalyzer()
    ])

    issues = engine.analyze(code)

    for issue in issues:
        print(issue)
