#include <iostream>
#include <algorithm>

using namespace std;

int a;
int b;

int fun(int a, int b){
    int minint = std::min(a,b);
    int maxint = std::max(a,b);
    
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