var x,y;
var m;
var r1, r2;
r1=20;
r2=50;
m=0.2;
function setup()
{
 createCanvas(500,500);
 background(255,0,0);


}

function draw()
{
  ellipse(250,250,20,20);

  x = 250 + r1 * cos(m);
  y = 250 + r2 * sin(m);
  m = m+20;

  ellipse(x,y,10,10);

}
