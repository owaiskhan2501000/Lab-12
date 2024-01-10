class CustomException(Exception):
    def __init__(self, message="A custom exception occurred"):
        self.message = message
        super().__init__(self.message)

def check_condition(value):
    if value < 0:
        raise CustomException("Value cannot be negative")

try:
    user_input = int(input("Enter a non-negative number: "))
    check_condition(user_input)
    print(f"The entered value is: {user_input}")
except CustomException as ce:
    print(f"CustomException: {ce}")
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
