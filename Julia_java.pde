//Java version of Julia Set from Math Adventures with Python

//Declare 2-element array, assign to variable c
float[] c = new float[2];

//set the range of x-values
int xmin=-2;
int xmax=2;

//range of y-values
int ymin = -2;
int ymax = 2;

//calculate the range
float rangex = xmax - xmin;
float rangey = ymax - ymin;

//Declare xscl and yxscl
// We'll assign them values in setup

float xscl = rangex/600;
float yscl = rangey/600;

void setup(){
    size(600,600);
    colorMode(HSB);
    noStroke();

}
    
void draw(){
    //Declare the components of c
    c[0] = 0.25*mouseX*xscl; //real
    c[1] = 0.25*mouseY*yscl; //imaginary
    //go over all x's and y's on the grid
    for (int x=0;x<width;x++){
        for (int y=0;y<height;y++){
            float[] z ={xmin+x*xscl,ymin+y*yscl};
            //put z into the julia function
            int col=julia(z,100);
            //if julia returns 100
            //that location never diverged
            //not in julia set --> black
            if (col == 100){
                fill(0); //black
            }else{
              //calculate color from "col"
                int c1 = (255-2*col);
                fill(c1,255,255);
            }
            rect(x,y,1,1); //draw the tiny rectangle
        }
    }
  }
    

int julia(float[] z,int num){
    //runs the process num times
    //and returns the diverge count
    int count=0;
    //define z1 as z
    float[] z1 = z;
    //iterate num times
    while (count <= num){
        //check for divergence
        if (magnitude(z1) > 2.0){
        //return the step it diverged on
            return count;
        }
        //iterate z
        z1=cAdd(cMult(z1,z1),c);
        count+=1;
    }
    //if z hasn't diverged by the end
    return num;
}


float[] cAdd(float[] a,float[] b){
  float[] output = {a[0]+b[0],a[1]+b[1]};
    return output;
}

float[] cMult(float[] u,float[] v){
    //Returns the product of two complex numbers
    float[] output = {u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]};
    return output;
}
 

float magnitude(float[] z){
    float output = z[0]*z[0] + z[1]*z[1];
    if (output == 0){
      return 0;
    } else {
      return sqrt(output);
    }
}
