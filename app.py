import re
from flask import Flask, request, Response
 
app = Flask(__name__)
 
@app.route("/v1/answer", methods=["POST"])
def answer():
    data = request.get_json(force=True, silent=True) or {}
    query = data.get("query", "")
    
    numbers = re.findall(r'\d+', query)
    
    if len(numbers) == 2:
        total = int(numbers[0]) + int(numbers[1])
        text = f"The sum is {total}."
    else:
        text = "I don't know"
    
    return Response(text, status=200, content_type="text/plain; charset=utf-8")
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
 
