#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;

int a;
int b;

pair<int, int> fun(int A, int B) {
    int minint = std::min(A,B);
    int maxint = std::max(A,B);
    
    minint = minint + 10;
    maxint = maxint * 2;
    return make_pair(minint, maxint); 
}

int main() {
    cin >> a >> b;
    if(a != b) {
        pair<int, int> result = fun(a,b);
        // 원래의 a, b 값을 수정된 값으로 업데이트
        if(a < b) {
            a = result.first;
            b = result.second;
        } else {
            b = result.first;
            a = result.second;
        }
        cout << a << " " << b;  // 수정된 a, b 값을 출력
    }
    
    return 0;
}
