from flask import Flask, request, jsonify

app = Flask(__name__)

# POST method
@app.route('/bfhl', methods=['POST'])
def handle_post():
    return jsonify({"message": "POST request received"}), 200

# GET method
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
