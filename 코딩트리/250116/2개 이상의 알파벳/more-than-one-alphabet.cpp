#include <iostream>
#include <string>

using namespace std;

string A;
bool  check(string A);

int main() {
    cin >> A;

    bool re = check(A);
    if(re){
        cout<<"Yes"<<endl;
    }else{
        cout<<"No"<<endl;
    }
    
    
     
    return 0;
}

bool check(string A){

    for(int i=0;i<sizeof(A);i++){
        for(int j=1;j<sizeof(A)-1;j++){
            if(A[i] != A[i+j]){
                return true;
        }else{return false;}
        }
    }
}