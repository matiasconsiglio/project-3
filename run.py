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

print(
    "This program calculates the final grade of an exam. "
    "First takes as input the quantity of students and questions of the exam. "
    "Second takes as input the score per question and the percentage each "
    "question ponderates from the global grade. "
    "In this hypotetical program the grading works from 0 to 100 points. "
    "0 is the minumum score and 100 is the maximum score. "
    "To pass the student needs to have a score higher or equal to 60 points. "
    "For example an exam has 2 questions. A random student gets 30 points "
    "in the first question and 80 points in the second. "
    "The first question has a weight of 30% of the global grade and "
    "the second question has a weight of 70% of the global grade. "
    "The student global grade would be 65 points. Pass.\n "
)


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
    quantity = values
    quantity_data_int = (int(x) for x in quantity)   
    try:
        [int(value) for value in values]
        if len(values) != 2:
            raise ValueError(
                f"Exactly 2 values required, you provided {len(values)}"
            ) 
        elif all(x < 1 for x in quantity_data_int):
            raise ValueError(
                "Student and questions must be atleast 1"
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
    grade_title_points.append(f'Question {ind} (xpts)')


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
    ponderation_title_percentage.append(f'Question {ind} (x%)')


def update_ponderation_worksheet_title(ponderation_title_worksheet):
    """
    Update ponderation worksheet with title. 
    If user input 3 question for the exam this will update the ponderation
    worksheet title with 3 columns.
    Question 1 % to Question 3 % Starting in B1.
    A1 starts with Student Name.
    """
    pond_worksheet = SHEET.worksheet("ponderation")
    pond_worksheet.append_row(ponderation_title_worksheet, table_range='B1')


update_ponderation_worksheet_title(ponderation_title_percentage)

number_students = int(data_students_questions[0])

for i in range(1, number_students + 1):
    
    def get_students_name():
        """
        Function used to ask the user for the different names of the students.
        Will ask for the exact amount of names as students input from user.
        """
    
        while True:
            print(f"Please enter the name of the student {i}")
            print("The name must only contain letters")
            student_name = input("Enter de name:")

            if validate_name(student_name):
                print("The name is valid!")
                break
        return student_name
    
    def validate_name(name_value):
        """
        Function that validates the name of the students is only alphabetic.
        """

        try:
            if name_value.isalpha():
                return True

            else:
                raise ValueError(
                    "The student name must be conformed by letters"
                )
                return False
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
        return True

    def update_student_name(data_student_name):
        """
        Function that add the name of the students to grade and
        ponderation spreedsheets
        """
        print("Updating grade and ponderation worksheet...\n")
        print(data_student_name)
        gradee_worksheet = SHEET.worksheet("grade")
        gradee_worksheet.append_row(data_student_name)
        ponderationn_worksheet = SHEET.worksheet("ponderation")
        ponderationn_worksheet.append_row(data_student_name)
        print("Student name updated successfully.\n")  

    student_name = []
    student_name.append(get_students_name())
    update_student_name(student_name)

    

