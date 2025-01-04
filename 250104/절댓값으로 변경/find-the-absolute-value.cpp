#include <iostream>

using namespace std;

int n;
int arr[50];

int main() {
    cin >> n;
    //cout<< n<<endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Write your code here!
    for(int i=0; i<n;i++){  
        if(arr[i]<0){
            int temp=0-arr[i];
            arr[i]=temp;}
        cout<<arr[i]<<" ";

    }

    return 0;
}