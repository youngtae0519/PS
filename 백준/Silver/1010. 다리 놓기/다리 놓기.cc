#include <bits/stdc++.h>

using namespace std;

int T, N, M;
int** arr;

int cal(int a, int b) {
    if(arr[a][b] == 0) {
        arr[a][b] = cal(a - 1, b) + cal(a - 1, b - 1);
    }
    return arr[a][b];
}

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> T;
    arr = new int*[30];
    for(int i = 0; i < 30; i++) {
        arr[i] = new int[30];
    }
    for(int i = 1; i < 30; i++) {
        arr[i][0] = 1;
        arr[i][1] = i;
        arr[i][i] = 1;
    }
    
    while(T--) {
        cin >> N >> M;
        
        if(N == M) {
            cout << "1\n";
        } else {
            cout << cal(M - 1, N) + cal(M - 1, N - 1) << "\n";            
        }    
    }
    
    return 0;
}