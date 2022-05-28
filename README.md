# Exam Results

This program calculates the final grade of an exam. First takes as input the quantity of students and questions of the exam. Second takes as input the percentage each question ponderates from the global grade. Then the program will ask for the first student name, later will ask for the score per question for that student. The program will continue asking for students names and scores until the last student. For each student the program will calculate and show the final grade and if the student passes the exam.

In this hypothetical program the grading works from 0 to 100 points. 0 is the minumum score and 100 is the maximum score. To pass the student needs to have a score higher or equal to 60 points. For example, an exam has 2 questions. A random student gets 30 points in the first question and 80 points in the second. The first question has a weight of 30% of the global grade and the second question has a weight of 70% of the global grade. The student global's grade would be 65 points. Pass.

All the information is added to google spreadsheets. When the program is runned again, all the worksheets gets cleaned and inserted with titles... Ready for a new run. 

[Here is the live version of my project](https://project-3-exam-results.herokuapp.com/)

## Features

### Existing Features

Responsive on all device sizes and has interactive elements.

- Navigation Bar

    - Includes links to the logo "MaTT", Home page, Bio, Media and Contact. The Navigation Bar is fixed to the top so the user will be able to access it the whole time.
    - Will allow the user to travel through the different sections of the page without the need of scrolling.

![Navigation Bar](/assets/readme-images/logo_menu.png)
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

- Creating a Gallery with images of MaTT.

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

- HTML

    - No errors were returned when passing through the official W3C validator.

![HTML Validator](/assets/readme-images/html_validator.png)
- CSS

    - No errors were returned when passing through the official W3C validator.

![CSS Validator](/assets/readme-images/css_validator.png)
- Web Developer Tool -  Lighthouse 

    - 94% Accessibility.

![Accessibility Lighthouse](/assets/readme-images/lighthouse.png)
### Different View by Device

- Web

![Bio](/assets/readme-images/bio.png)
- Ipad Air

![Bio](/assets/readme-images/ipadair.png)
- Iphone 12 max

![Bio](/assets/readme-images/iphone12pro_bio.png)
### Unfixed Bugs

- YouTube video wont play on smartphone.
- Form returns "this form is not secure autofill has been turned off" since it action attribute is "mailto" and not an "https//:" secure server.

## Deployment

- The site was deployed to GitHub pages.

    - In the GitHub repository, navigate to the Settings tab.
    - From the source section drop-down menu, select the Master Branch.
    - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - https://matiasconsiglio.github.io/Matt/

## Credits

- All code was done by the student with the support of Code Institute classes and his mentor. 

- All Media content was done and uploaded by the student.

- Music used to make the sets and audio for video from media where bought in different pages like "www.beatport.com" or apple music.

- Principal image was taken by Futuro Berg, a professional photographer.

- Pioneer XDJ-RX3 Photo used at the end of the site was obtained from www.pioneerdj.com 
