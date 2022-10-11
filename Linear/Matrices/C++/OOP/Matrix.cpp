#include <iostream>
using namespace std;
class Matrix {
private:
    int row, col, r, c;
    int A[10][10], B[10][10], C[10][10];
public:
    void size();
    void InputMatrixA();
    void InputMatrixB();
    void AddMatrix();
    void SubMatrix();
    void PrintMatrixC();
};

void Matrix::size() {
    cout << "Enter number of rows: ";
    cin >> row;
    cout << "Enter number of columns: ";
    cin >> col;
}
// Input elements of Matrix A.
void Matrix::InputMatrixA() { 
    cout << endl << "Input for Matix A: " << endl;
    for (r = 0; r < row; ++r)
        for (c = 0; c < col; ++c)
        {
            cout << "Input element A" << r + 1 << c + 1 << " : ";
            cin >> A[r][c];
        }
}
// Input elements of Matrix B.
void Matrix::InputMatrixB() {
    cout << endl << "Input for Matrix B: " << endl;
    for (r = 0; r < row; ++r)
        for (c = 0; c < col; ++c)
        {
            cout << "Input element B" << r + 1 << c + 1 << " : ";
            cin >> B[r][c];
        }
}
// Adding Matrix A and B
void Matrix::AddMatrix() {
    cout << endl << "Adding Matrix A and B: " << endl;
    for (r = 0; r < row; ++r)
        for (c = 0; c < col; ++c)
            C[r][c] = A[r][c] + B[r][c];
}
// Subtract Matrix B from A
void Matrix::SubMatrix() {
    cout << endl << "Subtracting Matrix B from A: " << endl;
    for (r = 0; r < row; ++r)
        for (c = 0; c < col; ++c)
            C[r][c] = A[r][c] - B[r][c];
}
 // Print Matrix C matrix.
    void Matrix::PrintMatrixC() {
        cout << endl << "Matrix C =: " << endl;
        for (r = 0; r < row; ++r)
            for (c = 0; c < col; ++c)
            {
                cout << C[r][c] << "  ";
                if (c == col - 1)
                    cout << endl;
            }

}
    
int main()
{ 
    Matrix Mat;
    Mat.size();
    Mat.InputMatrixA();
    Mat.InputMatrixB();
    Mat.AddMatrix();
    Mat.PrintMatrixC();
    Mat.SubMatrix();
    Mat.PrintMatrixC();
}