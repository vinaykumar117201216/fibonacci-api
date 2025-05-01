from flask import Flask, request, jsonify


app = Flask(__name__)

def fibonacci(n):
    if n < 0:
        return "Invalid input", 400
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    try:
        n = int(request.args.get('n', ''))
    except (TypeError, ValueError):
        return jsonify({"error": "InvalidEntry, provide an integer."}), 400    
    result = fibonacci(n)
    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    return jsonify({"n": n, "fibonacci": result})


if __name__ == '__main__':
    app.run(debug=True)
