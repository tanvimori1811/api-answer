import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/v1/answer", methods=["POST"])
def answer():
    data = request.get_json(force=True, silent=True) or {}
    query = data.get("query", "")

    # -------- LEVEL 1: SUM --------
    nums = re.findall(r'\d+', query)
    if len(nums) >= 2 and ("+" in query or "sum" in query.lower()):
        total = int(nums[0]) + int(nums[1])
        return Response(f"The sum is {total}.", content_type="text/plain")

    # -------- LEVEL 2: DATE --------
    match = re.search(r'\b(\d{1,2} [A-Za-z]+ \d{4})\b', query)
    if match:
        return Response(match.group(1), content_type="text/plain")

    # -------- LEVEL 3: ODD / EVEN --------
    match = re.search(r'\d+', query)
    if match:
        num = int(match.group())

        if "odd" in query.lower():
            return Response("YES" if num % 2 != 0 else "NO", content_type="text/plain")

        if "even" in query.lower():
            return Response("YES" if num % 2 == 0 else "NO", content_type="text/plain")

    return Response("I don't know", content_type="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
