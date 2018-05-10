var x,y;
var a,f;
x = 0; //time axis
a = 50; //Amplitude
f = 20; //frequency

function setup()
{
 createCanvas(300,300);
 background(255,0,0);
 strokeWeight(5);
}

function draw()
{
  y = 200 +  a * sin(6.28*f*x); //200 shift y axis downwards
  x++;
  point(x,y);

}
