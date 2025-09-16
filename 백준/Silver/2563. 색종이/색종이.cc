#include <iostream>

using namespace std;

int n, row, col, ans;
int** arr;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  arr = new int*[100];
  for(int i = 0; i < 100; i++) {
    arr[i] = new int[100];
    fill_n(arr[i], 100, 0);
  }

  cin >> n;
  for(int i = 0; i < n; i++) {
    cin >> col >> row;
    for(int y = 0; y < 10; y++) {
      for(int x = 0; x < 10; x++) {
        arr[(100 - row) - y][col + x] = 1;
      }
    }
  }

  ans = 0;
  for(int i = 0; i < 100; i++) {
    for(int j = 0; j < 100; j++) {
      ans += arr[i][j];
    }
  }

  cout << ans << "\n";

  return 0;
}