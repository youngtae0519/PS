#include <bits/stdc++.h>

using namespace std;

int N, M, num;
map<int, int> m;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> num;
        m[num] = 1;
    }
    
    cin >> M;
    
    for(int i = 0; i < M; i++) {
        cin >> num;
        if(m[num] == 1) {
            cout << "1 ";
        } else {
            cout << "0 ";
        }
    }
    
    return 0;
}