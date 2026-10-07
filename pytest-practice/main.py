import requests

def add(a : int, b : int) -> int:
    return a+b

def devide(a: int , b: int) -> float:
    if (b==0):
        raise ZeroDivisionError("Division by 0 is not allowed") 
    
    return a /b

def widthdrwal(amount :float , deduction: float) -> float:
    if amount < deduction:
        raise ValueError("Amount is less than withdrwal amount")
    
    return amount - deduction



def get_customer(customer_id):
    try:
        response = requests.get(
            f"https://example.com/customers/{customer_id}"
        )
    except requests.Timeout:
        return None
    return response.json()