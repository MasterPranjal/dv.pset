//Simple Harmonic Motion
var angle = 0.0;

function setup()
{
	createCanvas(300, 300);
	background(250,0,0);
	strokeWeight(2);

}

function draw()
{
	var amplitude = 50;
  var y = amplitude * sin(angle);
  angle += 0.03;

  stroke(0);
  fill(150);
  translate(width/2,height/2);
  line(0,0,0,y);
  ellipse(0,y,20,20);

}
