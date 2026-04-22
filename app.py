from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/v1/answer', methods=['POST'])
def answer():
    data = request.get_json()
    query = data.get("query", "")

    nums = list(map(int, re.findall(r'\d+', query)))
    
    if len(nums) == 2:
        result = nums[0] + nums[1]
        return f"The sum is {result}."

    return "I don't know"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
