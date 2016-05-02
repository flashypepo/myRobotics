var five = require("johnny-five");
var board = new five.Board();

board.on("ready", function() {
  console.log("Ready event. Repl instance auto-initialized!");

  var led = new five.Led(3); // 2016_0112 led was op 9
    //* use REPL
    this.repl.inject({
        l : led
    });
  /*/
  this.repl.inject({
    // Allow limited on/off control access to the
    // Led instance from the REPL.
    on: function() {
      led.on();
    },
    off: function() {
      led.off();
    }
  });
  //*/
  led.on();
});
