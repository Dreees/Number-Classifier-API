from flask import Flask

app = Flask(__name__)


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

@app.route('/')
def home():
    return "The Famous Number Classifier API!"

if __name__ == '__main__':
    app.run(debug=True)
