#include <iostream>
using namespace std;

bool correct(int num1) {
    // 3의 배수 체크
    if(num1 % 3 == 0) {
        return true;
    }
    
    // 각 자릿수에 3,6,9가 있는지 체크
    int temp = num1;
    while(temp > 0) {
        int digit = temp % 10;  // 현재 자릿수
        if(digit == 3 || digit == 6 || digit == 9) {
            return true;
        }
        temp /= 10;  // 다음 자릿수로 이동
    }
    
    return false;
}

int main() {
    int a, b;
    int cnt = 0;
    cin >> a >> b;
    
    for(int i = a; i <= b; i++) {
        if(correct(i)) {
            //cout << i << endl;
            cnt++;
        }
    }
    cout << cnt;
    
    return 0;
}
