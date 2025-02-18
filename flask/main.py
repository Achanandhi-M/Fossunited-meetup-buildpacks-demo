from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask app!"

# A simple route to return JSON data
@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        'message': 'This is a simple API endpoint!',
        'status': 'success'
    })

# A route to demonstrate handling POST requests with JSON data
@app.route('/api/post', methods=['POST'])
def post_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    return jsonify({
        'message': 'Data received successfully!',
        'your_data': data
    }), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
