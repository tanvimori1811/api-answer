from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/v1/answer', methods=['POST'])
def answer():
    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"output": "I don't know"})

    query = data["query"].lower()

    # Extract numbers
    nums = list(map(int, re.findall(r'\d+', query)))

    if len(nums) >= 2:
        result = sum(nums)
        return jsonify({"output": f"The sum is {result}."})

    return jsonify({"output": "I don't know"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
