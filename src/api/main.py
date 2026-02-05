from fastapi import FastAPI
from pydantic import BaseModel

from engine.analysis_engine import AnalysisEngine
from smells.long_function import LongFunctionAnalyzer
from smells.unused_variable import UnusedVariableAnalyzer
from smells.deep_nesting import DeepNestingAnalyzer
from src.ml.model import predict_smell
class CodeRequest(BaseModel):
    code: str


class Issue(BaseModel):
    type: str
    line: int | None = None
    function: str | None = None
    variable: str | None = None
    length: int | None = None
    depth: int | None = None
app = FastAPI(
    title="AI-assisted Code Review Tool",
    description="Static code analysis service for Python",
    version="1.0.0"
)

engine = AnalysisEngine([
    LongFunctionAnalyzer(),
    UnusedVariableAnalyzer(),
    DeepNestingAnalyzer()
])
@app.post("/analyze")
def analyze_code(request: CodeRequest):
    static_issues = engine.analyze(request.code)
    ml_flag = predict_smell(request.code)

    return {
        "static_issues": static_issues,
        "ml_prediction": "code_smell" if ml_flag else "clean"
    }
