#include <bits/stdc++.h>

using namespace std;

int M, N;

bool isPrime(int n) {
    for(long long int i = 3; i * i <= n; i += 2) {
        if(n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> M >> N;
    
    for(int i = M; i <= N; i++) {
        if(i == 2) {
            cout << "2\n";
            continue;
        }
        if(i % 2 == 0) {
            continue;
        }
        if(i >= 3 && isPrime(i)) {
            cout << i << "\n";
        }
    }
    
    return 0;
    
}