/*
In the terminal you need to write:

g++ Contours-exactos.cpp -o Contours-exactos.out
./Contours-exactos.out


The output of this script is a file called: Contour_Strong+Weak.dat

*/


#include <iostream> //como import, input output functions
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>




using namespace std; // como from numpy import *

//g++ fraccionesVsMag.cpp -o fraccionesVsMag.out


int compare (const void * a, const void * b)
{
  return ( *(double*)a > *(double*)b ) ? 1 : -1;
}



int main()
{

int N=1592;							//total number of galaxies
double lambda[N];
double Mag[N], Tipo[N];
double x[N], y[N], z[N], w[N];




	ifstream entrada;
	entrada.open("R0.7_Bar_Weight_Mass_BV.dat");

	double bar, weight, mass, color;
	int i,j,k;
	i=0;

	while(!entrada.eof()){
		


	entrada >> bar >> weight >> mass >> color;		//columns per line

	x[i]=mass;
	y[i]=color;
	z[i]=bar;
	w[i]=weight;

//	cout << w[i] << endl;

	i=i+1;




	}

	entrada.close();


//////////////////////////////
//////////////////////////////

    
    
    double xmin, xmax, ymin, ymax, ddx, ddy, smoothx, smoothy;
    
    int Nbinx=6;			//Number of bins in x-axis
    int Nbiny=6;			//Number of bins in y-axis
    
    double Nmin=15.0;		//Minimum number of galaxies per square bin to estimate the bar fraction
    
    xmin=8.5;				//Here you choose the limits of the area to divide into bins
    xmax=11.5;
    ymin=-0.3;
    ymax=1.8;
    
    
    ddx=(xmax-xmin)/Nbinx;
    ddy=(ymax-ymin)/Nbiny;
    
    
    double Binx[Nbinx], Biny[Nbiny], Binz[Nbinx][Nbiny];
    double countNon, countBar, countStrong, countWeight, countTotal;
    
    
    
    
    
    ofstream myfile1;
    myfile1.open ("R0.7_Contour_Mass_BV.dat");
    
    
    for(i=0; i<Nbinx; i++)
	{Binx[i]=xmin+i*ddx-ddx/2;
        
        for(j=0; j<Nbiny; j++)
		{Biny[j]=ymin+ddy*j-ddy/2;
            
            countNon=0., countBar=0., countStrong=0., countWeight=0., countTotal=0.;
            
            
            for(k=0;k<N;k++)
			{
                if(x[k]> Binx[i]-ddx && x[k] < Binx[i]+ddx && y[k]> Biny[j]-ddy && y[k]<Biny[j]+ddy)
				{
                    countTotal=countTotal+1;
                    countWeight=countWeight+w[k];
                    if(z[k] > 0.5)
                        countStrong=countStrong+w[k];
//				myfile1 << Binx[i] << "\t" << Biny[j] << "\t" << countStrong << endl;

                    
				}
                
                
			}
			
			if(countTotal > Nmin )
            {Binz[i][j]=(countStrong)/countWeight;
				myfile1 << Binx[i] << "\t" << Biny[j] << "\t" << Binz[i][j] << endl;
            }	
			
			
            
		}
		myfile1 << "   " << endl;		// Linea extra para gnuplot
	}
    
    
    myfile1.close();
    

    
    
}
