#include <bits/stdc++.h>

using namespace std;

long long int A, B, big, small;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> A >> B;
    
    if(A == 1 || B == 1) {
        cout << A * B;
    } else {
        big = max(A, B);
        small = min(A, B);
        for(int i = 1; big * i <= big * small; i++) {
            if((big * i) % small == 0) {
                cout << big * i;
                break;
            }
        }
    }
      
    return 0;
}