var x, y;
var flag=false;
function setup()
{
  createCanvas(500,500);
  background(100);
  x=50;
  y=250;
}

function draw()
{
  ellipse(x,y,50,50);
  if(!flag)
  {
    x=x+1;
  }
  else x=x-1;

  if(x==450)
  {
    flag=true;
  }

  if(x==50)
  {
    flag=false;
  }

}
