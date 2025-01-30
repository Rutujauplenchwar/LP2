#include <bits/stdc++.h>
using namespace std;

class N_Queen
{
    int n;
    char **matrix;

public:
    N_Queen(int x)
    {
        n = x;
        matrix = new char *[n];
        for (int i = 0; i < n; i++)
        {
            matrix[i] = new char[n];
            for (int j = 0; j < n; j++)
            {
                matrix[i][j] = '-';
            }
        }
    }

    bool isSafe(int row, int col)
    {
        int duprow = row;
        int dupcol = col;

        // Check upper diagonal (↖️)
        while (row >= 0 && col >= 0)
        {
            if (matrix[row][col] == 'Q')
                return false;
            row--;
            col--;
        }

        row = duprow;
        col = dupcol;

        // Check left side (←)
        while (col >= 0)
        {
            if (matrix[row][col] == 'Q')
                return false;
            col--;
        }

        row = duprow;
        col = dupcol;

        // Check lower diagonal (↙️)
        while (row < n && col >= 0)
        {
            if (matrix[row][col] == 'Q')
                return false;
            row++;
            col--;
        }

        return true;
    }

    bool solve(int col)
    {
        if (col >= n)
        {
            return true;
        }

        for (int i = 0; i < n; i++)
        {
            if (isSafe(i, col))
            {
                matrix[i][col] = 'Q';

                if (solve(col + 1))
                    return true;
                matrix[i][col] = '-';
            }
        }

        return false;
    }

    void print()
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
};

int main()
{
    int n;
    cout << "\nEnter n = ";
    cin >> n;
    N_Queen pro(n);

    if (pro.solve(0))
    {
        cout << "\nSolution found:" << endl;
        pro.print();
    }
    else
    {
        cout << "\nNo solution exists!" << endl;
    }

    return 0;
}





