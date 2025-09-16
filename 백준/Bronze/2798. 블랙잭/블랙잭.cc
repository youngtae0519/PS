#include <bits/stdc++.h>

using namespace std;

int N, M;
int ans = 0, tmp = 0;
int* arr;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> M;

  arr = new int[N];

  for(int i = 0; i < N; i++) {
    cin >> arr[i];
  }

  for(int i = 0; i < N - 2; i++) {
    for(int j = i + 1; j < N - 1; j++) {
      for(int k = j + 1; k < N; k++) {
        tmp = arr[i] + arr[j] + arr[k];
        if(tmp > ans && tmp <= M) {
          ans = tmp;
        }
      }
    }
  }

  cout << ans << "\n";

  delete arr;

  return 0;
}