#include <bits/stdc++.h>

using namespace std;

int N, num, M;
int* dat;
deque<int> dq;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    dat = new int[N];
    
    for(int i = 0; i < N; i++) {
        cin >> num;
        dat[i] = num;
    }
    
    for(int i = 0; i < N; i++) {
        cin >> num;
        if(dat[i] == 0) {
            dq.push_back(num);
        }
    }
    
    cin >> M;
    
    for(int i = 0; i < M; i++) {
        cin >> num;
        dq.push_front(num);
        cout << dq.back() << " ";
        dq.pop_back();
    }
    
    return 0;
}