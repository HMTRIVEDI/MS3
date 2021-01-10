# Movimento

---

#### Movimento provide information to the user about the most amazing and desirable places to visit around the world. it's explorer campanion.

![GitHub Logo](/assets/Multi-Device-Website-Mockup-Generator.png)
---

## UX

---

#### when we travel we always wonder what we go for as world is fulll of amazing places divided in diffrent borders. but no worries movement is there for you

### user story

- User want to find a good local place to visit.
- User want to signup.
- User want to login.
- User wnat to see profile.
- User want to see diffrent list of place.
- User want to see more info about the location.
- User want to provide information of the location 
- User want to edit the information.
- User want to edit the information.
- User want to delete the information.
- Guest user want to contact us.

### Current Features

- user can signup on website.
- user can login on website.
- user can logout from page.
- user can see the list of location 
- user can delete and update the location details.
- usre can see more details about the location info.

### Features yet to devlop

- User can edit user profile.
- Event page where user can see diffrent local event happning around as per his current position.
- User can add events and loaction to visit in it's bucket list.
- user can short the location as per the diffrent filters like country,     distance from current position, cetegory of loaction
- reviews & rating  by diffrent users about loaction

---

## wireframes
  - in devlopment stage few things and design has been changed and some features has been removed due to time limit and will be devloped in next version
   
![GitHub Logo](/assets/wirefram/MS3-page-001.jpg)
![GitHub Logo](/assets/wirefram/MS3-page-002.jpg)
![GitHub Logo](/assets/wirefram/MS3-page-003.jpg)
![GitHub Logo](/assets/wirefram/MS3-page-004.jpg)
![GitHub Logo](/assets/wirefram/MS3-page-005.jpg)
![GitHub Logo](/assets/wirefram/MS3-page-006.jpg)

## Technologies Used

- HTML
  - This project uses HTML as the main language used to complete the structure of the Website.
- CSS
  - This project uses custom written CSS to style the Website.
- JavaScript
  - JavaScript is used along with emailjs for the contact form. This sends an   email to the owner on form submit.
- Python
  - project main focused on using Python, the back-end logic.
- MongoDB
  - MongoDB was used to create the document based databases(collections) used as data storage for this project.
- Bootstrap 
  - Bootstrap was used through the website for layout and responsiveness.
- Bootstrap- template
  - Free Bootstrap template used for creating base of the website.
- Google Fonts
  - Google fonts are used throughout the project to import the Inter and Bevan fonts.
- GitHub
  - GithHub is the hosting site used to store the source code for the Website.
- Git
  - Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.
- Heroku
  - Heroku was used to deploy the live website.
- Google Chrome Developer Tools
  - For debugging and testing google chrome Developer tools used.
- balsamiq Wireframes
  - Balsamiq used for wireframes
- freelogdesign
  - Free logo design was used in order to create the website logo.
- Font Awesome
  - All icone are used from font Awesome
- Favicon
  - Favicon.io was used to make the site favicon
- Techsini
  - Website Mockup Generator was used to create the Mock up image in this README

---
## Testing
---
### Automated testing
---
- HTML pages has been tested using w3c validator
  - found 10 error in html templates has been solved by taking all corrective   mesuures errors and solved status can me found in **test.md** file
- Pythone code has been tested using pip8online
No error found result can be seen in **test.md** file

---
### Manual Testing
---
---
#### CRUD testing
---
- Data Input:
  tested that whenever user input data in amy form ( user signup,give Location information, update location information) does it get response from the mongodb 

  Status: Active

- Data display:
  tested that whenever user select a option to see perticular data does it get responce from mongodb 
    - Profile : on click on profile user must be able to see the profile infomation provided at time of signup.
    - Place: on click user must be able to see the location and information about it if data is there.

    status: Active

- Data delete: tested whene user want to delete a data which input by him 
   
   status: Active
---
#### Responsivness
---
  - website has been tested on many hardware laptop, phone, desktop and looks perfactly fine on all screen size
  - test result can be seen on **test.md**
---
### website features Testing 
---

1. User story first impration of website:
  on accesing the website user must be able to see the following links home,free signup, Login email form for sending the infomration to the website owner. and on the image name of the website " Movimento" below it the info about the website.

2. User story Signup: 
  - website have exclusive information so user need to signup.
  - on click on signup user must me able to see signup page and after feeling the form page must me redirect to home page.

3. User Story Signup form: 
  - filds with * are mandatory so if user escape those , form can not be accepted.

4. User Login: 
  - on click on login button model will popup and ask user to provide username and pasword and if password username are correct it will redirect user to home page and there will be massage says " welcome to movimento a travelat's guide ", if password or username is incorrect it will redirect respactive page.

  - After login user can see hidden navigation links " place, profile"

5. User want more info about location: on click on info button user can find more info about the given location

6. User want to give information regarding new location: user can fillup the form given at bottom of the place page and then submit it will redirect to place page and user can see the location has been updated in database.

7. user want to edit the location page: if user want to edit infomation he given it can be done by clicking on edit button.
 - on click updateplace page popup and by filling the page and clicking on submit button user can update all details and if click cancel it will redirect it to the place page without changing anything.

8. user want to delete the location: if location updated by user he only can delete it by clicking on delete button.


## Deployment

---
### Project Creation
---
 
 To create this project I used the CI Gitpod Full Template by navigating here and clicking the 'Use this template' button.

 I was then directed to the create new repository from template page and entered in my desired repo name, then clicked Create repository from template button.

 Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

 The following commands were used for version control throughout the project:

 git add filename - This command was used to add files to the staging area before committing.

 git commit -m "commit message explaining the updates" - This command was used to to commit changes to the local repository.

 git push - This command is used to push all committed changes to the GitHub repository.

---
### Deployment to Heroku
---
#### Create application:
---
1. Navigate to Heroku.com and login.
2. Click on the new button.
3. Select create new app.
4.  Enter the app name.
5.  Select region.
6.  Set up connection to Github Repository:

 Click the deploy tab and select GitHub - Connect to GitHub.
 A prompt to find a github repository to connect to will then be displayed.
 Enter the repository name for the project and click search.
 Once the repo has been found, click the connect button.
 Set environment variables:

7. Click the settings tab and then click the Reveal Confid Vars button and add  the following:

 - key: IP, value: 0.0.0.0
 - key: PORT, value: 5000
 - key: MONGO_DBNAME, value: (database name you want to connect to)
 - key: MONGO_URI, value: (mongo uri - This can be found in MongoDB by going to 
 - key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).
 Enable automatic deployment:

8. Click the Deploy tab
 - In the Automatic deploys section, choose the branch you want to deploy from  then click Enable Automation Deploys.

---

## Credits
- All data used on project are used only for educational purposes and collected from multiple resources will be given cretits as and when gethered more information 
### Content
All content for the location info has been collected from Wikipedia and diffrent location info website. for future whenever new location will be added Movimento does not claim any right or responsiblity on those information 
### Media
All Media for the website has been collected from diffrent websites and used as URL to display those info, and furthere whenver new location will be added Movimento does not claim any right or responsiblity on those media.

### Acknowledgements
- Rahul Patil
- https://www.w3schools.com/
- Slack Community
- tutor support
- https://startbootstrap.com/(for website base templete)
