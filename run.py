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
    
    print("Please enter quantity of students and questions from exam")
    print("Data should be two numbers, separated by commas.")
    print("Example: 2,3")

    quantity_str = input("Enter your data here: ")

    quantity_data = quantity_str.split(",")

    return quantity_data

data = get_quantity_students_questions_data()

data1 = data[0]

print(data1)