#include <iostream>
using namespace std;

int mod(int *x){
    
    for(int i=0;i<=sizeof(*x);i++){
        if(x[i]%2 ==0){x[i]=x[i]/2;}
    }
    for(int j=0;j<=sizeof(*x);j++){
        cout<<x[j]<<" ";
    }    
    return 0;

}


int main() {
    // 여기에 코드를 작성해주세요.
    int N;
    int arr[N];
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>arr[i];

    }
    mod(arr);
    return 0;
}