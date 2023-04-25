// Team Double A V2 :: Sasha Shifrina, Anna Fang
// SoftDev pd7
// K31 -- canvas based JS animation
// 2023-04-25
// --------------------------------------------------

var c = document.getElementById('playground');
var dotButton = document.getElementById('buttonCircle');
var stopButton = document.getElementById('buttonStop');

var ctx = c.getContext('2d');

ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
  ctx.clearRect(0, 0, playground.width, playground.height);
};

var radius = 0;
var growing = true;

var drawDot = (e) => {
  while(true){
    clear(e);
    requestID = window.requestAnimationFrame();
    ctx.beginPath();
    ctx.arc(playground.width/2, playground.height/2, radius, 0, 2*Math.PI);
    ctx.fill();
    if (growing == true) {
      radius += 1;
    }
    else {
      radius -= 1;
    }
    if (radius*2 >= playground.width) {
      window.cancelAnimationFrame(requestID);
      growing = false;
    }
  }

};

dotButton.addEventListener("click", drawDot);
