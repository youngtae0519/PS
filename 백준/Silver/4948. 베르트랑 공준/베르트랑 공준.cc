#include <bits/stdc++.h>

using namespace std;

int n, ans;

bool isPrime(int x) {
    for(long long int i = 3; i * i <= x; i += 2) {
        if(x % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    while(true) {
        cin >> n;
        if(n == 0) {
            break;
        }
        
        ans = 0;
        if(n == 1) {
            cout << "1\n";
        } else {
            for(int i = n + 1; i <= 2 * n; i++) {
                if(i % 2 == 0) {
                    continue;
                }
                if(isPrime(i)) {
                    ans++;
                }
            }
            cout << ans << "\n";
        }
    }
    
    return 0;
}