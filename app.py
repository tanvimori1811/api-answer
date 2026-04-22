from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")

    # DATE extraction
    date_pattern = r'\b\d{1,2} (January|February|March|April|May|June|July|August|September|October|November|December) \d{4}\b'
    match = re.search(date_pattern, query)

    if match:
        return jsonify({"output": match.group()})

    return jsonify({"output": "Not found"})

if __name__ == "__main__":
    app.run()
