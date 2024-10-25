import pytest
from ..ast import create_rule, evaluate_rule

def test_create_rule():
    rule_string = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule_string)
    assert ast is not None

def test_evaluate_rule():
    ast = create_rule("age > 30")
    data = {"age": 35}
    assert evaluate_rule(ast, data) == True
