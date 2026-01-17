#include <bits/stdc++.h>

using namespace std;

int N, num, ans;
int* arr;
deque<int> d;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    arr = new int[N + 1];
    
    for(int i = 0; i < N; i++) {
        cin >> num;
        arr[i + 1] = num;
        d.push_back(i + 1);
    }
    
    while(N--) {
        ans = d.front();
        num = arr[ans];
        cout << ans << " ";
        d.pop_front();
        if(num > 0) {
            for(int i = 1; i < num; i++) {
                d.push_back(d.front());
                d.pop_front();
            }
        } else {
            num = -num;
            for(int i = 0; i < num; i++) {
                d.push_front(d.back());
                d.pop_back();
            }
        }
    }
    
    return 0;
}