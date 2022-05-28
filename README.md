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
![grade worksheet updated](/assets/readme-images/grade_updated_2.png)
![results worksheet updated](/assets/readme-images/results_updated.png)



## Features Left to Implement

- Allow the user to download the google spreadsheets with all the input and output information.
- Combine quantity and ponderation worksheets together.
- Combine grade and results worksheets together.
- Asking for only First and Last name option as student name, both with uppercase in the first letter.

## User Experience (UX)

### User stories as first time visitor goals

- As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the Artist.
- As a First Time Visitor, I want to be able to navigate throughout the site in an easy way and be able to understand the content.
- As a First Time Visitor, I want to look for testimonials from the Artist to learn more about him and the intentions with the webpage. I also want to locate their social media links to see their followings on social media to determine how trusted and known they are.

### Testing User Stories from User Experience (UX) Section

- As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the Artist.

    - Users are greeted with an image of the Artist plus a phrase from him.
    - Thanks to the Bio and Media sections the user can learn more from the life of the Artist and also listen/watch some of his work as a DJ. Both of this helps to understand the value of the Artist and his intentions with the webpage.
    - Thanks to the contact form and the footer the users are able to either get to know more about the Artist or contact him directly.

- As a First Time Visitor, I want to be able to navigate throughout the site in an easy way and be able to understand the content.

    - The header and the footer will give company to the users while they navigate the whole site, giving them easy access to it and also to get to know more about the Artist or directly contact him.
    - The content itself of the site is self-explanatory, user-friendly.

- As a First Time Visitor, I want to look for testimonials from the Artist to learn more about him and the intentions with the webpage. I also want to locate their social media links to see their followings on social media to determine how trusted and known they are.

    - The Bio gives initial information about the artist.
    - The site gives the opportunity to get to know the artist and the followers thanks to direct links to his social-media accounts.

## Testing

- pep8online.com

    - No errors were returned when passing through the official pep8online.com validator.

![PEP8 Validator](/assets/readme-images/pep8online.png)
- CSS

    - No errors were returned when passing through the official W3C validator.

![CSS Validator](/assets/readme-images/css_validator.png)
- Web Developer Tool -  Lighthouse 

    - 94% Accessibility.

![Accessibility Lighthouse](/assets/readme-images/lighthouse.png)
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
- Name of student can only contain alphabetic charaters. This means that no "space" allowed. So the program only accepts first name or last name.
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

