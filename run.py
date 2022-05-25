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
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 2 numbers separated
    by comma. The loop will repeatedly request data, until it is valid.
    Code adapted from love-sandwiches example project from CI course.
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


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 2 values.
    Code adapted from love-sandwiches example project from CI course.
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


def update_data_quantity_worksheet(data_students_questions):
    """
    Update quantity worksheet, add new row with the list data provided.
    Code adapted from love-sandwiches example project from CI course.
    """
    print("Updating Quantity worksheet...\n")
    quantity_worksheet = SHEET.worksheet("quantity")
    quantity_worksheet.append_row(data_students_questions)
    print("quantity worksheet updated successfully.\n")


data_students_questions = get_quantity_students_questions_data()
quantity_data = [int(num) for num in data_students_questions]
update_data_quantity_worksheet(quantity_data)

quantity_questions = quantity_data[1]

grade_title_points = []

for ind in range(1, quantity_questions + 1):
    grade_title_points.append(f'Question {ind} (pts)')


def update_grade_worksheet_title(grade_title_worksheet):
    """
    Update grade worksheet with title, if user input 3 question for the exam,
    this will update the grade worksheet title with 3 columns.
    Question 1 (pts) to Question 3 (pts) Starting in B1.
    A1 starts with Student Name.
    """
    grade_worksheet = SHEET.worksheet("grade")
    grade_worksheet.append_row(grade_title_worksheet, table_range='B1')


update_grade_worksheet_title(grade_title_points)

ponderation_title_percentage = []

for ind in range(1, quantity_questions + 1):
    ponderation_title_percentage.append(f'Question {ind} %')


def update_ponderation_worksheet_title(ponderation_title_worksheet):
    """
    Update ponderation worksheet with title, 
    if user input 3 question for the exam,
    this will update the ponderation worksheet title with 3 columns.
    Question 1 % to Question 3 % Starting in B1.
    A1 starts with Student Name.
    """
    pond_worksheet = SHEET.worksheet("ponderation")
    pond_worksheet.append_row(ponderation_title_worksheet, table_range='B1')


update_ponderation_worksheet_title(ponderation_title_percentage)




