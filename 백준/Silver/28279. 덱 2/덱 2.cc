#include <bits/stdc++.h>

using namespace std;

int N, cmd, x;
deque<int> d;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    while(N--) {
        cin >> cmd;
        if(cmd == 1) {
            cin >> x;
            d.push_front(x);
        } else if(cmd == 2) {
            cin >> x;
            d.push_back(x);
        } else if(cmd == 3) {
            if(!d.empty()) {
                cout << d.front() << "\n";
                d.pop_front();
            } else {
                cout << "-1\n";
            }
        } else if(cmd == 4) {
            if(!d.empty()) {
                cout << d.back() << "\n";
                d.pop_back();
            } else {
                cout << "-1\n";
            }
        } else if(cmd == 5) {
            cout << d.size() << "\n";
        } else if(cmd == 6) {
            if(d.empty()) {
                cout << "1\n";
            } else {
                cout << "0\n";
            }
        } else if(cmd == 7) {
            if(!d.empty()) {
                cout << d.front() << "\n";
            } else {
                cout << "-1\n";
            }
        } else if(cmd == 8) {
            if(!d.empty()) {
                cout << d.back() << "\n";
            } else {
                cout << "-1\n";
            }
        }
    }
    
    return 0;
}