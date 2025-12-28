#include <bits/stdc++.h>

using namespace std;

int N, num;
int cur = 1;
stack<int> s;
string ans = "Nice";

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        while(true) {
            if(s.empty() || s.top() > cur) {
                break;
            }
            s.pop();
            cur++;
        }
        cin >> num;
        if(num == cur) {
            cur++;
        } else if(num > cur) {
            if(!s.empty() && s.top() < num) {
                ans = "Sad";
                break;
            }
            s.push(num);
        }   
    }
    
    cout << ans;
    
    return 0;
}