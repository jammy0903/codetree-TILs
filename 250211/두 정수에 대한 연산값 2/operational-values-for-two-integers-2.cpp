#include <iostream>
#include <algorithm>

using namespace std;

int a, b;

int fun(int a, int b){
    auto result = std::minmax(a,b);
    int maxint = result.second*2;
    int minint = result.first+10;

    cout<<minint<<" "<<maxint;
    return 0;
}
int main() {
    cin >> a >> b;
    if(a==b){
        return 0;
    }
    fun(a,b);

    return 0;


}