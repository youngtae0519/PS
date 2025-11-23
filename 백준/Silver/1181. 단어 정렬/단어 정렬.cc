#include <bits/stdc++.h>

using namespace std;

struct compare {
    bool operator() (const string& a, const string& b) const {
        if(a.size() == b.size()) {
            return a < b;
        } else {
            return a.size() < b.size();
        }
    }
};

int N;
string tmp;
set<string, compare> s;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> tmp;
        s.insert(tmp);
    }
    
    for(auto it = s.begin(); it != s.end(); it++) {
        cout << *it << "\n";
    }
    
    return 0;
}