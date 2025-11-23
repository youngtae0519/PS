#include <bits/stdc++.h>

using namespace std;

int N, num;
int arr[10001];

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> num;
        arr[num]++;
    }
    
    for(int i = 0; i < 10001; i++) {
        if(arr[i] == 0) {
            continue;
        }
        for(int j = 0; j < arr[i]; j++) {
            cout << i << "\n";
        }
    }
    
    return 0;
}