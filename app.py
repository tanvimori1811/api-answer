from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.route("/v1/answer", methods=["POST"])
def answer():
    data = request.get_json(force=True, silent=True) or {}
    query = data.get("query", "").strip()

    q = query.lower()

    # -------- LEVEL 1 --------
    nums = re.findall(r'\d+', q)
    if len(nums) >= 2 and ("+" in q or "sum" in q):
        total = int(nums[0]) + int(nums[1])
        return jsonify({"output": f"The sum is {total}."})

    # -------- LEVEL 2 --------
    date_match = re.search(r'\b(\d{1,2} [A-Za-z]+ \d{4})\b', query)
    if date_match:
        return jsonify({"output": date_match.group(1)})

    # -------- LEVEL 3 --------
    num_match = re.search(r'\d+', q)
    if num_match:
        num = int(num_match.group())

        if "odd" in q:
            return jsonify({"output": "YES" if num % 2 != 0 else "NO"})

        if "even" in q:
            return jsonify({"output": "YES" if num % 2 == 0 else "NO"})

    return jsonify({"output": ""})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
