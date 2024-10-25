import re

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f"Node(type={self.node_type}, value={self.value})"


import re

def parse_operand(operand_str):

    match = re.match(r'(\w+)\s*(=|>|<|>=|<=)\s*(.+)', operand_str.strip())
    if match:
        attribute, operator, value = match.groups()
        value = value.strip().strip("'\"")
        return Node("operand", value={"attribute": attribute, "operator": operator, "value": value})
    return None

def create_rule(rule_string):

    operators = ['AND', 'OR']
    tokens = re.split(r'\s+(AND|OR)\s+', rule_string)

    # Base case: Single condition, no operators
    if len(tokens) == 1:
        return parse_operand(tokens[0])

    # Recursive case: Break at the first operator and recursively create left and right nodes
    left = parse_operand(tokens[0])
    operator = tokens[1]
    right = parse_operand(tokens[2])

    return Node("operator", left=left, right=right, value=operator)


def combine_rules(rules, combine_operator="AND"):

    if len(rules) == 0:
        return None
    if len(rules) == 1:
        return rules[0]

    # Recursively combine all rules into a single AST
    combined_ast = rules[0]
    for rule in rules[1:]:
        combined_ast = Node("operator", left=combined_ast, right=rule, value=combine_operator)
    
    return combined_ast

def evaluate_rule(ast, data):

    if ast.node_type == "operand":
        # Extract the operand value (e.g., age > 30)
        attribute, operator, value = ast.value["attribute"], ast.value["operator"], ast.value["value"]
        # Convert to appropriate type
        actual_value = data.get(attribute)
        if actual_value is None:
            raise ValueError(f"Missing attribute: {attribute}")

        # Evaluate condition
        if operator == ">":
            return actual_value > float(value)
        elif operator == "<":
            return actual_value < float(value)
        elif operator == "=":
            return str(actual_value) == value
        elif operator == ">=":
            return actual_value >= float(value)
        elif operator == "<=":
            return actual_value <= float(value)
    elif ast.node_type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    return False

if __name__ == "__main__":
    # Example rule strings
    rule1_str = "(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')"
    rule2_str = "(age > 30 AND department = 'Marketing') AND (salary > 20000 OR experience > 5)"

    # Parse rules into ASTs
    rule1_ast = create_rule(rule1_str)
    rule2_ast = create_rule(rule2_str)

    # Combine rules into a single AST
    combined_ast = combine_rules([rule1_ast, rule2_ast], "AND")

    # Example data
    data1 = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    data2 = {"age": 23, "department": "Marketing", "salary": 18000, "experience": 2}

    # Evaluate rules
    print("Rule 1 AST:", rule1_ast)
    print("Rule 2 AST:", rule2_ast)
    print("Combined AST:", combined_ast)
    print(f"Evaluate data1: {evaluate_rule(combined_ast, data1)}")  # Expected: True
    print(f"Evaluate data2: {evaluate_rule(combined_ast, data2)}")  # Expected: False

