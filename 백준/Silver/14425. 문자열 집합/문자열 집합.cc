#include <bits/stdc++.h>

using namespace std;

int N, M;
int ans = 0;
string tmp;
set<string> s;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N >> M;
    
    for(int i = 0; i < N; i++) {
        cin >> tmp;
        s.insert(tmp);
    }
    
    for(int i = 0; i < M; i++) {
        cin >> tmp;
        if(s.find(tmp) != s.end()) {
            ans++;
        }
    }
    
    cout << ans << "\n";
    
    return 0;
}