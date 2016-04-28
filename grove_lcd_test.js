// 2016_0428
var five = require("johnny-five");
var board = new five.Board();

board.on("ready", function() {

    var lcd = new five.LCD({ 
        controller: "JHD1313M1"
    });
    // use REPL
    this.repl.inject({
        l : lcd
    });

  lcd.print("Hello");
});