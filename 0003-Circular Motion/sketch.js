var m=3.00, r=20, x,y;

function setup(){
	createCanvas(500, 500);
	background(100,0,0);
	strokeWeight(1);
	smooth();
}

function draw()
{
  x= 100+r*cos(m)*2;
  y= 100+r*sin(m)*2;
	m=m+0.06;

  ellipse(x,y,50,50);

}
