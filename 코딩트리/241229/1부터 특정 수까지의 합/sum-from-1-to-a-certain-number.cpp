#include <iostream>
#include <string>
using namespace std;

int fun(int a);

int main(){
    int N=0;
    
    cin >> N;
    int result = fun(N);

    return(0);
}

int fun(int a){
    
    int sum=0;
    for(int i=1;i<a+1;i++){
        sum +=i;
        int wd = sum;
    }
    int dvd = sum/10;
    cout << dvd;
    return (dvd);
}


