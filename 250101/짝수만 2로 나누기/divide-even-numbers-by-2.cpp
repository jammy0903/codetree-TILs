#include <iostream>
using namespace std;


int mod(int *x,int size){

    for(int i=0;i<size;i++){
        if(x[i]%2==0){
            x[i]=x[i]/2;
        }
    }
    return 0;
}


int main() {
    // 여기에 코드를 작성해주세요.
    int N;
    cin>>N;

    int* arr = new int[N];
    for(int i=0;i<N;i++){
        cin>>arr[i];
    }
    mod(arr,N);
    for(int i=0;i<N;i++){
        cout<<arr[i]<<" ";
    }
    delete[] arr;
    return 0;
}