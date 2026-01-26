#include <bits/stdc++.h>

using namespace std;

int N;
int* arr;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    arr = new int[N + 1];
    
    arr[0] = 1;
    arr[1] = 1;
    for(int i = 2; i <= N; i++) {
        arr[i] = arr[i - 1] * i;
    }
    
    cout << arr[N];
    
    return 0;
}