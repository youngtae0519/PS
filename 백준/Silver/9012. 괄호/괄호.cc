#include <bits/stdc++.h>

using namespace std;

int T;
string tmp;
stack<char> s;
bool wrong = false;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> T;
    
    while(T--) {
        cin >> tmp;
        stack<char> s;
        wrong = false;
        for(int i = 0; i < tmp.size(); i++) {
            if(tmp[i] == '(') {
                s.push(tmp[i]);
            } else {
                if(s.empty()) {
                    wrong = true;
                    break;
                }
                s.pop();
            }
        }
        if(wrong || !s.empty()) {
            cout << "NO" << "\n";
        } else {
            cout << "YES" << "\n";
        }
    }
    
    return 0;
}