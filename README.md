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
- Home Page

    - Includes a professional photo of MaTT.
    - Includes a short phrase about music.
    - This will guide the user to a first approximation and introduction of what MaTT has to offer as a DJ.

![Home](/assets/readme-images/home.png)
- Bio

    - Includes nationality and residence of MaTT.
    - Gives a brief description of the journey of MaTT as a DJ.
    - Gives an explanation of what makes MaTT a special DJ, what kind of playing style he offers and what he is looking forward to attempting inside the music industry.

![Bio](/assets/readme-images/bio.png)
- Media

    - This section works as an audiovisual portfolio that allows the user to listen and watch different music sets from MaTT.
    - The media shown in this section also works as a link to the music social-media of MaTT, Soundcloud and Youtube.
    - Finally the user will actually listen and watch what Matt was expressing with words in the Bio, in case of liking it the user will be able to go to the different social-media or contact him directly in the form from the next section.

![Media Soundcloud](/assets/readme-images/media_1.png)
![Media Youtube](/assets/readme-images/media_2.png)
- Contact

    - This section works as a tool for connecting the user directly with MaTT.
    - Requires Full Name, Email and Comments/Ideas to be able to push forward the information to MaTT.
    - An image of a Pioneer XDJ-RX3 is shown at the end of the page as a hint of what MaTT likes/uses to play. Also used to give positive visual feedback for the user.

![Contact](/assets/readme-images/contact.png)
- Footer 

    - The Footer includes 3 icons with a direct link to MaTT social-media. Soundcloud, Youtube and Instagram. Links will open in a new tab.
    - This section works as a tool for connecting the user directly with MaTT through Soundcloud, Youtube or Instagram.
    - The footer is fixed to the page as the user scrolls, this will help the user in any moment of decision of contact or follow to be there as a direct access.

![Footer](/assets/readme-images/footer.png)
## Features Left to Implement

- Allow the user to download the google spreadsheets with all the input and output information.

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
- No more Bugs.

## Deployment

- The site was deployed to heroku.com using Code Institue's mock terminal for Heroku.

    1.  Each input in the run.py must end with "\n" so the input line for each input appears in heroku.
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

