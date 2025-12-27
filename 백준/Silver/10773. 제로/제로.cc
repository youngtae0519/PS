#include <bits/stdc++.h>

using namespace std;

int K, num, ans;
stack<int> s;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> K;
    
    for(int i = 0; i < K; i++) {
        cin >> num;
        if(num != 0) {
            s.push(num);
        } else {
            s.pop();
        }
    }
    
    while(!s.empty()) {
        ans += s.top();
        s.pop();
    }
    
    cout << ans;
    
    return 0;
}