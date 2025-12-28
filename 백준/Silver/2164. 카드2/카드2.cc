#include <bits/stdc++.h>

using namespace std;

int N, tmp;
queue<int> q;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    for(int i = 1; i <= N; i++) {
        q.push(i);
    }
    
    while(true) {
        if(q.size() == 1) {
            break;
        }
        q.pop();
        
        if(q.size() == 1) {
            break;
        }
        tmp = q.front();
        q.pop();
        q.push(tmp);
    }
    
    cout << q.front();
    
    return 0;
}