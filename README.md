<h1>Project plan</h1>

<h2>WSD 2019</h2>



<h3>Team</h3>

Group: Valtteri Luodemäki 605845, Oskari Heinonen 605573, Jussi Huotari 353252



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

