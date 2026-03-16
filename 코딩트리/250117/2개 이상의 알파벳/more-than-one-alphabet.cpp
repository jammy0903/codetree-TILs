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

bool check(string A) {
    int len = A.length();
    for(int i = 0; i < len; i++) {
        for(int j = i + 1; j < len; j++) {
            if(A[i] != A[j]) {
                return true;  // 다른 문자 발견
            }
        }
    }
    return false;  // 모든 문자가 같음
}