#include <bits/stdc++.h>

using namespace std;

int N, k;
int* arr;

bool desc(int a, int b) {
    return a > b;
}

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N >> k;
    arr = new int[N];
    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    sort(arr, arr + N, desc);
    
    cout << arr[k - 1] << "\n";
    return 0;
}