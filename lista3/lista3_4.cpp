//6x^4+5x^3-13x^2+x+1
#include <iostream>
#include <cmath>

using namespace std;

double wielomian(double x)
{
	return 6*pow(x,4)+5*pow(x,3)-13*pow(x,2)+x+1;
}

int main()
{

for(double i = -1.0; i < 1.0; i+=0.0001)
{
	cout << wielomian(i);
}
}
