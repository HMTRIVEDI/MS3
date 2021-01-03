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

7. Click the settings tab and then click the Reveal Confid Vars button and add the following:

 key: IP, value: 0.0.0.0
 key: PORT, value: 5000
 key: MONGO_DBNAME, value: (database name you want to connect to)
 key: MONGO_URI, value: (mongo uri - This can be found in MongoDB by going to clusters > connect > connect to your application and substituting the password and dbname that you set up in the link).
 key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).
 Enable automatic deployment:

8. Click the Deploy tab
 In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

---

## Credits

### Content

### Media

### Acknowledgements

---
