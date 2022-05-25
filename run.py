import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project_3')

def get_quantity_students_questions_data():
    """
    Get quantity of students and quantity of questions the exam has.
    input from user.
    """
    while True:

        print("Please enter quantity of students and questions from exam")
        print("Data should be two numbers, separated by commas.")
        print("Example: 2,3")

        quantity_str = input("Enter your data here: ")

        quantity_data = quantity_str.split(",")

        if validate_data(quantity_data):
            print("Data is valid!")
            break

    return quantity_data

#data_quantity = get_quantity_students_questions_data()

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 2 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 2:
            raise ValueError(
                f"Exactly 2 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

data_students_questions = get_quantity_students_questions_data()
quantity_data = [int(num) for num in data_students_questions]
