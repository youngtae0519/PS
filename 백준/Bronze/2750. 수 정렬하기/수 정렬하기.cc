#include <bits/stdc++.h>

using namespace std;

int N;
int* arr;

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    arr = new int[N];
    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    sort(arr, arr + N);
    for(int i = 0; i < N; i++) {
        cout << arr[i] << "\n";
    }
    return 0;
}