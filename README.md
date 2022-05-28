# Exam Results

This program calculates the final grade of an exam. First takes as input the quantity of students and questions of the exam. Second takes as input the percentage each question ponderates from the global grade. Then the program will ask for the first student name, later will ask for the score per question for that student. The program will continue asking for students names and scores until the last student. For each student the program will calculate and show the final grade and if the student passes the exam.

In this hypothetical program the grading works from 0 to 100 points. 0 is the minumum score and 100 is the maximum score. To pass the student needs to have a score higher or equal to 60 points. For example, an exam has 2 questions. A random student gets 30 points in the first question and 80 points in the second. The first question has a weight of 30% of the global grade and the second question has a weight of 70% of the global grade. The student global's grade would be 65 points. Pass.

All the information is added to google spreadsheets. When the program is runned again, all the worksheets gets cleaned and inserted with titles... Ready for a new run. 

[Here is the live version of my project](https://project-3-exam-results.herokuapp.com/)

![Welcome image](/assets/readme-images/first_run.png)

## Features

### Existing Features

Responsive on all device sizes and has interactive elements.

- Welcome Message

    - Welcomes the user to the program "Exam Results".

![Welcome message](/assets/readme-images/welcome_message.png)
- Introduction

    - Explains what te program do.
    - Explains the inputs needed.
    - Explains the outputs of the program.
    - Gives an example of what to expect.
    - Let the user know that all the information is momentary saved in google spreadsheets while the program is running.

![Introduction](/assets/readme-images/introduction.png)
- First Input: Number of students and questions from the exam.

    - Ask the user to input the number of students that took the exam.
    - Ask the user to input the number of questions of the exam.
    - Explain how the input must be; 2 integers separated by comma.
    - Gives an example of how the input must me.
    - Shows the place for the input

![First Input: Number of students and questions from the exam](/assets/readme-images/first_input.png)
- Output from first Input.

    - For this scenario the input was: 2 students and 2 questions for the exam. 2,2
    - Output message for valid data.
    - Let the user know that the data is being updated in the Quantity, Grade and Ponderation worksheets.
    - Let the user know that the data was succsesfully updated to worksheets.
    - Program updates quantity worksheet with Number of Students:2 and Number of Questions:2.
    - Program updates grade worksheet with title for 2 questions: "Question 1 (xpts)" and "Question 2 (xpts)". In this worksheet there is also the title for Student Name because if will will up later with the different students names and scores of each one of them for each question of the exam.
    - Program updates ponderation worksheet with title for 2 questions: "Question 1 (%pts)" and "Question 2 (%pts)". The ponderation worksheet will not be updated with Student Name since this % per questions are the same for all the students.

![First Output: Valid data and data saved to worksheets](/assets/readme-images/first_output.png)
![Quantity worksheet updated](/assets/readme-images/quantity_updated.png)
![Grade worksheet updated](/assets/readme-images/grade_updated.png)
![Ponderation worksheet updated](/assets/readme-images/ponderation_updated.png)
- Second Input: % of ponderation of each question of the exam.

    - Ask the user to input the "%" of ponderation of each question of the total grade of the exam.
    - Ask the user to input the number of "%" depending on how much questions the user initialy input.
    - Explain how the input must be in this case 2 integers separated by comma. If the user input initialy 3 questions the program will ask the user to input 3 different "%".
    - Gives an example of how the input must me explaining an hipotetical case.
    - Each input must be between 1 and 99 %. A question can't have 0 % of value.
    - Shows the place for the input.
    - For all cases the add of all "%" as input must add 100%, for this case the 2 "%" must add 100%. 

![Second Input: % of each of the input questions from the exam](/assets/readme-images/second_input.png)
- Output from Second Input.

    - For this scenario the input was: percentage 1 = 40% and percentage 2 = 60% So: 40,60
    - Output message for valid data.
    - Let the user know that the data is being updated in the Ponderation worksheet.
    - Let the user know that the data was succsesfully updated to worksheet.
    - Program updates ponderation worksheet with "%" for 2 questions: "40" and "60". The ponderation worksheet will not be updated anymore.

![Second Output: Valid data and data saved to worksheets](/assets/readme-images/second_output.png)
![Ponderation worksheet updated](/assets/readme-images/ponderation_updated_2.png)
- Third Input: Name of first student.

    - Ask the user to input the name of the first student.
    - Ask the user to input the name of the student with just alphabetical characters. "space" is also allowed. User can enter only First name, Only Last name or both together.
    - Program is not affected by uppercase or lowercasse letters.
    - Shows the place for the input.
  
![Third Input: Name of first student](/assets/readme-images/third_input.png)
- Output from Third Input.

    - For this scenario the input was: Matias Castro
    - Output message for valid data.
    - Let the user know that the data is being updated in the grade and results worksheets.
    - Let the user know that the data was succsesfully updated to worksheets.

![Third Output: Valid student name and name saved to worksheets](/assets/readme-images/third_output.png)
![grade worksheet updated](/assets/readme-images/grade_updated_2.png)
![results worksheet updated](/assets/readme-images/results_updated.png)
- Fourth Input: Score for each question of first student.

    - Ask the user to input the score for each question of the exam.
    - Ask the user to input the number of "socres" depending on how much questions the user initialy input.
    - Explain how the input must be in this case 2 integers separated by comma. If the user input initialy 3 questions the program will ask the user to input 3 different socres.
    - Each score must be between 0 and 100.
    - Shows the place for the input.
  
![Fourth Input: Score for each question of first student.](/assets/readme-images/fourth_input.png)
- Output from Fourth Input.

    - For this scenario the input was: score 1 = 55 points and score 2 = 65 points. So: 55,65
    - Output message for valid data.
    - Let the user know that the data is being updated in the grade worksheet.
    - Let the user know that the data was succsesfully updated to the worksheet.
    - Output result for current student "Matias Castro". Final grade of 61 points and the student passes because the final score is equal or higher than 60 points.
    - Let the user know that the data is being updated in the results worksheet.
    - Let the user know that the data was succsesfully updated to worksheet.

![Fourth Output: Valid score per question, final grade, and pass result... Information saved to worksheets](/assets/readme-images/fourth_output.png)
![grade worksheet updated](/assets/readme-images/grade_updated_3.png)
![results worksheet updated](/assets/readme-images/results_updated_2.png)
- Loop Input

    - After grade and exam result for student one, the program will continue asking for all the students names and the scores they got in each one of the questions from the exam.

- Loop Output

    - As the program give the output of the final grade and pass result to the first student, will continue to give the final grade and pass result for each student.
    - Final grade rounded with round() function.

![Loop Input Output: repeat process of input and output for every student.](/assets/readme-images/loop.png)
![Final grade worksheet updated](/assets/readme-images/final_grade.png)
![Final results worksheet updated](/assets/readme-images/final_results.png)

- Runnning the program again

    - If the user decides to run the program again. At the start of it, the program will clear all the worksheets and add specific titles for each one of them.

![Cleaned quantity worksheet](/assets/readme-images/quantity_initial.png)
![Cleaned grade worksheet](/assets/readme-images/grade_initial.png)
![Cleaned ponderation worksheet](/assets/readme-images/ponderation_initial.png)
![Cleaned results worksheet](/assets/readme-images/results_initial.png)

## Features Left to Implement

- Allow the user to download the google spreadsheets with all the input and output information.
- Combine quantity and ponderation worksheets together.
- Combine grade and results worksheets together.
- Asking for only First and Last name option as student name, both with uppercase in the first letter.

## User Experience (UX)

### User stories as first time visitor goals

- As a First Time Visitor, I want to easily understand the main purpose of the program.
- As a First Time Visitor, I want to be able to navigate throughout the program in an easy way and be able to understand the content.
- As a First Time Visitor, I want to be able of getting information back from the program.

### Testing User Stories from User Experience (UX) Section

- As a First Time Visitor, I want to easily understand the main purpose of the program.

    - Users are greeted with a welcome message.
    - Users can have fast access to the instructions and purpous of the program.
    - Users are given example of what the program does.

- As a First Time Visitor, I want to be able to navigate throughout the program in an easy way and be able to understand the content.

    - The program is giving information and explaining what it expects as input from the user through the whole proccess.
    - The program is giving feedback continuesly through the program via Output for the user to understand what is happening and what comes next.

- As a First Time Visitor, I want to be able of getting information back from the program.

    - The program after every input from the user gives and output with preciss information for the user to keep a clear understand of what is happening.

## Testing

- pep8online.com

    - No errors were returned when passing through the official pep8online.com validator.

![PEP8 Validator](/assets/readme-images/pep8online.png)
- Correct input

    - In the Existing Features section, was shown how the program works and what to expect with correct input. Tested and every feature works properly. For terms of space this process will not be repeated since was already done.

- Incorrect Input for quantity of students and questions: 

    - Input: not integer, more or less than 2 inputs, less than 1 student or 1 questions including negatives.  

![Not integer error](/assets/readme-images/not_int_error_1.png)
![More or less than 2 inputs error](/assets/readme-images/not_2_input.png)
![Less than error](/assets/readme-images/less_than_1.png)

- Incorrect Input for % of each question of ponderation of total grade: 

    - Input: not integer, more or less inputs than quantity of question input, percentage higher than 100 or lower than 0, add of different % resulting different than 100%. 

![Not integer error](/assets/readme-images/ponderation_no_int.png)
![More or less inputs than quantity of question input](/assets/readme-images/ponderation_more_less_inputs.png)
![Percentage higher than 100 or lower than 0](/assets/readme-images/ponderation_outbounds.png)

### Different View by Device

- Web

![Introduction view web](/assets/readme-images/web.png)
- Ipad Air

![Introduction view ipad air](/assets/readme-images/ipad_air.png)
- Iphone 12 pro

![Introduction view iphone 12 pro](/assets/readme-images/iphone_12_pro.png)
### Bugs

- App wont work properly on smartphone.
- When user input a negative % with a positive % that adds on 100% for the ponderation input the data was shown as valid. Bug fixed, problem in code line 273 "quantity_ponderation_int = [int(x) for x in ponderation_values]". Used "()" instead of "[]", function was created instead of list. Bug fixed with the help of the mentor.
- Name of student can be first name, last name or both together, no uppercase or lowercase restriction included.
- No more Bugs.

## Deployment

- The site was deployed to heroku.com using Code Institue's mock terminal for Heroku.

    1. Each input in the run.py must end with "\n" so the input line for each input appears in heroku.
	2. All the dependencies instaled through the Code Institute template and both gspread and google-auth in Github must be instaled in heroku also for the program to work. For this in the terminal "pip3 freeze > requirements.txt" must be typed. Requirement.txt bus be correct spelled because heroku while loading the program will search for the dependencies in this folder to install them and then after allowing the code to run.
	3. Git add . command plus git commit -m "Add requirements for deployment." and git push comands must be input to the terminal.
	4. Create account in heroku.com
	5. Input name, last name, email address, student role, country in this case Sweden and Python as primary development language. Finally reCAPTCHA and create account.
	6. Confirm account in email.
	7. Create password and Login.
	8. Accepts terms and services.
	9. Create first app from heroku dashboard.
	10. Select unique name for the app and region, in this case "Europe".
	11. App created.
	12. Go to Settings tab.
	13. Go to Config Vars.
	14. Add 2: first one Key = CREDS and value will be all the information inside the file creds.json that includes de private data saved in .gitignore. Second one Key = PORT, value = 8000. This one to improve compatibility with various Python Libraries.
	15. Add dependencies needed directly fro heroku directly from "Add buildpack".
	16. First one needed is Python.
	17. Second one needed is "nodejs", handles the mock terminal code provided.
	18. Python buildpack must be first in order in the list, second nodejs.
	19. In github terminal command: heroku login -i
	20. Command: email and password.
	21. Command: heroku apps.
	22. Command: heroku git:remote - project-3-exam-results
	23. Command: git add . && git commit -m "Deploy to heroku via CLI".
	24. Command: git push origin main
    25. Command: git push heroku main

## Credits

- All code was done by the student with the support of Code Institute classes, love-sandwiches project and his mentor. 

- All Media content was done and uploaded by the student.

- Code Institue and heroku for deployment terminal.

