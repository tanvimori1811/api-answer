from flask import Flask, request, Response
import re

app = Flask(__name__)

@app.route('/v1/answer', methods=['POST'])
def answer():
    data = request.get_json()
    query = data.get("query", "")

    nums = list(map(int, re.findall(r'\d+', query)))

    if len(nums) == 2:
        result = nums[0] + nums[1]
        return Response(f"The sum is {result}.", mimetype="text/plain")

    return Response("I don't know", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
