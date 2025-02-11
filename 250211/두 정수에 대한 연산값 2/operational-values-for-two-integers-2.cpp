#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;

int a;
int b;

pair<int ,int > fun(int A, int B){
    int minint = std::min(A,B);
    int maxint = std::max(A,B);
    
    minint = minint+10;
    maxint = maxint*2;
    //cout<<minint<<" "<<maxint;
    return make_pair(minint, maxint); 
}
int main() {
    cin >> a >> b;
    if(a!=b){
       pair<int , int> result = fun(a,b);
       cout<<result.first<<" "<<result.second;
    }
    
    return 0;


}