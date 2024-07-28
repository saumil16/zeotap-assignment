# tests/test_rules.py
import unittest
from app.rules import create_rule, combine_rules, evaluate_rule, serialize_ast, deserialize_ast

class TestRules(unittest.TestCase):
    def test_create_rule(self):
        rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)
        print("Created AST:", ast)

    def test_combine_rules(self):
        rule1 = create_rule("((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)")
        rule2 = create_rule("((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)")
        combined_ast = combine_rules([rule1, rule2])
        self.assertIsNotNone(combined_ast)
        print("Combined AST:", combined_ast)

    def test_evaluate_rule(self):
        rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        ast = create_rule(rule_string)
        data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        result = evaluate_rule(ast, data)
        print("Evaluation Result:", result)
        self.assertTrue(result)

    def test_serialize_deserialize(self):
        rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        ast = create_rule(rule_string)
        serialized_ast = serialize_ast(ast)
        deserialized_ast = deserialize_ast(serialized_ast)
        data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        result = evaluate_rule(deserialized_ast, data)
        print("Evaluation Result after Serialization/Deserialization:", result)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
