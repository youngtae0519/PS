#include <bits/stdc++.h>

using namespace std;

int N, num;
int idx = 0;
int* arr;
set<int> s;
map<int, int> m;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    arr = new int[N];
    
    for(int i = 0; i < N; i++) {
        cin >> num;
        arr[i] = num;
        s.insert(num);
    }
    
    for(auto it = s.begin(); it != s.end(); it++) {
        m[*it] = idx;
        idx++;
    }
    
    for(int i = 0; i < N; i++) {
        cout << m[arr[i]] << " ";
    }

    
    return 0;
}