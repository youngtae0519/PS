#include <bits/stdc++.h>

using namespace std;

int N, K, tmp;
queue<int> q;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N >> K;
    
    for(int i = 1; i <= N; i++) {
        q.push(i);
    }
    
    cout << "<";
    while(N--) {
        for(int i = 1; i < K; i++) {
            tmp = q.front();
            q.pop();
            q.push(tmp);
        }
        cout << q.front();
        if(N > 0) {
            cout << ", ";
        }
        q.pop();
    }
    cout << ">";
    
    return 0;
}