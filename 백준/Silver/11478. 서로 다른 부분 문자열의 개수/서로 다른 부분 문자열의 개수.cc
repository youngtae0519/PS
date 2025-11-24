#include <bits/stdc++.h>

using namespace std;

string S, tmp;
set<string> s;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> S;
    
    for(int i = 1; i < S.length() + 1; i++) {
        for(int j = 0; j < S.length() - i + 1; j++) {
            tmp = S.substr(j, i);
            s.insert(tmp);
        }
    }
    
    cout << s.size();
    
    return 0;
}