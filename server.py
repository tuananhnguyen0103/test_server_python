from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/getvalue', methods=['POST'])
def your_api_endpoint():
    # Access the data sent to the API
    data = request.json

    # Process the data (e.g., pass it to your Rasa model)

    # Prepare the response
    response = {
        'message': 'Your response message'
    }

    # Return the response as JSON
    return jsonify(response)

@app.route('/api/hello', methods=['GET'])
def hello():
    # Prepare the response
    response = {
        'message': 'Hello, how are you'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8686)
