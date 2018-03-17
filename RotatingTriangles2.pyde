'''copy of another sketch @rantonse posted on twitter
Python version with sliders 12/31/16'''

from slider import Slider

num = 90; #number of triangles
t = 0.0;
dt = 0.1;
slider1 = Slider(0,20,6);
slider2 = Slider(10,120,90);

def setup():
  size(500,600)
  colorMode(HSB)
  strokeWeight(2)
  slider1.position(10,10)
  slider2.position(10,60);
  
def draw():
  global t,dt
  background(255);
  offset = slider1.value();
  num = int(slider2.value());
  slider1.label = "offset"
  slider2.label = "number"
  translate(width/2,height/2);
  for i in range(num):
    pushMatrix();
    rotate(-PI/2 + radians(i/float(num)*360));
    translate(150,0);
    rotate(t/4 +i/offset);
    fill(i*5,300,300);
    #angle from 0 to 180 degrees
    j = map(i,0,num,0,PI)
    #size of triangle from 0 to max
    sz = map(sin(j),0,1,0,150);
    strokeWeight(2)
    tri2(sz);
    popMatrix();
  t += dt;

#the triggy method
def tri(sz):
  beginShape();
  for i in range(3):
      vertex(sz*cos(2*PI/3*i), sz*sin(2*PI/3*i));

  endShape(CLOSE)

#the special triangles method
def tri2(sz):
  triangle(-sz/2,sz/(2*sqrt(3)),
          sz/2,sz/(2*sqrt(3)),
          0,-sz/sqrt(3));
  