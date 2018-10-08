//pade.cpp
//aproksymacja Pade funkcji exp(-x)
#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

int main()
{
	ofstream G("pade.dat");
	double y,z1,z2,zz1,zz2;
	double d = 0.1;
	double x = 0.0;
	for(int i = 0; i < 50; i++)
	{
		x += d;
		y  = exp(-x);
		z1 = (6.0 - 2.0*x)/(6.0 + 4.0*x + x*x);
		z2 = (6.0 - 4.0*x + x*x)/(6.0 + 2.0*x);
		zz1= y - z1;
		zz2= y - z2;
		G << x << "\t" << y << "\t" << z1 << "\t" << z2 << "\t" << zz1 << "\t" << zz2 <<"\n";
	}
}
