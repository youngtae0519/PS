#include <bits/stdc++.h>

using namespace std;

int T, N, ans;
int prime[1'000'001];

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    for(int i = 2; i <= 1'000'001; i++) {
        if(prime[i] == 0) {
            prime[i] = 1;
            for(int j = i; j <= 1'000'001; j += i) {
                if(prime[j] == 0) {
                    prime[j] = 2;
                }
            }
        }
    }
    
    cin >> T;
    for(int i = 0; i < T; i++) {
        cin >> N;
        ans = 0;
        if(prime[N - 2] == 1) {
            ans++;
        }
        for(int j = 3; j <= N / 2; j += 2) {
            if(prime[j] == 1 && prime[N - j] == 1) {
                ans++;
            }
        }
        cout << ans << "\n";
    }
    
    return 0;
}