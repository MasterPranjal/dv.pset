var x,y,t=0,input,input2,a=PI/6,m=300,n=0,name,button;
var r=0, flag=0;

function setup()
{
  createCanvas(300, 300);
  background(255,0,0);
  stroke(255);
  strokeWeight(5);

  input = createInput();
  input.position(20, 65);
  input2 = createInput();
  input2.position(20, 85);

  greeting = createElement('h5', 'enter u for projectile and angle');
  greeting.position(20, 5);

  button = createButton('submit');
  button.position(20, 105);
  button.mousePressed(update);
}

function draw()
{
  if(flag==1){
  translate(0,height);
  ellipse(UX(),-UY(),5,5);
}
}

function update()
{
  r=input.value();
  a=input2.value()
  flag=1;
}

function UX()
{
  x=(r*cos(PI/6)*t);
  return x;
}

function UY()
{
  y=(r*sin(PI/6)*t - (9.8*t*t)/2);
  t+=0.1;
  return y;
}
