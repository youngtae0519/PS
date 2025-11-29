#include <bits/stdc++.h>

using namespace std;

int T;
long long int n;

int isPrime(long long int n) {
    for(long long int i = 3; i * i <= n; i += 2) {
        if(n % i == 0) {
            return -1;
        }
    }
    return n;
}

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0); 
    
    cin >> T;
    
    for(int i = 0; i < T; i++) {
        cin >> n;
        if(n <= 2) {
            cout << "2\n";
        } else {
            if(n % 2 == 0) {
                n++;
            }
            while(true) {
                if(isPrime(n) != -1) {
                    break;
                }
                n += 2;
            }
            cout << n << "\n";
        }   
    }
    
    return 0;
}