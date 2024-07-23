from ast import Node

def create_rule(rule_string):
    age_node = Node("operand", value=("age", ">", 30))
    department_node = Node("operand", value=("department", "=", "Sales"))
    salary_node = Node("operand", value=("salary", ">", 50000))
    experience_node = Node("operand", value=("experience", ">", 5))

    and_node1 = Node("operator", left=age_node, right=department_node)
    and_node2 = Node("operator", left=salary_node, right=experience_node)

    root_node = Node("operator", left=and_node1, right=and_node2)

    return root_node

def combine_rules(rules):
    if not rules:
        return None

    combined_ast = rules[0]
    for rule in rules[1:]:
        combined_ast = Node("operator", left=combined_ast, right=rule, node_type="AND")

    return combined_ast

def evaluate_node(node, data):
    if node.node_type == "operand":
        attribute, operator, value = node.value
        if operator == ">":
            return data[attribute] > value
        elif operator == "<":
            return data[attribute] < value
        elif operator == "=":
            return data[attribute] == value
    elif node.node_type == "operator":
        if node.value == "AND":
            return evaluate_node(node.left, data) and evaluate_node(node.right, data)
        elif node.value == "OR":
            return evaluate_node(node.left, data) or evaluate_node(node.right, data)
    return False

def evaluate_rule(ast, data):
    return evaluate_node(ast, data)