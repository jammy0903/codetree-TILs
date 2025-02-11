#include <iostream>
#include <algorithm>

using namespace std;

int a;
int b;

int fun(int A, int B){
    int minint = std::min(A,B);
    int maxint = std::max(A,B);
    
    minint = minint+10;
    maxint = maxint*2;
    cout<<minint<<" "<<maxint;
    return 0;
}
int main() {
    cin >> a >> b;
    if(a!=b){
        fun(a,b);
    }
    
    return 0;


}