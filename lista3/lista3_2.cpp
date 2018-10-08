#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
	int A[2][2] = { {2,4},{8,-3} };
	int B[2][2] = { {-5,4},{2,0} };
	int C[2][2];

	for (int i = 0; i < 2; i++)
		for (int j = 0; j < 2; j++)
		{
			C[i][j] = 0;
			for (int k = 0; k < 2; k++)
			{
				C[i][j] += A[i][k] * B[k][j];
			}
			cout << C[i][j] << "\n";
		}
	system("pause");
}
