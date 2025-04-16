from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend on different port to call the API

# In-memory vote count (reset on server restart)
votes = {
    "A": 0,
    "B": 0
}

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    choice = data.get('choice')

    if choice in votes:
        votes[choice] += 1
        return jsonify({"message": f"Vote for '{choice}' recorded successfully."}), 200
    else:
        return jsonify({"message": "Invalid vote option!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
