from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/v1/answer', methods=['POST'])
def answer():
    data = request.get_json()
    query = data.get("query", "").strip()

    try:
        nums = list(map(int, re.findall(r'-?\d+', query)))

        if len(nums) >= 2:
            result = sum(nums)

            # EXACT formatting
            output = f"The sum is {result}."
            return jsonify({"output": output})

    except:
        pass

    return jsonify({"output": "I don't know."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
