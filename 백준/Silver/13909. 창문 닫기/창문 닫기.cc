#include <bits/stdc++.h>

using namespace std;

long long int N;
int ans = 0;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    for(long long int i = 1; i * i <= N; i++) {
        ans++;
    }
    
    cout << ans;
    
    return 0;
}