This repository is for Aalto University CS-C3170 - Web Software Development course project. The project was made in teams of three people.

<h1>Final Submission</h1>

<h3>Implemented features</h3>

We implemented all features except RESTful API and Social Media sharing. Looking backwards, we think that we we're successful in all implemented features. We had some struggles with implementing the payment method and linking our own game to our service (since it is hosted in our own page). We would give ourselves at least max - 50 points per feature. All of us tried to learn something from every created feature, but we did divide some responsibility areas. Valtteri had his focus on styling, interaction, mobile friendliness, payment and player functionalities, Oskari on Game/service interaction, payment, Save/load and resolution feature, developer functionalities and our own game and Jussi concentrated on Authentication, 3rd party login and Heroku implementation.


<h3>Instructions</h3>

You can sign up on our site as a developer or as a player. Player has four main views; home page shows games that player has purchased, browse games page shows all games available on the website, Highscores page shows every game and their highscores and every game has own detail page where the game is played. Player can also search games with a game name from navigation bar. Browse games page has links to purchase games that user does not yet own. Developer has two additional views; view where developer can add new games to site and sales stats view that shows sales for each developer's games. Developer cannot buy or play games, except their own games.




<h1>Project plan</h1>

<h2>WSD 2019</h2>





<h3>Description</h3>

First of all, we need to familiarize more the Django framework. We plan first to do a version with the mandatory functional requirements that also meet the generic requirements and signs of quality in the project description. First version is tested for different attacks and security is improved if needed. After that we will work on extra features if we have time for them.  



<h3>Structure</h3>

Views we are going to implement:  

- list of developer’s games,  

- available games for player to purchase,  

- games user has purchased,  

- scores of a game,

- transactions of a user,  

- list of developers,  

- list of registered players,  



Different models could be:  games, developers, players, game sessions, transaction  

- <b>Game:</b> name, URL, current high score, price

- <b>Developer:</b> name, password (through django user model), inventory of games that are on sale,   

- <b>Player:</b> name, password (through django user model), ongoing games

- <b>Transaction:</b> game, player, price

- <b>Game session:</b> player, game, save, score  



<h3>Workflow</h3>

We are going to meet weekly face-to-face and we will discuss the next steps in the project and individual tasks that should be completed by the next meeting. Hopefully our workflow will be a bit scrum like with changing sprint lengths. The only tool we are planning to use is git through version.aalto.fi and hopefully with proper use of branching the working on same repo jointly will be successful.



<h3>Implementation and timetable</h3>

Starting from beginning of semester and inside dl would be a week before the courses dl.

Implementation order from most crucial to less crucial and hopefully we will have time to do all the extra features given in the example and not only meet the necessary requirements.
