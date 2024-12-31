#include <iostream>
using namespace std;


int temping(int &a, int &b){
    int temp = a;
    a=b;
    b=temp;
    return a,b;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n,m;
    cin>>n>>m;
    n,m = temping(n,m);
    cout << n << " " << m; 
    return 0;
}
