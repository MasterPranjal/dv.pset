var x,y;
var flag1 = false;
var flag2 = false;
function setup()
{
  createCanvas(500,500);
  background(200);
  x1=50;
  y1=250;

  x2=450;
  y2=250;
}
function draw() {
    clear();
    ellipse(x1,y1,50,50);
    if (!flag1){
      x1 += 5;
    }
    else x1-= 5;

    if(x1==450) {
      flag1 = true;
    }

    if ( x1==50) {
      flag1 = false;
    }

  ellipse(x2,y2,50,50);
  if (!flag2){
    x2 -= 5;
  }
  else x2+= 5;

  if(x2==50) {
    flag2 = true;
  }

  if ( x2==450) {
    flag2 = false;
  }
}
