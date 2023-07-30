from flask import Flask, jsonify, request, Blueprint

operations_bp = Blueprint('/operations', __name__)

operations = [
    {
        "name": "operation1",
        "parameters": {
            "name": "type",
            "name2": "type2"
        },
        "description": "This is operation 1."
    },
    {
        "name": "operation2",
        "parameters": {
            "name3": "type3",
            "name4": "type4"
        },
        "description": "This is operation 2."
    }
]

@operations_bp.route('/get_operations', methods=['GET'])
def get_operations():
    return jsonify({"operations": operations})

@operations_bp.route('/retrieve_operation_names', methods=['GET'])
def retrieve_operations():
    operation_names = [op['name'] for op in operations]
    return jsonify({"names" : operation_names})

@operations_bp.route('/retrieve_operation_parameters', methods=['POST'])
def retrieve_operation_parameters():
    data = request.json
    operation_name = data.get('operationName')
    operation = next((op for op in operations if op['name'] == operation_name), None)
    if operation:
        parameters = operation['parameters']
        print(parameters)
        return jsonify({"parameters": parameters})
    else:
        return jsonify({"error": "Operation not found."}), 404

@operations_bp.route('/retrieve_operation_description', methods=['POST'])
def retrieve_operation_description():
    data = request.json
    operation_name = data.get('operationName')
    operation = next((op for op in operations if op['name'] == operation_name), None)
    if operation:
        description = operation['description']
        return jsonify({"description": description})
    else:
        return jsonify({"error": "Operation not found."}), 404
