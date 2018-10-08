#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <string>

using namespace std;

unsigned long int silnia(int x)
{
	unsigned long int wynik=1;
	for(int i=1;i <= x;i++)
		wynik *= i;
		
		return wynik;
}

long double sum(int x, int N,string name)
{
	long double wynik=0;
	ofstream G(name);
	
	for(int i=0;i <= N;i++)
	{
		wynik += pow(x,i)/silnia(i);
		G << setprecision(100)<< i << "\t" << wynik << "\t" << wynik - exp(x) << "\n";
	}
	
	return wynik;
}


int main()
{
	sum(10,60,"data10.txt");
	sum(2,60,"data2.txt");
	sum(-2,60,"data-2.txt");
	sum(-10,60,"data-10.txt");
}
