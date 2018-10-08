#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	double x = 1.0;
	double e = 1;
		
	for(;x+e!=1;e/=2)
	{
		cout << e << "\t" << x+e << endl;
	}
	system("pause");
}
