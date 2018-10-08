//6x^4+5x^3-13x^2+x+1
#include <iostream>
#include <cmath>

using namespace std;

double horner(int wsp[],int st, double x)
{
  if(st==0)
    return wsp[0];
 
  return x*horner(wsp,st-1,x)+wsp[st];
}

double wielomian(double x)
{
	return 6 * pow(x, 4) + 5 * pow(x, 3) - 13 * pow(x, 2) + x + 1;
}


int main()
{
	int wsp[] = {6,5,-13,1,1};

	for (double i = -10; i < 10; i += 0.0001)
		/*horner(wsp,4,i);*/
		wielomian(i);

}
