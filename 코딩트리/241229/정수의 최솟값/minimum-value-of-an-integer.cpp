#include <iostream>
using namespace std;

int fun(int A, int B, int C);

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,c;
    cin>>a>>b>>c;
    
    cout<<fun(a,b,c);
    return 0;
}

int fun(int A, int B, int C){
    int mini=min(min(A,B),min(B,C));
    int minimini = min(mini,min(A,C));
    return(minimini);
}