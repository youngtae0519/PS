#include <bits/stdc++.h>

using namespace std;

int N, x, y;
int** arr;

bool compare(int a[2], int b[2]) {
    if(a[1] == b[1]) {
        return a[0] < b[0];
    } else {
        return a[1] < b[1];
    }
}

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    arr = new int*[N];
    for(int i = 0; i < N; i++) {
        arr[i] = new int[2];
    }
    
    for(int i = 0; i < N; i++) {
        cin >> x >> y;
        arr[i][0] = x;
        arr[i][1] = y;
    }
    
    sort(arr, arr + N, compare);
    
    for(int i = 0; i < N; i++) {
        cout << arr[i][0] << " " << arr[i][1] << "\n";
    }
    
    return 0;
}