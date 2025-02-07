from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes.

def is_prime(n: int) -> bool:
    #Check if the number is a prime number.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    #Check if the number is a perfect number.
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n: int) -> bool:
    #Check if the number is an armstrong number.
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n

def is_odd(n: int) -> bool:
    #Check if the number is an odd number.
    return n % 2 != 0

def digit_sum(n: int) -> int:
    # Add up the didgits.
    return sum(int(d) for d in str(n))

def get_fun_fact(n: int) -> str:
    #Fetch a fun fact about the number from the Numbers API.
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return response.text
        else:
            return "No fun fact available."
    except Exception as e:
        return f"Error fetching fun fact: {e}"

# API Endpoint
@app.route('/api/number_classifier', methods=['GET'])
def classify_number():
    #Classify a number and return its properties.
    number = request.args.get('number')
    
    # Validate input
    if number is None or not number.isdigit():
        return jsonify({"error": True, "number": "alphabet"}), 400

    number = int(number)
    
    # Determine properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if is_odd(number):
        properties.append("odd")
    else:
        properties.append("even")

    # Construct JSON response in the required order
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(response)

# Run the API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
