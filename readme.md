# Recipedia

Recipedia is an online cookbook. It allows users to view reipes online as well as contribute their own. 
it's built using Flask, Python, mongoDB and Pymongo. The full suite of CRUD operations is offered. 

## UX

With the brief focussing on data and interactivity, I though it best to utilise a sparse and clean frontend. I stuck close to the format offered by Materialize supplementing the styling only very occasionally. 
Of importance was the user story:

"I can see a list of recipes and click on them for the full detail"

I used this as the centre of my solution and built the UI around that as a base. 

"i can Create, Read, Update, and Delete recipes"

This was also important in my design ethos. I wanted each of the CRUD activities to be avaialble from the landing page. The Read Update and Delete are served by buttons in the recipe entry itself. The Add is accessed via the nav bar. 

## Features

As mentioned prior. the single screen CRUD was the man force behind this design. Implementation of this along with a stable build was the main aim for this project. 
Because of this the main 'Recipes' view needed to be uncluttered and attractive. Clicking on a recipe brings up a list of ingredients required as well as the RUD buttons mentioned previously. I added Update and Delete buttons to the Recipe view also to underline the straightforward and user friendly design. 
I tried to have all pages mirror this look to offer uniformity across the app. 

### Existing Features

Single Screen CRUD from the landing page : This informed the whole design. Having the CRUD activities available from not just the main page, but most other screens was important.

### Features left to implement

Unfortunately there was a lot of time wasted in my project due to trying to achive this using mySQL instead of MongoDB. Whilst I carried out a lot of work designing a relational db schema, I found the lack of clarity on how to integrate with Pymysql and/or flask-mysql was bringing my work to a standstill. 
Eventually I felt that I had no choice but to migrate to a MongoDB database and felt this to be much more user-friendly. The CodeInstitue's resources were also of more use re MongoDB - frankly I wish that I had elected to use MongoDb from day 1.
For information I have included the mySQL Schema and ERD. 

## Technologies Used

Materialize - a css/js framework that aided with creating a pleasing frontend - https://materializecss.com/
PyMongo     - a Python/MongoDB API. Universal in the connection between app and db - https://api.mongodb.com/python/current/
JQuery      - works in tandem with Materialize  - https://jquery.com

## Testing

The app has been tested on multiple screen sizes inc laptop, desktop, android phone/tablet, ios phone, and to my eyes has proven responsive. 
As a test for defensive design, I had allowed my partner and several colleagues time to attempt to 'break' the app/site. I am satisied that they have been unable to do so. 
All HTML/CSS has been validated at W3C online code validators - with no errors shown other than those caused by the Flask syntax. 

Unfortunately due to the nature of the project, I didn't feel that there was much call for automated testing. 

## Deployment

The app is deployed on Heroku. There are no differences between the local and deployed versions. 
I came across an issue when initially trying to host on heroku caused by the fact that I had initially obscured the mongodb connection. However the app will only successfully launch with the connection SRI noted in the app body. 

## Credits

### Content 

Several recipes were lifted from the following website - https://www.bbc.com/food/recipes
