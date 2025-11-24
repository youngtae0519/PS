#include <bits/stdc++.h>

using namespace std;

struct compare {
    bool operator() (const string a, const string b) const {
        return a > b;
    }
};

int n;
string name, state;
map<string, bool, compare> m;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> n;
    
    for(int i = 0; i < n; i++) {
        cin >> name >> state;
        if(state == "enter") {
            m[name] = true;
        } else {
            m[name] = false;
        }
    }
    
    for(auto it = m.begin(); it != m.end(); it++) {
        if(it->second) {
            cout << it->first << "\n";
        }
    }
    
    return 0;
}