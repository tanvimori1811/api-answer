from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")

    # -------------------------
    # 1. DATE EXTRACTION
    # -------------------------
    date_pattern = r'\b\d{1,2} (January|February|March|April|May|June|July|August|September|October|November|December) \d{4}\b'
    date_match = re.search(date_pattern, query)

    if date_match:
        return jsonify({"output": date_match.group()})

    # -------------------------
    # 2. DATE FORMAT (DD/MM/YYYY)
    # -------------------------
    slash_date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
    slash_match = re.search(slash_date_pattern, query)

    if slash_match:
        return jsonify({"output": slash_match.group()})

    # -------------------------
    # 3. SIMPLE ADDITION
    # -------------------------
    numbers = list(map(int, re.findall(r'\d+', query)))
    if "add" in query.lower() or "+" in query or "sum" in query.lower():
        if len(numbers) >= 2:
            return jsonify({"output": f"The sum is {sum(numbers)}."})

    # -------------------------
    # 4. SUBTRACTION
    # -------------------------
    if "subtract" in query.lower() or "-" in query:
        if len(numbers) >= 2:
            result = numbers[0]
            for n in numbers[1:]:
                result -= n
            return jsonify({"output": f"The result is {result}."})

    # -------------------------
    # 5. MULTIPLICATION
    # -------------------------
    if "multiply" in query.lower() or "*" in query:
        if len(numbers) >= 2:
            result = 1
            for n in numbers:
                result *= n
            return jsonify({"output": f"The result is {result}."})

    # -------------------------
    # 6. DIVISION
    # -------------------------
    if "divide" in query.lower() or "/" in query:
        if len(numbers) >= 2 and numbers[1] != 0:
            result = numbers[0] / numbers[1]
            return jsonify({"output": f"The result is {result}."})

    # -------------------------
    # DEFAULT RESPONSE
    # -------------------------
    return jsonify({"output": "Unable to process the query."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
