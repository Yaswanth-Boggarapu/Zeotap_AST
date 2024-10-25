# backend/api.py
from flask import Flask, request, jsonify
from .ast import create_rule, combine_rules, evaluate_rule
from .database import save_rule, fetch_rules

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    try:
        # Log incoming request for debugging
        print("Received request for /create_rule:", request.json)

        rule_string = request.json['rule_string']
        
        # Check if rule_string is present
        if not rule_string:
            return jsonify({"error": "Missing rule_string in request"}), 400

        rule_ast = create_rule(rule_string)
        save_rule(rule_ast)

        return jsonify({"message": "Rule created successfully", "rule_ast": str(rule_ast)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/evaluate', methods=['POST'])
def evaluate_rule_endpoint():
    try:
        print("Received request for /evaluate:", request.json)

        ast = request.json['ast']
        data = request.json['data']

        # Validate inputs
        if ast is None or data is None:
            return jsonify({"error": "Missing ast or data in request"}), 400

        result = evaluate_rule(ast, data)
        return jsonify({"result": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
