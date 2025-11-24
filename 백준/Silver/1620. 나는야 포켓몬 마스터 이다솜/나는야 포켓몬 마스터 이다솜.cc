#include <bits/stdc++.h>

using namespace std;

int N, M;
string name, tmp;
map<string, int> m1;
map<int, string> m2;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N >> M;
    
    for(int i = 0; i < N; i++) {
        cin >> name;
        m1[name] = i + 1;
        m2[i + 1] = name;
    }
    
    for(int i = 0; i < M; i++) {
        cin >> tmp;
        if(isdigit(tmp[0])) {
            cout << m2[stoi(tmp)] << "\n";
        } else {
            cout << m1[tmp] << "\n";
        }
    }
    
    return 0;
}