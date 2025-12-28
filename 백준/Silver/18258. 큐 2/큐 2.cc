#include <bits/stdc++.h>

using namespace std;

int N, num;
string cmd;
deque<int> dq;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    while(N--) {
        cin >> cmd;
        if(cmd == "push") {
            cin >> num;
            dq.push_back(num);
        } else if(cmd == "pop") {
            if(dq.empty()) {
                cout << "-1\n";
            } else {
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        } else if(cmd == "size") {
            cout << dq.size() << "\n";
        } else if(cmd == "empty") {
            if(dq.empty()) {
                cout << "1\n";
            } else {
                cout << "0\n";
            }
        } else if(cmd == "front") {
            if(dq.empty()) {
                cout << "-1\n";
            } else {
                cout << dq.front() << "\n";
            }
        } else if(cmd == "back") {
            if(dq.empty()) {
                cout << "-1\n";
            } else {
                cout << dq.back() << "\n";
            }
        }
    }
    
    return 0;
}