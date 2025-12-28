#include <bits/stdc++.h>

using namespace std;

string tmp;
stack<char> s;
string ans = "yes";

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    while(true) {
        getline(cin, tmp);
        if(tmp[0] == '.') {
            break;
        }
        
        stack<char> s;
        ans = "yes";
        for(int i = 0; i < tmp.size(); i++) {
            if(tmp[i] == '(' || tmp[i] == '[') {
                s.push(tmp[i]);
            } else if(tmp[i] == ')') {
                if(s.empty() || s.top() != '(') {
                    ans = "no";
                    break;
                }
                s.pop();
            } else if(tmp[i] == ']') {
                if(s.empty() || s.top() != '[') {
                    ans = "no";
                    break;
                }
                s.pop();
            }
        }
        
        if(!s.empty()) {
            ans = "no";
        }
        
        cout << ans << "\n";
    }
    
    return 0;
}