from flask import Flask, request, Response
import re

app = Flask(__name__)

@app.route('/v1/answer', methods=['POST'])
def answer():
    try:
        data = request.get_json(force=True) or {}
        query = data.get("query", "")

        # Extract numbers
        nums = list(map(int, re.findall(r'\d+', query)))

        if len(nums) == 2:
            result = nums[0] + nums[1]

            # EXACT required output (no newline, no JSON)
            return Response(
                f"The sum is {result}.",
                content_type="text/plain; charset=utf-8"
            )

        return Response("I don't know", content_type="text/plain; charset=utf-8")

    except Exception:
        return Response("I don't know", content_type="text/plain; charset=utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
