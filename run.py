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


def clean_worksheets(worksheet, worksheet_title):

    clean_worksheet = SHEET.worksheet(worksheet)
    clean_worksheet.clear()
    clean_worksheet.append_row(worksheet_title)


quantity_title = ["Number of Students", "Number of Questions"]
grade_ponderation_title = ["Student Name"]
results_title = ["Student Name", "Final Grade", "Pass"]

clean_worksheets("quantity", quantity_title)
clean_worksheets("grade", grade_ponderation_title)
clean_worksheets("ponderation", grade_ponderation_title)
clean_worksheets("results", results_title)


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
        print("Data should be two integer numbers, separated by commas.")
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
        elif any(x < 1 for x in quantity_data_int):
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
    print("Updating Quantity, Grade and Ponderation worksheets...\n")
    quantity_worksheet = SHEET.worksheet("quantity")
    quantity_worksheet.append_row(data_students_questions)
    print("Worksheets updated successfully.\n")


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
        grade_worksheet = SHEET.worksheet("grade")
        grade_worksheet.append_row(data_student_name)
        ponderationn_worksheet = SHEET.worksheet("ponderation")
        ponderationn_worksheet.append_row(data_student_name)
        results_worksheet = SHEET.worksheet("results")
        results_worksheet.append_row(data_student_name)

        print("Student name updated successfully.\n")  

    student_name = []
    student_name.append(get_students_name())
    update_student_name(student_name)
    
    def get_questions_score():
        """
        Function used to ask the user for the different scores of each of
        the input questions, for each student.
        Will ask for score between 0 and 100 points for each question .
        """
        while True:
            print(
                f"Please enter the score for each of the {quantity_questions} "
                f"questions for the student {student_name}."
                )
            print(
                f"You must input {quantity_questions} integer numbers "
                "separated with commas and each number should be "
                "between 0 and 100 points."
                )
            questions_score_str = input("Enter the scores here:")
            questions_score = questions_score_str.split(",")

            if validate_score(questions_score):
                print("Score for each question is valid!")
                break
        return questions_score

    def validate_score(score_values):
        """
        Function that validates the score input by the user for each question
        is between 0 and 100, only interger. Also will validate that the
        quantity of different score input is equal to the quantity of
        questions input. For each student.
        """
        quantity_score = score_values
        quantity_score_int = (int(x) for x in quantity_score)   
        try:
            [int(score) for score in score_values]
            if len(score_values) != quantity_questions:
                raise ValueError(
                    f"Exactly {quantity_questions} values required, you "
                    f"provided {len(score_values)}"
                ) 
            elif any(x < 0 or x > 100 for x in quantity_score_int):
                raise ValueError(
                    "Score of each questions must be between 0 and 100"
                )          

        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True
    
    def update_questions_score_worksheet(data_score_questions):
        """
        Function that add the score of each question for each one of the
        students to grade worksheet.
        """
        print("Updating grade worksheet...\n")
        score_worksheet = SHEET.worksheet("grade")
        score_worksheet.append_row(data_score_questions, table_range=f'B{i+1}')
        print("grade worksheet updated successfully.\n")

    data_score_questions = get_questions_score()
    quantity_data = [int(num) for num in data_score_questions]
    update_questions_score_worksheet(quantity_data)

    def get_questions_ponderation():
        """
        Function used to ask the user for the different ponderation of each of
        the input questions, for each student.
        Will ask for ponderation between 0 and 100 % for each question.
        Each % input per question added together should be exactly 100%.
        """
        while True:
            print(
                "Please enter the % of ponderation for each of the"
                f"{quantity_questions} questions for the student"
                f"{student_name}."
                )
            print(
                f"You must input {quantity_questions} integer numbers "
                "separated with commas and each number should be between "
                "0 and 100.\n"
                "For example an exam has two questions, first has a value "
                "of 40% and second 60%, both % add in total 100% of the grade "
                "of the exam."
                )
            questions_ponderation_str = input(
                "Enter the numbers that represent% here:"
                )
            questions_ponderation = questions_ponderation_str.split(",")

            if validate_ponderation(questions_ponderation):
                print("Porcentage for each question is valid!")
                break
        return questions_ponderation

    def validate_ponderation(ponderation_values):
        """
        Function that validates the porcentage input by the user for each
        question is between 0 and 100, only interger. Also will validate
        that the quantity of different porcentage input is equal to the
        quantity of questions input. Finally will validate that the sum
        of all the porcentage input is exactly 100%. For each student.
        """
        quantity_ponderation = ponderation_values
        quantity_ponderation_int = (int(x) for x in quantity_ponderation)
         
        try:
            [int(score) for score in ponderation_values]
            add_ponderation = sum(quantity_ponderation_int)
            if len(ponderation_values) != quantity_questions:
                raise ValueError(
                    f"Exactly {quantity_questions} values required, you provided\
                         {len(ponderation_values)}"
                ) 
            elif any(x < 0 or x > 100 for x in quantity_ponderation_int):
                raise ValueError(
                    "Porcentage for each questions must be between 0 and 100"
                )
            elif (add_ponderation != 100):
                raise ValueError(
                    "All the % input together must add 100%"
                )          

        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

        return True
    
    def update_questions_ponderation_worksheet(data_pond_questions):
        """
        Function that add the % of each question for each one of the students
        to ponderation worksheet.
        """
        print("Updating grade worksheet...\n")
        pond_worksheet = SHEET.worksheet("ponderation")
        pond_worksheet.append_row(data_pond_questions, table_range=f'B{i+1}')
        print("grade worksheet updated successfully.\n")

    data_pond_questions = get_questions_ponderation()
    quantity_ponderation = [int(num) for num in data_pond_questions]
    update_questions_ponderation_worksheet(quantity_ponderation)

    points_ponderated_question = []
    grade_student = []

    def get_grade():
        """
        """
        for data, ponderation in zip(quantity_data, quantity_ponderation):
            question = data*(ponderation/100)
            points_ponderated_question.append(question)
        round_list = [round(num) for num in points_ponderated_question]    
        grade_student = sum(x for x in round_list)
        
        print(f"The final grade for {student_name} is {grade_student}")
        return grade_student

    grade = get_grade()

    def get_pass_answer():
        """
        """ 
        if (grade >= 60):
            pass_grade = True
        else:
            pass_grade = False
        print(f"Pass:{pass_grade}")
        return pass_grade

    answer = get_pass_answer()

    def update_results_worksheet(grade_result, pass_result):
        """
        """
        print(f"Updating results worksheet with {student_name} reults")
        results_worksheet = SHEET.worksheet("results")
        results_worksheet.append_row(grade_result, table_range=f'B{i+1}')
        results_worksheet = SHEET.worksheet("results")
        results_worksheet.append_row(pass_result, table_range=f'C{i+1}')
        print("Results worksheet updated successfully.\n")

    final_grade = []
    final_pass_answer = []
    final_grade.append(grade)
    final_pass_answer.append(answer)
    update_results_worksheet(final_grade, final_pass_answer)
    