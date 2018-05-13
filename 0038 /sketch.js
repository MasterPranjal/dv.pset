var x,y;
var m;
var r1, r2;
r1=30;
r2=10;
m=0.2;

r3=40;
r4=20;

r5=50;
r6=30;

r7=60;
r8=40;

r9=70;
r10=50;

r11=80;
r12=60;

r13=90;
r14=70;

r15=110;
r16=80;

function setup()
{
 createCanvas(500,500);
 background(255,0,0);
}

function draw()
{
  ellipse(250,250,50,50);

  //1st planet
  x = 250 + r1 * cos(m);
  y = 250 + r2 * sin(m);
  m = m+20;

  ellipse(x,y,10,10);

  //2nd planet
  x = 250 + r3 * cos(m);
  y = 250 + r4 * sin(m);
  m = m+20;

  ellipse(x,y,5,5);

  //3rd planet
  x = 250 + r5 * cos(m);
  y = 250 + r6 * sin(m);
  m = m+20;

  ellipse(x,y,10,10);

  //4th planet
  x = 250 + r7 * cos(m);
  y = 250 + r8 * sin(m);
  m = m+20;

  ellipse(x,y,6,6);

  //5th planet
  x = 250 + r9 * cos(m);
  y = 250 + r10 * sin(m);
  m = m+20;

  ellipse(x,y,8,8);

  //6th planet
  x = 250 + r11 * cos(m);
  y = 250 + r12 * sin(m);
  m = m+20;

  ellipse(x,y,10,10);

  //7th planet
  x = 250 + r13 * cos(m);
  y = 250 + r14 * sin(m);
  m = m+20;

  ellipse(x,y,4,4);

  //8th planet
  x = 250 + r15 * cos(m);
  y = 250 + r16 * sin(m);
  m = m+20;

  ellipse(x,y,2,2);

}
