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
    """
    First function called to clean the worksheets.
    Generates new titles for worksheets every time
    the program is run.

    Parameters:
    worksheet: str with the name of the worksheet.
    worksheet_title: str with the title for each
    worksheet.
    """
    clean_worksheet = SHEET.worksheet(worksheet)
    clean_worksheet.clear()
    clean_worksheet.append_row(worksheet_title)


def get_quantity_students_questions_data():
    """
    Get quantity of students and quantity of questions the exam has.
    input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 2 numbers separated
    by comma. The loop will repeatedly request data, until it is valid.
    Code adapted from love-sandwiches example project from CI course.

    Returns:
    quantity_data: List with 2 strings separated by comma, Example ['2','3']
    """
    while True:
        print("Please enter quantity of students and questions from the exam.")
        print("Data should be two integer numbers, separated by commas.")
        print("Example: 2,3")
        quantity_str = input("Enter your data here:\n")
        quantity_data = quantity_str.split(",")
        if validate_data(quantity_data):
            print("Data is valid!")
            break
    return quantity_data


def validate_data(data_students_questions):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 2 values.
    Code adapted from love-sandwiches example project from CI course.

    Parameters:
    data_students_questions: Take as parameter quantity_data return from
    get_quantity_students_questions_data(). List of 2 strings.

    Return:
    boolean: True if all conditions apply as asked by the function.
    False if not.
    """
    try:
        quantity_data_int = [int(x) for x in data_students_questions]
        if len(quantity_data_int) != 2:
            raise ValueError(
                "Exactly 2 values required, you provided"
                f"{len(quantity_data_int)}\n"
            )
        elif any(x < 1 for x in quantity_data_int):
            raise ValueError(
                "Student and questions must be at least 1\n"
            )
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True


def update_data_quantity_worksheet(data_students_questions):
    """
    Update quantity worksheet, add new row with the list data provided.
    Code adapted from love-sandwiches example project from CI course.

    Parameters:
    data_students_questions list: Take as parameter quantity_data return from
    get_quantity_students_questions_data(). List of 2 strings.
    """
    print("Updating Quantity, Grade and Ponderation worksheets...\n")
    quantity_worksheet = SHEET.worksheet("quantity")
    quantity_worksheet.append_row(data_students_questions)
    print("Worksheets updated successfully.\n")


def generate_grade_ponderation_title(data_students_questions, worksheet_title):
    """
    Generates title for grade and ponderation title worksheets.
    will vary depending on the quantity of questions as input.

    Parameters:
    data_students_questions list: Take as parameter quantity_data return from
    get_quantity_students_questions_data(). List of 2 strings.
    Worksheet_title: string that depending if used for grade or
    ponderation worksheet will input points or %.

    Return:
    list: List with strings including title for each column for
    grade and ponderation worksheets.
    """
    quantity_questions = data_students_questions[1]
    grade_ponderation_title_points = []
    for ind in range(1, quantity_questions + 1):
        grade_ponderation_title_points.append(
            f'Question {ind} {worksheet_title}'
            )
    return grade_ponderation_title_points


def update_grade_ponderation_title(
    data_students_questions, worksheet_to_update, location
):
    """
    Update grade or ponderation worksheet with title, if user input 3 question
    for the exam, this will update the grade worksheet title with 3 columns.
    Question 1 (xpts) to Question 3 (xpts) Starting in B1.
    A1 starts with Student Name. This scenario will update the ponderation
    worksheet title with 3 columns.
    Question 1 (x%) to Question 3 (x%) Starting in A1.

    Parameters:
    data_students_questions list: Take as parameter quantity_data return from
    get_quantity_students_questions_data(). List of 2 strings.
    worksheet_to_update: String that input worksheet to update.
    location: String that input location in the worksheet to update the title.
    """
    grade_worksheet = SHEET.worksheet(worksheet_to_update)
    grade_worksheet.append_row(data_students_questions, table_range=location)


def get_students_name(number_name):
    """
    Function used to ask the user for the different names of the students.
    Will ask for the exact amount of names as students input from the user.
    Use while until the input is valid as asked.

    Parameters:
    number_name: int used for loop for asking student name depending on input
    of how many students did the exam.

    Returns:
    student_name: list with one string containing student name for n.
    """
    while True:
        print(f"Please enter the name of the student {number_name}.")
        print("The name must contain letters. Also space is allowed.")
        student_name = input("Enter the name:\n")
        if validate_name(student_name):
            print("The name is valid!")
            break
    return student_name


def validate_name(name_value):
    """
    Function that validates the name of the students is only alphabetic.
    Also allow to have 'space' in case the input is first name and last
    name.

    Parameters:
    name_value: takes as input student_name list with one string containing
    the student name.

    Returns:
    boolean: True if student_name only contains alphabetic characters. False
    if not.
    """
    try:
        if all(x.isalpha or x.isspace for x in name_value):
            return True

        else:
            raise ValueError(
                "The student name must be conformed by letters\n"
            )
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False
    return True


def update_student_name(name_value):
    """
    Function that adds the name of the students to grade worksheet.

    Parameters:
    name_value: takes as input student_name list with one string containing
    student name for n.
    """
    print("Updating grade and results worksheet...\n")
    grade_worksheet = SHEET.worksheet("grade")
    grade_worksheet.append_row(name_value)
    results_worksheet = SHEET.worksheet("results")
    results_worksheet.append_row(name_value)
    print("Student name updated successfully.\n")


def get_questions_ponderation(quantity_questions_exam):
    """
    Function used to ask the user for the different ponderation of each of
    the input questions, for each student.
    Will ask for ponderation numbers between 0 and 100 % for each question.
    Each % input per question added together should be exactly 100%.

    Parameters:
    quantity_questions_exam: int that indicates the quantity of questions
    the user input that the exam has.

    Return:
    questions_ponderation: list with str that contains the ponderation of
    each question the exam has.
    """
    while True:
        print(
            "Please enter the % of ponderation for each of the "
            f"{quantity_questions_exam} question(s) of the exam"
            )
        print(
            f"You must input {quantity_questions_exam} integer numbers "
            "separated with commas and each number should be between "
            "0 and 100.\n"
            "For example an exam has two questions, first has a value "
            "of 40% and second 60%, both % add in total 100% of the grade "
            "of the exam."
            )
        questions_ponderation_str = input(
            "Enter the numbers that represent each % here:\n"
            )
        questions_ponderation = questions_ponderation_str.split(",")

        if validate_ponderation(
            questions_ponderation, quantity_questions_exam
        ):
            print("Percentage for each question is valid!")
            break
    return questions_ponderation


def validate_ponderation(ponderation_values, quantity_questions_exam):
    """
    Function that validates the percentage input by the user for each
    question must be between 0 and 100, only integers. Also will validate
    that the quantity of different percentage input is equal to the
    quantity of questions input. Finally will validate that the sum
    of all the porcentage input is exactly 100%. For each student.

    Parameters:
    ponderation_values:list with str that contains the ponderation of
    each question the exam has.
    quantity_questions_exam: int that indicates the quantity of questions
    the user input that the exam has.
    Returns:
    boolean: True if all conditions apply as asked by the function.
    False if not.
    """
    try:
        quantity_ponderation_int = [int(x) for x in ponderation_values]
        add_ponderation = sum(quantity_ponderation_int)
        if len(ponderation_values) != quantity_questions_exam:
            raise ValueError(
                f"Exactly {quantity_questions_exam} values required, you provided\
                        {len(ponderation_values)}\n"
            )
        elif add_ponderation != 100:
            raise ValueError(
                "All the % input together must add 100%\n"
            )
        elif any(x <= 0 or x > 100 for x in quantity_ponderation_int):
            raise ValueError(
                "Percentage for each questions must be between 0 and 100\n"
            )

    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True


def update_questions_ponderation_worksheet(ponderation_values):
    """
    Function that add the % of each question for each one of the students
    to the ponderation worksheet.
    Parameters:
    ponderation_values:list with str that contains the ponderation of
    each question the exam has.
    """
    print("Updating ponderation worksheet...\n")
    pond_worksheet = SHEET.worksheet("ponderation")
    pond_worksheet.append_row(ponderation_values)
    print("Ponderation worksheet updated successfully.\n")


def get_questions_score(quantity_questions_exam, name_value):
    """
    Function used to ask the user for the different scores of each of
    the quantity input questions, for each student.
    Will ask for a score between 0 and 100 points for each question.

    Parameters:
    quantity_questions_exam: int that indicates the quantity of questions
    the user input that the exam has.
    name_value: takes as input student_name list with one string containing
    student name for n.

    Return:
    questions_score: list with str that contain each score from each
    question from the exam.
    """
    while True:
        print(
            f"Please enter the score for each of the {quantity_questions_exam}"
            f" questions for the student {name_value}."
            )
        print(
            f"You must input {quantity_questions_exam} integer numbers "
            "separated with commas and each number should be "
            "between 0 and 100 points."
            )
        questions_score_str = input("Enter the scores here:\n")
        questions_score = questions_score_str.split(",")

        if validate_score(questions_score, quantity_questions_exam):
            print("Score for each question is valid!")
            break
    return questions_score


def validate_score(score_values, quantity_questions_exam):
    """
    Function that validates the score input by the user for each question
    is between 0 and 100, only integer. Also validates that the
    quantity of different score input is equal to the quantity of
    questions input. For each student.

    Parameters:
    score_values: questions_score return from get_questions_score
    list with str that contain each score from each question from
    exam.
    quantity_questions_exam: int that indicates the quantity of questions
    the user input that the exam has.

    Returns:
    boolean: True if all conditions apply as asked by the function.
    False if not.
    """
    try:
        quantity_score_int = [int(x) for x in score_values]
        if len(score_values) != quantity_questions_exam:
            raise ValueError(
                f"Exactly {quantity_questions_exam} values required, you "
                f"provided {len(score_values)}\n"
            )
        elif any(x < 0 or x > 100 for x in quantity_score_int):
            raise ValueError(
                "Score of each questions must be between 0 and 100\n"
            )

    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False
    return True


def update_questions_score_worksheet(score_values, n):
    """
    Function that add the score of each question for each one of the
    students to grade the worksheet.

    Parameters:
    score_values: questions_score return from get_questions_score
    list with str that contain each score from each question from
    exam.
    n: indicates which students the loop is when this function is called.
    helps to indicate where to locate the data in the grade worksheet.
    """
    print("Updating grade worksheet...\n")
    score_worksheet = SHEET.worksheet("grade")
    score_worksheet.append_row(score_values, table_range=f'B{n+1}')
    print("Grade worksheet updated successfully.\n")


def get_grade(data_students_questions, ponderation_values, name_value):
    """
    Function that calculates the final grade for each student, taking as input
    the score for each question of the student, the ponderation of each
    question and the student.

    Parameters:
    data_students_questions list: Take as parameter quantity_data return from
    get_quantity_students_questions_data(). List of 2 strings.
    ponderation_values:list with str that contains the ponderation of
    each question the exam has.
    name_value: takes as input student_name list with one string containing
    student name for n.

    Returns
    grade_student: int that corresponds to the final grade of the student n.
    """
    points_ponderated_question = []
    grade_student = []
    for data, ponderation in zip(data_students_questions, ponderation_values):
        question = data*(ponderation/100)
        points_ponderated_question.append(question)
    round_list = [round(num) for num in points_ponderated_question]
    grade_student = sum(x for x in round_list)
    print(f"The final grade for {name_value} is {grade_student} points.")
    return grade_student


def get_pass_answer(grade):
    """
    Function that takes as input the final grade of the student n.
    calculates if the student passes the exam or not.

    Parameters:
    grade: int, return from get_grade() grade_student:
    int that correspond to the final grade of the student n.
    Returns:
    boolean: True if grade is equal or higher than 60 points.
    else false. if True student Pass
    """
    if (grade >= 60):
        pass_grade = True
    else:
        pass_grade = False
    print(f"Pass:{pass_grade}")
    return pass_grade


def update_results_worksheet(
    grade, pass_result, name_value, number_name
):
    """
    Function that updates the result worksheet for the student n with
    final grade score and boolean for Passing.

    Parameters:
    grade: int, return from get_grade() grade_student:
    int that correspond to the final grade of the student n.
    pass_result: boolean True if grade is equal or higher than 60 points.
    else false. if True student Pass.
    name_value: takes as input student_name list with one string containing
    student name for n.
    number_name: indicates which students the loop is when this function
    is called. Helps to indicate where to locate the data in the grade
    worksheet.
    """
    print(f"Updating results worksheet with {name_value} results.")
    results_worksheet = SHEET.worksheet("results")
    results_worksheet.append_row(grade, table_range=f'B{number_name+1}')
    results_worksheet = SHEET.worksheet("results")
    results_worksheet.append_row(
        pass_result, table_range=f'C{number_name+1}'
    )
    print("Results worksheet updated successfully.\n")


def loop_data_input(
    quantity_questions_exam, quantity_of_students, ponderation_values
):
    """
    Loop function that asks the name of the student "i", asks for
    the points the student "i" scores per question. Updates the grade
    worksheet with the scores. Calculates the final grade for the student i.
    Check if the student "i" passes or not. Finally updates this information
    to the results worksheet.

    quantity_questions_exam: int that indicates the quantity of questions
    the user input that the exam has.
    quantity_of_students: int that indicates the quantity of student
    the user input that did the exam.
    ponderation_values:list with str that contains the ponderation of
    each question the exam has.
    """
    number_students = quantity_of_students

    for i in range(1, number_students + 1):

        student_name = []
        student_name.append(get_students_name(i))
        update_student_name(student_name)
        data_score_questions = get_questions_score(
            quantity_questions_exam, student_name
            )
        quantity_data = [int(num) for num in data_score_questions]
        quantity_pond = [int(num) for num in ponderation_values]
        update_questions_score_worksheet(quantity_data, i)

        grade = get_grade(quantity_data, quantity_pond, student_name)

        answer = get_pass_answer(grade)

        final_grade = []
        final_pass_answer = []
        final_grade.append(grade)
        final_pass_answer.append(answer)
        update_results_worksheet(
            final_grade, final_pass_answer, student_name, i
            )


def main():
    """
    Main function that calls all the other functions.
    """
    quantity_title = ["Number of Students", "Number of Questions"]
    grade_title = ["Student Name"]
    results_title = ["Student Name", "Final Grade", "Pass"]

    clean_worksheets("quantity", quantity_title)
    clean_worksheets("grade", grade_title)
    clean_worksheets("ponderation", None)
    clean_worksheets("results", results_title)
    print('Welcome to "Exam Results" project!\n')

    print(
        "This program calculates the final grade of an exam. "
        "First takes as input the quantity of students and questions of the "
        "exam. Second takes as input the percentage each question "
        "ponderates from the global grade. Then the program will ask for the "
        "first student name, later will ask for the score per question for "
        "that student. The program will continue asking for student's names "
        "and scores until the last student. For each student the program will "
        "calculate and show the final grade and if the student passes "
        "the exam.\n"
        "In this hypothetical program the grading works from 0 to 100 points. "
        "0 is the minimum score and 100 is the maximum score. "
        "To pass the student needs to have a score higher or equal to 60 "
        "points. For example, an exam has 2 questions. A random student gets "
        "30 points in the first question and 80 points in the second. "
        "The first question has a weight of 30% of the global grade and "
        "the second question has a weight of 70% of the global grade. "
        "The student global's grade would be 65 points. Pass.\n"
        "While the program runs it saves all the information in "
        "Google Spreadsheets.\n"
    )

    data_students_questions = get_quantity_students_questions_data()
    quantity_data = [int(num) for num in data_students_questions]
    update_data_quantity_worksheet(quantity_data)
    quantity_questions = quantity_data[1]
    quantity_students = quantity_data[0]
    grade_title = "(xpts)"
    grade_update = generate_grade_ponderation_title(quantity_data, grade_title)
    update_grade_ponderation_title(grade_update, "grade", "B1")
    ponderation_title = "(x%)"
    ponderation_update = generate_grade_ponderation_title(
        quantity_data, ponderation_title
        )
    update_grade_ponderation_title(ponderation_update, "ponderation", "A1")
    data_pond_questions = get_questions_ponderation(quantity_questions)
    quantity_ponderation = [int(num) for num in data_pond_questions]
    update_questions_ponderation_worksheet(quantity_ponderation)
    loop_data_input(quantity_questions, quantity_students, data_pond_questions)


main()
