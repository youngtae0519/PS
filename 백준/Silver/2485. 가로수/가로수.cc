#include <bits/stdc++.h>

using namespace std;

int N, gap, ans;
int* arr;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    arr = new int[N];
    
    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    gap = arr[1] - arr[0];
    
    for(int i = 1; i < N - 1; i++) {
        for(int j = gap; j > 0; j--) {
            if((arr[i + 1] - arr[i]) % j == 0 && gap % j == 0) {
                gap = j;
                break;
            }
        }
    }
    
    for(int i = 0; i < N - 1; i++) {
        ans += ((arr[i + 1] - arr[i]) / gap) - 1;
    }
    
    cout << ans;
    
    return 0;
}