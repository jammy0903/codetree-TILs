#include <iostream>
using namespace std;

bool correct(int num1);

bool correct(int num1) {
    int fir = num1/10;
    int sec = num1%10;

    // 3의 배수인 경우
    if(num1 % 3 == 0) {return true; }

        
    
    // 첫째 자리가 3,6,9이고
    if ((fir == 3)|| (fir == 6) || (fir == 9)||(sec == 3) || (sec == 6) || (sec == 9) ){
        // 둘째 자리가 3,6,9이고
    return true;      
    }
    return false;  // 조건을 만족하지 않는 경우
}

int main() {
    int a, b;
    int cnt = 0;
    cin >> a >> b;
    
    for(int i = a; i <= b; i++) {
        if(correct(i)) {
            
            cnt++;
        }
    }
    cout << cnt;
    
    return 0;
}
