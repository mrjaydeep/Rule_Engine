class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # Left child (Node)
        self.right = right  # Right child (Node)
        self.value = value  # Value for operand nodes

    def __repr__(self):
        return f"Node(type={self.type}, left={self.left}, right={self.right}, value={self.value})"


def create_rule(rule_string):
    if rule_string == "rule1":
        return Node('operator', 
                    value='OR',  
                    left=Node('operator', 
                              value='AND',  
                              left=Node('operand', value='age > 30'), 
                              right=Node('operand', value="department = 'Sales'")),
                    right=Node('operator', 
                               value='OR',  
                               left=Node('operand', value="age < 25"), 
                               right=Node('operand', value="department = 'Marketing'")))
    elif rule_string == "rule2":
        return Node('operator', 
                    value='AND',  
                    left=Node('operand', value="age > 30"), 
                    right=Node('operand', value="department = 'Marketing'"))
    else:
        raise ValueError("Unknown rule")


def combine_rules(rules):
    if len(rules) < 2:
        raise ValueError("At least two rules are required to combine.")
    
    combined_root = Node('operator', value='AND', left=rules[0], right=rules[1])
    return combined_root


def evaluate_rule(ast, data):
    if ast.type == 'operand':
        condition = ast.value
        field, operator, value = parse_condition(condition)
        return evaluate_condition(data.get(field), operator, value)
    elif ast.type == 'operator':
        left_eval = evaluate_rule(ast.left, data)
        right_eval = evaluate_rule(ast.right, data)
        if ast.value == 'AND':
            return left_eval and right_eval
        elif ast.value == 'OR':
            return left_eval or right_eval
        else:
            raise ValueError("Unknown operator in AST")


def parse_condition(condition):
    field, operator_value = condition.split(" ", 1)
    operator, value = operator_value.split(" ", 1)
    return field, operator, value


def evaluate_condition(field_value, operator, value):
    if operator == '>':
        return field_value > int(value)
    elif operator == '<':
        return field_value < int(value)
    elif operator == '=':
        return field_value == value.strip("'")
    else:
        raise ValueError("Unknown operator")


def print_ast(node, level=0):
    if node is not None:
        print(" " * level + f"Node(type={node.type}, value={node.value})")
        print_ast(node.left, level + 2)
        print_ast(node.right, level + 2)


# Example usage
rule1_ast = create_rule("rule1")
rule2_ast = create_rule("rule2")
combined_ast = combine_rules([rule1_ast, rule2_ast])

# Print the AST structure for debugging
print_ast(combined_ast)

# Sample data
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result = evaluate_rule(combined_ast, data)

print(f"Evaluation result: {result}")
