/* ���������� �������� ��� ������� ������ ����������� */

#include <locale>
#include <stdlib.h>
#include <iostream>
#include <malloc.h>

using namespace std;

#define N_MIN	3			// ����������� ���������� ������
#define N_MAX	30			// ������������ ���������� ������

#define ALPHA	1			// ��� ��������
#define BETTA	3			// ����������� ���������

#define T_MAX	100			// ����� ����� �������
#define M		20			// ���������� �������� � �������
#define Q		100			// ����������
#define RHO		0.5			// ����������� ��������� ��������

// ��������� ���� (������, ������ ������, ���������� ������)
struct WAY_TYPE 
{
	int itabu;
	int length;
	int *tabu;
};

// ����������� �������� ������� ant � ������� to
double probability (int to, WAY_TYPE ant, double **pheromone, double **distance, int vertex) 
{
	// ���� ������� ��� ��������, ���������� 0
	for (int i = 0; i < ant.itabu; ++i) 
		if (to == ant.tabu[i]) 
			return 0;

	double sum = 0.0;
	int from = ant.tabu[ant.itabu-1];
	// ������� ����� � �����������
	for (int j = 0; j < vertex; ++j)
	{
		int flag = 1;
		// ���������, ������� �� ������� j �������
		for (int i = 0; i < ant.itabu; ++i) 
			if (j == ant.tabu[i]) 
				flag = 0;
		// ���� ���, ����� ���������� � ����� �����
		if (flag) 
			sum += pow (pheromone[from][j], ALPHA) * pow (distance[from][j], BETTA);
	}
	// ���������� �������� �����������
	return pow (pheromone[from][to], ALPHA) * pow (distance[from][to], BETTA) / sum;
}

// �������� ������� ��������� ������
WAY_TYPE AntColonyOptimization (double **distance0, int vertex, int start, int finish) 
{
// ������������� ������ � ������ ��������
	WAY_TYPE way;
	way.itabu = 0;
	way.length = -1;
	way.tabu = (int *) malloc (sizeof (int) * vertex);
// ������������� ������ � ���������� � ���������� ��������
	double **distance = NULL, **pheromone = NULL;
	distance = (double **) malloc (sizeof (double *) * vertex);
	pheromone = (double **) malloc (sizeof (double *) * vertex);
	for (int i = 0; i < vertex; ++i) 
	{
		distance[i] = (double *) malloc (sizeof (double) * vertex);
		pheromone[i] = (double *) malloc (sizeof (double) * vertex);
		for (int j = 0; j < vertex; ++j) 
		{
			pheromone[i][j] = 1.0 / vertex;
			if (i != j) 
				distance[i][j] = 1.0 / distance0[i][j];
		}
	}
// ������������� ��������
	WAY_TYPE ants[M];
	for (int k = 0; k < M; ++k) 
	{
		ants[k].itabu = 0;
		ants[k].length = 0.0;
		ants[k].tabu = (int *) malloc (sizeof (int) * vertex);
		ants[k].tabu[ants[k].itabu++] = start;
	}

// �������� ����
	for (int t = 0; t < T_MAX; ++t) 
	{
	// ���� �� ��������
		for (int k = 0; k < M; ++k) 
		{
		// ����� �������� ��� k-�� �������
			do {
				int j_max = -1;
				double p_max = 0.0;
				for (int j = 0; j < vertex; ++j) 
				{
				// �������� ����������� �������� � ������� j
					if (ants[k].tabu[ants[k].itabu-1] != j) 
					{
						double p = probability (j, ants[k], pheromone, distance, vertex);
						if (p && p >= p_max) 
						{
							p_max = p;
							j_max = j;
						}
					}
				}
				ants[k].length += distance0[ants[k].tabu[ants[k].itabu-1]][j_max];
				ants[k].tabu[ants[k].itabu++] = j_max;
			} while (ants[k].tabu[ants[k].itabu-1] != finish);
		// ��������� ������� �� ���� �������
			for (int i = 0; i < ants[k].itabu-1; ++i) 
			{
				int from = ants[k].tabu[i % ants[k].itabu];
				int to = ants[k].tabu[(i+1) % ants[k].itabu];
				pheromone[from][to] += Q / ants[k].length;
				pheromone[to][from] = pheromone[from][to];
			}
		// �������� �� ������ �������
			if (ants[k].length < way.length || way.length < 0) 
			{
				way.itabu = ants[k].itabu;
				way.length = ants[k].length;
				for (int i = 0; i < way.itabu; ++i) 
					way.tabu[i] = ants[k].tabu[i];
			}
		// ���������� ��������
			ants[k].itabu = 1;
			ants[k].length = 0.0;
		}
	// ���� �� ������
		for (int i = 0; i < vertex; ++i)
			for (int j = 0; j < vertex; ++j)
			// ���������� �������� ��� ����� (i, j)
				if (i != j) pheromone[i][j] *= (1 - RHO);
	}
	// ���������� ���������� �������
	return way;
}

// ����� ����� � ���������
int main (int argc, char *argv[]) 
{
	setlocale (LC_ALL, "Russian");

	double **D = NULL;
	int N = 0, A = 0, B = 0;
// ������������� ������� ����������
	while (N < N_MIN || N > N_MAX) 
	{
		cout << "������� ���������� ������ [" << N_MIN << ", " << N_MAX << "]: "; cin >> N;
	}
	cout << "������� ������� ����������" << endl;
	D = (double **) malloc (sizeof (double *) * N);
	for (int i = 0; i < N; ++i) 
	{
		D[i] = (double *) malloc (sizeof (double) * N);
		for (int j = 0; j < N; ++j)
		{
			if (i == j)
				D[i][j] = 0;
			else if (i > j)
				D[i][j] = D[j][i];
			else
			{
				cout << "������� ���������� �� ������� " << i+1 << " � ������� " << j+1 << ": ";
				cin >> D[i][j];
			}
		}
	}

// ����� ���������� ����� ���������
	cout << "������� ���������� ����� ���������: " << endl;
	cout << "  1\t2\t3\t " << endl;
	for (int i = 0; i < N; ++i) 
	{
		cout << i+1 << " ";
		for (int j = 0; j < N; ++j)
		{
			cout << D[i][j] << " \t";
		}
		cout << endl;
	}

// ������������� ��������� � �������� �����
	while (A < 1 || A > N) 
	{
		cout << "������� ��������� ������� �� 1 �� " << N << ": "; cin >> A;
	}
	while (B < 1 || B > N || B == A) 
	{
		cout << "������� �������� ������� �� 1 �� " << N << " �������� " << A << ": "; cin >> B;
	}

// ��������� ��������
	WAY_TYPE way = AntColonyOptimization (D, N, --A, --B);

// ������� ���������
	cout << "������ ����: " << way.length << endl;
	cout << "����: " << ++way.tabu[0];
	for (int i = 1; i < way.itabu; ++i) 
		cout << " -> " << ++way.tabu[i];
	
	cin.get();
	cin.get();

	return 0;
}