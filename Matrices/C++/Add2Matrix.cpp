#include <iostream>
using namespace std;

int main()
{
    int row, col, r, c;
    int MatrixA[10][10], MatrixB[10][10], MatrixC[10][10];

    cout << "Enter number of rows: ";
    cin >> row;
    cout << "Enter number of columns: ";
    cin >> col;

    // Input elements of Matrix A.
    cout << endl << "Input for Matix A: " << endl;
    for (r = 0; r < row; ++r)
        for (c = 0; c < col; ++c)
        {
            cout << "Input element A" << r + 1 << c + 1 << " : ";
            cin >> MatrixA[r][c];
        }

    // Input elements of Matrix B.
    cout << endl << "Input for Matrix B: " << endl;
    for (r = 0; r < row; ++r)
        for (c = 0; c < col; ++c)
        {
            cout << "Input element B" << r + 1 << c + 1 << " : ";
            cin >> MatrixB[r][c];
        }

    // Adding Matrix A and B
    for (r = 0; r < row; ++r)
        for (c = 0; c < col; ++c)
            MatrixC[r][c] = MatrixA[r][c] + MatrixB[r][c];

    // Print Matrix C matrix.
    cout << endl << "Sum of two matrix is: " << endl;
    for (r = 0; r < row; ++r)
        for (c = 0; c < col; ++c)
        {
            cout << MatrixC[r][c] << "  ";
            if (c == col - 1)
                cout << endl;
        }

    return 0;
}