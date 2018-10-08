#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int sgn(double x)
{
	if (x > 0) return 1;
	if (x < 0) return -1;
	return 0;
}

double b(double i)
{
	return pow(10, i);
}

int main()
{
	double a = 100;
	double c = 100;
	double x1;
	double x2;
	double x11;
	double x22;

	for (double i = 7.4; i < 8.5; i += 0.1)
	{
		x1 = (1 / (2 * a))*(-b(i) - sgn(b(i))*sqrt(pow(b(i), 2) - 4 * a*c));
		x2 = (1 / (2 * a))*(-b(i) + sgn(b(i))*sqrt(pow(b(i), 2) - 4 * a*c));

		x11 = (1 / (2 * a))*(-b(i) - sgn(b(i))*sqrt(pow(b(i), 2) - 4 * a*c));
		x22 = c / (a*x11);

		cout << x1 << "\t" << x2 << "\n" << x11 << "\t" << x22 << "\n\n";
	}
	system("pause");
}