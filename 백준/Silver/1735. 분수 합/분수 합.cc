#include <bits/stdc++.h>

using namespace std;

int a1, a2, b1, b2, bunja, bunmo, start;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> a1 >> b1;
    cin >> a2 >> b2;
    
    bunmo = b1 * b2;
    bunja = a1 * b2 + a2 * b1;
    start = min(bunmo, bunja) / 2;
    
    for(int i = start; i > 1; i--) {
        if(bunmo % i == 0 && bunja % i == 0) {
            bunmo /= i;
            bunja /= i;
        }
    }
    
    cout << bunja << " " << bunmo;
    
    return 0;
}