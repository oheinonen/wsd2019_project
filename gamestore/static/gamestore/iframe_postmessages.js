function showAlert(data){
  alert(data);
};
window.addEventListener('message', function(event) {

  switch (event.data.messageType) {

    case "SCORE":

      $.ajax({
        type: 'get',
        url: 'highscore/',
        data: {
          score: event.data.score
        },
        success: function (data) {
          alert(`Game over! Your score is ${event.data.score}.`);
        },
        error: function(data) {
          alert(`Error! Your score is not submitted.`);
        }
      });
      break;

    case "SAVE":

      $.ajax({
        type: 'get',
        url: 'save/',
        data: {
          gameState: JSON.stringify(event.data.gameState)
        },
        success: function (data) {
          alert(`Game saved! Your score is ${event.data.gameState['score']} and items ${event.data.gameState['playerItems']}.`);
        },
        error: function(data) {
          alert(`Error! Your game is not saved`);
        }
      });
      break;

    case "LOAD_REQUEST":

      $.ajax({
        type: 'get',
        url: 'load/',

        success: function (data) {
          var msg = {
            "messageType": "LOAD",
            "gameState": JSON.parse(data)
          };

          document.getElementById('iframe').contentWindow.postMessage(msg, '*');
          alert(`You game is now loaded`);
        },

        error: function(data) {
          var msg = {
            "messageType": "ERROR",
            "info": "Gamestate could not be loaded."
          };

          document.getElementById('iframe').contentWindow.postMessage(msg, '*');
        }
      });
      break;

    case "SETTING":
    //  document.getElementById('iframe').style.width = event.data.options.width;
    //  document.getElementById('iframe').style.height = event.data.options.height;
      $("#iframe").width(event.data.options.width);
      $("#ifrae").height(event.data.options.height);
      alert(`Game from ${event.origin} loaded.`);
      break;
  };
});
