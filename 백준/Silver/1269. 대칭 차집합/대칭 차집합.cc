#include <bits/stdc++.h>

using namespace std;

int a, b, num, ans;
set<int> A, B;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> a >> b;
    
    for(int i = 0; i < a; i++) {
        cin >> num;
        A.insert(num);
    }
    
    for(int i = 0; i < b; i++) {
        cin >> num;
        B.insert(num);
    }
    
    for(auto it = A.begin(); it != A.end(); it++) {
        if(B.find(*it) == B.end()) {
            ans++;
        }
    }
    
    for(auto it = B.begin(); it != B.end(); it++) {
        if(A.find(*it) == A.end()) {
            ans++;
        }
    }
    
    cout << ans;
    
    return 0;
}