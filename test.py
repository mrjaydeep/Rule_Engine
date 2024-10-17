import unittest

# Assuming your main code is in a file named rule_engine.py
from sol import Node, create_rule, evaluate_rule, combine_rules

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        # Test the creation of rule1
        rule1_ast = create_rule("rule1")
        self.assertIsNotNone(rule1_ast)
        self.assertEqual(rule1_ast.type, 'operator')

    def test_evaluate_rule(self):
        # Test evaluating rule1 against sample data
        rule1_ast = create_rule("rule1")
        data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        result = evaluate_rule(rule1_ast, data)
        self.assertTrue(result)  # Expecting True for this input

    def test_evaluate_rule2(self):
        # Test evaluating rule2 against sample data
        rule2_ast = create_rule("rule2")
        data = {"age": 25, "department": "Marketing", "salary": 60000, "experience": 3}
        result = evaluate_rule(rule2_ast, data)
        self.assertFalse(result)  # Expecting False for this input

    def test_combined_rules(self):
        # Test combining two rules
        rule1_ast = create_rule("rule1")
        rule2_ast = create_rule("rule2")
        combined_ast = combine_rules([rule1_ast, rule2_ast])
        self.assertIsNotNone(combined_ast)
        self.assertEqual(combined_ast.type, 'operator')


if __name__ == '__main__':
    unittest.main()
