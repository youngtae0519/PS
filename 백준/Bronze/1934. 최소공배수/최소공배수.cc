#include <bits/stdc++.h>

using namespace std;

int T, A, B;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> T;
    
    for(int i = 0; i < T; i++) {
        cin >> A >> B;
        
        if(A == 1 || B == 1) {
            cout << A * B << "\n";
        } else {
            for(int i = 1; A * i <= A * B; i++) {
                if((A * i) % B == 0) {
                    cout << A * i << "\n";
                    break;
                }
            }
        }
    }    
    
    return 0;
}