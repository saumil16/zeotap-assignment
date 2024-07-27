from flask import request, jsonify
from rules import create_rule, combine_rules, evaluate_rule
from database import save_rule, load_rules

def init_app(app):
    @app.route('/create_rule', methods=['POST'])
    def create_rule_api():
        rule_string = request.json.get('rule_string')
        ast = create_rule(rule_string)
        save_rule(rule_string, ast)
        return jsonify({"status": "success", "ast": repr(ast)})

    @app.route('/combine_rules', methods=['POST'])
    def combine_rules_api():
        rule_strings = request.json.get('rule_strings')
        rules = [create_rule(rule) for rule in rule_strings]
        combined_ast = combine_rules(rules)
        save_rule("combined_rule", combined_ast)
        return jsonify({"status": "success", "combined_ast": repr(combined_ast)})

    @app.route('/evaluate_rule', methods=['POST'])
    def evaluate_rule_api():
        ast = request.json.get('ast')
        data = request.json.get('data')
        result = evaluate_rule(ast, data)
        return jsonify({"status": "success", "result": result})