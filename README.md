heroku
postgreSQL
cloudinary
udemy
pexels
google fonts - Lilita One (TITLE) and PT Sans Narrow (Body)
Font Awesome
Bootstrap
Django All Auto


using CI Django Blog walkthrough to help build inital restaurant blog.
Harvester menu
django documentation
https://www.youtube.com/watch?v=EX6Tt-ZW0so




# Arthur &amp; Alfie's Restaurant

Arthur %amp; Alfie's is website built to showcase their restaurant, allowing a wider target audience to discover whats on offer. There is a page showcasing their menu and lastest blog articles. Furthermore users can register up to the site and log in to their account allowing them to 'like' blogs by the restaurant, providing the owners with subtle feedback on which blogs are the most popular. Users can book a table reservation and even sign up to their newsletter email subscription. Whilst signed in, the user is able to see their future table booking and has the functionality to edit, cancel or add.

This is a full-stack project built using Python + Django, HTML, CSS and JavaScript and is for educational purposes. 

![Responsive Mockup](#)

## Showcase

A deployed link to the website can be found [here](#)

## User Experience (UX)

 ### User Stories

  #### First Time Visitor Goals
   1. As a first time visitor I want to understand what the site is about and who the site is intended for. Starting with the title and core content of the index page, these elements should give a clear idea.
   2. As a first time visitor I want to be able to clearly navigate around the site knowing which page I am on and what information I should expect to find.
   3. As a first time visitor the flow of each page should read top to bottom with the interactive content following suit. The home / index page should then allow the user to flow onto the next relevant page.
   4. As a first time visitor I want the content to be in a consistant and simple structure from page to page. Navigation bar at the top, main body of the page and footer at the bottom.
   5. As a first time visitor the interactive content should be intuitive and not require content heavy text to explain how to use.
   6. As a first time visitor I want to see specific restaurant content like opening times, directions, the menu, blog and to book a table.
   7. As a first time visitor I do not want to necessarily register as a user to book a table, nor restrict me from signing up to the newsletter or read the blogs.
   8. As a first time visitor I have the option to register and sign up to an account which gives me access to further functionality such as manage bookings or like blogs.
  
  #### Returning Visitor Goals
   1. As a returning visitor I want to know the benefits of registering as a user and then easily see if I am logged in or not. 
   2. As a returning visitor I want to be able to locate the social media links in order to gain further insight and information but delivered through the different platforms: Youtube, Instagram, Facebook and Twitter.
   3. As a returning visitor I want to be able to sign up to the newsletter subscription and received email confirmation confirming that I am signed up.
   4. As a returning visitor having an account I want to be able to book a table reservation but then be able to edit, delete or add bookings to my account and see their status. 
   5. As a returning visitor having an account I want to be able to like the blog posts as I normally would with any other social media blog site.
  
  #### Frequent User Goals
   1. As a frequent user when I return to the site I want to remain logged in to my account so I can quickly navigate to 'my bookings' page enabling a quick view and access to the bookings functionality.
   2. As a frequent user I will be reading more content onsite therefore want the blogs to be clicked into to open up the content to read and on the menu page, to click into the meals to read specfic information on each meal.
   3. As a frequent user I want my blog likes to remain at the status I left them last time I was on the site.
   4. As a frequent user I want the restaurant to update the menu meals regularly to keep me interested along with the blog posts so I know the latest news.
   5. As a frequent user as I interact with the sites content I want messages to appear on the page informing me if I have submitted or actioned any details.
  
  #### Admin User Goals
   1. As an admin user I can log in allowing access to the websites backend database.
   2. As an admin user I can view the table bookings made and either approve or delete the booking. 
   3. As an admin user I can view the users who have signed up the the newsletter and/or registered an account.
   4. As an admin user I can add, edit or delete meals from the menu and also add, edit and delete meal categories.
   5. As an admin user I can add, edit or delete blogs. I also have the option to leave as a draft or post to go live on the frontend.
   6. As an admin user I can add, edit or delete different table configurations for the restaurant allowing users to select the correct table.

## Design

 ### Key User Features
  - Responsive site adapting to the screen size with the content not affected.
  - An index page providing the first time users with all the key information needed to know what the site is about.
  - Restaurant menu page outlining the meal choices avaialble with further links to the specific meal page providing more information.
  - Bookings page for all users (signed up or not) to send a table reservation request.
  - Newsletter page for all users to sign up to the restaurants newsletter email subscription.
  - Blog page for users to see the latest blog news sent out by the restaurant.
  - My Bookings page (only for users signed into their account) allowing users to book, edit or cancel table reservations.
  - Registration and Log In/Out page for users to sign up or log in to an account. 
  - Links to external social media pages in the footer so site visitors can navigate (on a different tab) to further restaurant content. 
 
 ### Structure
  - The site is made up of an initial home page, menu page, book now page, newsletter page, blog page, register page, log in page and my bookings page for logged in users.
  - Each page only has the relevant content expected in order to keep the site simple to understand. Every page is in a consistant style, format and layout aiding usability.
  - Bootstrap grid layout system has been used to create a responsive site.
    1. Navigation bar at the top with page title to the left and page links to the right.
    2. Rotational uber image under the navigation bar for inspiriation and reaffirming to the user it is a restaurant site.
    3. Title of the page and paragraph of text advising the user of the page and its use.
    4. Core content of the page.
    3. Social media footer at the bottom.
    4. Consistant colour scheme throughout each page specifically on the header / nav bar, page link buttons and footer.
 
 ### Colour Scheme
  - Colour scheme of the site designed using: https://coolors.co/
  - The header and nav bar are made up using the leading colour of the site, that being Oxford Blue. Dark Sienna drives the visual presence of the icons onsite, with headings complimented in Charcoal. Both Cadet Blue Crayola and Papaya Whip are supporting colours used sparingly in the lower levels such as blog details.
  - The button colours led by Bootstraps classes with Secondary a leading complimentary choice. Danger colour has been used appropriately with the cancelling of reservation button, likewise 'update reservation' in their Info class colour.
  - Each clickable button or heading link with have hover effects be it underline on heading links or coloour change on buttons. This reinforces the clickable element.
  ![Site Colour Scheme](#)
 
 ### Typography
  - Google Fonts has been used to stylise the text on site with headings and paragraphs complementing each other. Both modern styles with the headings eye catching and paragrpahs content clear to read on smaller screens.
  - The [Lilita One](https://fonts.google.com/specimen/Lilita+One?preview.size=61&thickness=8&query=Lilita+One) font is used for the headings throughout the site with Cursive as the fallback.
  - The [PT Sans Narrow](https://fonts.google.com/specimen/PT+Sans+Narrow?preview.size=61&query=pt+sans) font is used for the content paragraphs of the site with Sans-Serif as the fallback.
 
 ### Imagery
  - Underneath the navigation bar, there is a Bootstrap carousel which rotates through three images. These are focused on served food within a restaurant sitting and provide a visual representation of the website. This is stored in the local, static > images, folder.
  - Each menu item is supported with a visual image of the dish supporting user experience. This is stored in the Cloudinary database.
  - Each blog post has a relevant supporting image with ties into the content of the blog. This is stored in the Cloudinary database.
  - Icons feature heavily in the additional 'detail led' card navigation section on the landing page. Again, rather than text heavily and users having to read the information, these icons give an indication of what the heading link, links to. Icons have been sourced from fontawesome.

 ### Admin Database
  - The backend admin database has been created with the restaurants needs at the forefront. Within the project there are four main apps which have been created individually for simplicity and to separate out the tasks and the storing of data.
  - Blog database: to store 'draft' and 'posted' blogs created by the restaurant. Functionality allows to store unfinished blogs, post blogs, delete and update blogs. Also gives customers the option to like each blog.
  - Bookings database: There are two models, one for the restaurant table size choices, the owner can edit, add and delete table sizes to suit whats available and thus allowing customers to book the right table size. The other model for bookings. This is where the admin staff can see the bookings submitted via the form. On here they have the functionality to change the status of the booking to 'confirmed' in order to provide feedback to the customer. The admin staff can also access the customers details if needed to reach out directly to the user who booked the table.
  - Menu database: Two models, one for meal categories for the admin staff to assign categories to meals i.e starter, main or dessert. The option to add categories, amend or delete. Changes here are directly portrayed on the frontend. The second model for adding meals to the menu. The admin staff can publish the meal or leave as draft, whichever is needed. All relevant meal details found here e.g. price, vegetarian option, meal image, which again will directly show on the sites frontend when published. 
  - Newsletter database: The model stores all customers who sign up to the newsletter subscription. Admin staff can view customer name and email data if needed.
  ![Model Data Relational Diagram](#)

## Wireframe
 - [Desktop Wireframe](#)
 - [Tablet Wireframe](#)
 - [Mobile Wireframe](#)

## Current Features

 ### Navigation Bar
 - A responsive navigation bar featured on all pages of the site.
 - This section allows the user to easily navigate from page to page without having to use the back button or relooping back to the homepage.
 
 ![Nav Bar](#)
 
 ### Carousel and Opening Paragraph
 - A 

 ![Opening Content](#)

 ### Detail Navigation
 - A 

 ![Detail Nav](#)

 ### Latest News
 - A 

 ![Latest News](#)

 ### Opening Hours and Directions
 - A 

 ![Hours and Directions](#)
 
 ### The Footer
 - The footer section houses icons of the relevant social media platforms available which allows the user to click on, thus directing them to the relevant social page. The link will open up in a new tab as it gives the user the option to remain on the current page or click onto the social media tab that has just opened.
 - The footer encourages the user to keep connected via social media. It also gives the user confidence of the business / brand given the multiple social plaforms used.
 - The footer is responsive and featured at the bottom on all four pages. The footer is identical on each page to provide a consistent look and ease of navigation.

 ![Footer](#)
 
 ### Menu Page
 - A 

 ![Menu](#)

 ### Book Now Page
 - A 

 ![Book Now](#)

 ### Newsletter Page
 - A 

 ![Newsletter](#)

 ### Blog Page
 - A 

 ![Blog](#)

 ### Register, Log In / Out Pages
 - A 

 ![Register and Log In / Out](#)

 ### My Bookings Page
 - A 

 ![Bookings](#)
 
 ### Responsive Site
 - The site is responsive across various screen sizes from desktop, tablet and through to mobile. The user needs to be able to easily read, navigate and interact with the content across various devices.
 - Specific screen break points are: iphone 5 up to ipad (320px - 767px), ipad up to ipad Pro (768px - 1023px), ipad Pro to desktop (1024px +).
 - The use of Flexbox CSS helped create a responsive site.
 ### Accessibility
 - All images have an alt attribute taking into account users who are visually impaired. The site has contrasting background colours to text enabling an easy read. Background button colours have been set to match the relevant pages defined colour. Semantic HTML has been used to support machines to understand the layout of the site. All links have hover over effect.
 
## Features Left to Implement
 - Stars achieved from the reward chart tasks are to be represented on the games page. If the user succeeds in acheiving more stars from playing the game then the reward chart stars and the game stars are to be totalled together.
 - The totalled stars to be represented on the 'My Reward' page. From this total, once a reward is claimed, the cost of the reward is to be deducted from the total stars. This will bring together the links between the chart page, game page and reward page.
 - On the reward chart, to include a delete button removing a single task.

## Technologies Used

 ### Languages Used
  - [HTML](https://en.wikipedia.org/wiki/HTML5)
  - [CSS](https://en.wikipedia.org/wiki/CSS)
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
 ### Frameworks, Libraries & Programs Used
  - Balsamiq: used to create the wireframe during the design process.
  - Gitpod: used for writing the code and using the command line to commit and push to GitHub.
  - Git: used for version control through the gitpod terminal to commit to Git and push to GitHub.
  - GitHub: used to store the projects code after being pushed from Git. Used to host repository.
  - Hover.css: used for the links in the nav bar to underline, bold and turn background colour a lighter green. Used to reverse the background colour, font colour and bold the text in the buttons. The curser turns to a hand icon when hovered over link / clickable button.
  - Google Fonts: used to import the 'Bree Serif' font with 'Serif' as the fallback font for the headings and 'Open Sans' font with 'Sans-Serif' as the fallback font for the content of the site.
  - Font Awesome: used for icons in the header, footer and icons within the content of the site for aesthetic and UX purposes.
  - Favicon.io: used to generate the favicon icon of the site.

## Testing
 - I tested the sites interactive content to make sure the functionality worked as intended. In summary:
   - the reward input allowed the typed task to be added to the table with either an enter press or click on 'add' button. 
   - the stars in the chart are clickable to remove the opacity. 
   - the stars achieved counter totals the number of clicked stars.
   - the content of the table remains even when the browser is refreshed or the user comes back to the site.
   - the end of the week reset button removes the chart tables content.
   - playing the game delivers the expected result and are correct.
   - the game score counter tallys correctly and the stars earned counter calculates correctly.
   - the game instructions alert box appears when clicked on.
   - the 'claim reward' buttons bring up an expected alert when clicked on.
   - the feedback form submits correctly with the 'required' propoerty used where needed.
   - all the links work i.e. nav links take the user to the correct page, header logo clicks back through to the home page, footer social media icons open up the site in a new tab.
   - the link hovers work as intended and show the correct styling when cursor over.
   - the pages are responsive and look as intended based on the screen size, with mobile, tablet and desktop the main breakpoints.
   - I asked three family members to test out the site too by sending them the url link and provide honest feedback where possible.
 ### Google Inspect
  - I coded the site using mobile first design. Constantly using Google Inspect in the devtools to check my layout, make amendments, re-check and therefore delivering an end result that fits the brief and user goals. 
 ### Validator Testing
  #### HTML - 
   - All HTML validation was passed through the official W3C validator.
   - index.html returned with two errors, I had duplicated id="star" more than once for the repeat of the star icons in the table. Corrected to number the star ids element. On line 158, I did not include a space between href and class tags, corrected.
   ![Home Page Validator Results](https://github.com/Oliver-RC/reward-chart/blob/main/readme-content/index-validator.JPG)
   - game.html had one error on line 108 whereby I did not include a space between href and class tags, corrected.
   ![Game Page Validator Results](https://github.com/Oliver-RC/reward-chart/blob/main/readme-content/game-validator.JPG)
   - reward.html returned no errors.
   ![Reward Page Validator Results](https://github.com/Oliver-RC/reward-chart/blob/main/readme-content/reward-validator.JPG)
   - feedback.html had two errors on line 60 and 63 whereby I did not include a space between placeholder and required tags, both corrected.
   ![Feedback Page Validator Results](https://github.com/Oliver-RC/reward-chart/blob/main/readme-content/feedback-validator.JPG)
  #### CSS - 
   - No errors were found when passing through the official (Jigsaw) validator.
   ![CSS Validator Results](https://github.com/Oliver-RC/reward-chart/blob/main/readme-content/css-validator.JPG)
   - Two warnings were displayed, one due to using external style sheet for Google Fonts, one for an unknown vendor extension which I have created to help with the background colour maintenance of the site.
   ![CSS Validator Warnings](https://github.com/Oliver-RC/reward-chart/blob/main/readme-content/css-warning-validator.JPG)
  #### JavaScript - 
   - JS Hint Checker was used to highlight any functional errors, none returned. The only warning was regarding semicolons being missing on selected lines. Upon research, this is optional. Nevertheless I felt best practice to use semicolons so corrected both script.js and gsame.js files.
 ### Performance Testing
  - Tested the site on Google Developer Tools Lighthouse for desktop and mobile with good results on both. Performance, accessibility and SEO scored top marks. Best practices at 87 due to browser 404 errors but nothing of concern which impacts the site useability and performance.
  ![Lighthouse Results Desktop](https://github.com/Oliver-RC/reward-chart/blob/main/readme-content/accessibility-desktop.JPG)
  ![Lighthouse Results Mobile](https://github.com/Oliver-RC/reward-chart/blob/main/readme-content/accessibility-mobile.JPG)
  - Tested on [Wave](https://wave.webaim.org/) which helped me with accessibility, making sure my layout and design worked well with screen readers.
 ### User Stories Testing
  - First time user once on the site is able to understand the reasoning  of the site by the site heading but also the following content of the first page with clear section titles. The page reads from top to bottom with the task section and reward chart being the main content. Page links towards the bottom aid the journey of the user onto the next pages.
  - Returning user is able to interact with the site as intended with the reward table tasks saved to local storage. The game page restarting when returning and the footer icon links enabling the user to search for further content offsite.
  - Frequent user is able to reset the saved tasks and start afresh by clicking on the end of week reset button. The site is clearly structured and encompasses all the required elements to treat the site as the main reward system for the parent / carer. 
  ### Further Testing
  - Site tested on Google Chrome, Microsoft Edge, Firefox and Safari across the responsive page break points with CSS Flexbox working as intended on each page.
  - The site tested on the above browsers but also using the browsers on different operating systems, Microsoft and Apple. This was to check for all links, site elements, screen layout and functionality working as intended. 
  - The site was also tested on mobile, both Samsung Note 10 and iphone 10. Again using Google Chrome on both devices, Safari on Apple and Samsung Internet Browser.
  - All links on the site tested and directed to the correct page.
  ### Bugs
  - The reward chart table width when applying margins left and right would cause the table to overflow the page. Corrected by setting the width to 100%.
  - Issues with the footer not remaining at the bottom of the index and feedback page as the content of the body was not long enough. Resolved by extending the margin on the elements above to push footer to the bottom. Position absolute would cause the footer to sit ontop of the above elements and position fixed would also stick the footer above elements on the page.

## Deployment

 ### Hosting
  - The site was deployed to GitHub Pages using the following steps:
   - Log in to GitHub and locate my repository: Oliver-RC / collection-of-crafts.
   - Locate the 'Settings' link in the navigation bar an click into.
   - Find the 'Pages' section within Settings and click into. 
   - Under 'source', click on 'none' and a dropdown will apear, click on 'main' and save.
   - The page will refresh (it may take a while to update) and there will be a link stating: 'Your site is published at'.
   - Click on the link to open the site.
 ### Cloning
  - To make a local Clone:
   - Log into GitHub or creat an account and navigate to the gitpod repository [here](https://github.com/Oliver-RC/reward-chart).
   - Under the repository name, above the list of files, click on a button called 'Clone'.
   - If cloning with HTTPS, make sure HTTPS is underlined and then click on the clipboard icon to copy. Once clicked the icon will turn to a tick.
   - Open your local IDE open the terminal.
   - Change the current working directory to the location where you want the cloned directory to be.
   - Type git clone, and then paste the URL you copied earlier.
   - Press enter to create your local clone.
 ### Updates and Push to Hosting
   - Any updates to the code will need to be commited and pushed to the master branch. This will automatically update the hosted site.

## Credits

 ### Content
  - The inspiration for the interactive reward chart was gained from Web Dev Simplified - How to Code A Better To-Do List - Tutorial [YouTube](https://www.youtube.com/watch?v=W7FaYfuwu70&t=517s). I was able to understand Javascript that bit more and learn from the content whilst adapting it to my interactive reward chart.
  - For the star game, I took ideas from many rock, paper, scissors javascript code, however Code with Ania Kubow - 3 ways to code Rock Paper Scissors in JavaScript (Beginner to Intermediate to Advanced!) [YouTube](https://www.youtube.com/watch?v=RwFeg0cEZvQ) was credited with my key learning.
  - I wanted my nav bar to be responsive using Javascript therefore used Web Dev Simplified - Responsive Navbar Tutorial [YouTube](https://www.youtube.com/watch?v=At4B7A4GOPg) for further insight on how to action.
  - The reward chart needed to be responsive on mobile and display content suited to the screen size. I used IB-Media - Making a Responsive Table Using HTML & CSS [YouTube](https://www.youtube.com/watch?v=QjW5TsNquH8) for inspiration and learning.
  - Within my reward table I wanted clickable star icons using checkboxes, for this I took learning from [CSS-Tricks](https://css-tricks.com/the-checkbox-hack/)
 ### Media
  - The Favicon was created from Favicon.io [here](https://favicon.io/favicon-generator/)
  - Icons included within the content of the size used from Font Awesome [here](https://fontawesome.com/v5.15/icons?d=gallery&p=2&m=free)
  - Images used across the site taken from Unsplash [here](https://unsplash.com/). Specfic images used are:
   - A Sweet Treat Photo by [Analia Baggiano](https://unsplash.com/s/photos/sweets?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash)
   - Extra Time on Tablet Photo by [José Reyes](https://unsplash.com/s/photos/tablet?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash)
   - A New Magazine Photo by [Omar Flores](https://unsplash.com/s/photos/kids-book?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash)
   - A New Toy Photo by [Robo Wunderkind](https://unsplash.com/s/photos/childrens-toys?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash)
 ### Additional Resource
  - [Code Institue sample README file](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md) helped me to further build my own README for Collection of Crafts (MS1) project.
  - [Code Institue old sample README file](https://github.com/Code-Institute-Solutions/SampleREADME#readme) helped me to further build my own README for Collection of Crafts (MS1) project.
  - [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) was referenced for the languages used in this project. 
  - [Mockup design](http://ami.responsivedesign.is/#) used to create my responsive design file.
  - [W3schools](https://www.w3schools.com/) for various code information and trouble shooting.
  - [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript) for more Javascript specific syntax and function code information.
  - [Favicon](https://favicon.io/) used to generate the favicon icon of the site.
  - [Google fonts](https://fonts.google.com/) used to import the site fonts.
  - [Balsamiq wireframe](https://balsamiq.com/) used to create the wireframe during the design process.
  - [Font Awesome](https://fontawesome.com/) used for icons in the footer and icons within the content of the site for aesthetic and UX purposes.
  - [Unsplash](https://unsplash.com/) images taken from unsplash.
  - [HTML Validator](https://validator.w3.org/) used to test validity of HTML.
  - [CSS Validator](https://validator.w3.org/) used to test validity of CSS.
  - [Wave Accessibility](https://wave.webaim.org/) used to test accessibility of the site.
  - [JS Hint Checker](https://jshint.com/) used to test validity and working functions of Javascript.
 ### Acknowledgements
  - Brian Macharia - Mentor support. A thank you for your guidance throughout the project.
  - Code Institue Slack Community - A great resource and helpful community supported me through the challenges encountered.

**This project is for educational use only and was created for the Code Institue Portfolio Project 2: JavaScript Essentials**