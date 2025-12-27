#include <bits/stdc++.h>

using namespace std;

int N, a, b;
stack<int> s;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> a;
        if(a == 1) {
            cin >> b;
            s.push(b);
        } else if(a == 2) {
            if(s.empty()) {
                cout << -1 << "\n";
            } else {
                cout << s.top() << "\n";
                s.pop();
            }
        } else if(a == 3) {
            cout << s.size() << "\n";
        } else if(a == 4) {
            if(s.empty()) {
                cout << 1 << "\n";
            } else {
                cout << 0 << "\n";
            }
        } else if(a == 5) {
            if(s.empty()) {
                cout << -1 << "\n";
            } else {
                cout << s.top() << "\n";
            }
        }
        
    }
    
    return 0;
}