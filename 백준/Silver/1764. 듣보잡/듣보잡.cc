#include <bits/stdc++.h>

using namespace std;

int N, M, cnt;
string name;
set<string> s;
vector<string> v;

bool compare(string a, string b) {
    return a < b;
}

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N >> M;
    
    for(int i = 0; i < N; i++) {
        cin >> name;
        s.insert(name);
    }
    
    for(int i = 0; i < M; i++) {
        cin >> name;
        if(s.find(name) != s.end()) {
            v.push_back(name);
            cnt++;
        }
    }
    
    sort(v.begin(), v.end(), compare);
    
    cout << cnt << "\n";
    for(auto it = v.begin(); it != v.end(); it++) {
        cout << *it << "\n";
    }
    
    return 0;
}