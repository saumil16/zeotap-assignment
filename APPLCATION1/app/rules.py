# app/rules.py
from app.ast import Node

def create_rule(rule_string):
    # Placeholder implementation for demonstration purposes
    age_node = Node("operand", value=("age", ">", 30))
    department_node = Node("operand", value=("department", "=", "Sales"))
    salary_node = Node("operand", value=("salary", ">", 50000))
    experience_node = Node("operand", value=("experience", ">", 5))

    or_node1 = Node("operator", left=age_node, right=department_node, value="AND")
    or_node2 = Node("operator", left=Node("operand", value=("age", "<", 25)), right=Node("operand", value=("department", "=", "Marketing")), value="AND")
    and_node = Node("operator", left=Node("operator", left=or_node1, right=or_node2, value="OR"), right=Node("operator", left=salary_node, right=experience_node, value="OR"), value="AND")

    return and_node

def combine_rules(rules):
    if not rules:
        return None

    combined_ast = rules[0]
    for rule in rules[1:]:
        combined_ast = Node("operator", left=combined_ast, right=rule, value="AND")

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

def serialize_ast(node):
    if node is None:
        return None
    return {
        'node_type': node.node_type,
        'value': node.value,
        'left': serialize_ast(node.left),
        'right': serialize_ast(node.right)
    }

def deserialize_ast(node_dict):
    if node_dict is None:
        return None
    return Node(
        node_type=node_dict['node_type'],
        value=node_dict.get('value'),
        left=deserialize_ast(node_dict.get('left')),
        right=deserialize_ast(node_dict.get('right'))
    )
