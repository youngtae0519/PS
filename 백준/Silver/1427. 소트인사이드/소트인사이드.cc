#include <bits/stdc++.h>

using namespace std;

int N;
vector<int> v;

bool desc(int a, int b) {
    return a > b;
}

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    while(N > 0) {
        v.push_back(N % 10);
        N /= 10;
    }
    
    sort(v.begin(), v.end(), desc);
    for(auto it = v.begin(); it != v.end(); it++) {
        cout << *it;
    }
    
    return 0;
}