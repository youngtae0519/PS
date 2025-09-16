#include <bits/stdc++.h>

using namespace std;

int x, y;
int totalX[1001], totalY[1001];

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  for(int i = 0; i < 3; i++) {
    cin >> x >> y;
    totalX[x]++;
    totalY[y]++;
  }

  for(int i = 1; i < 1001; i++) {
    if(totalX[i] == 1) {
      cout << i << " ";
      break;
    }
  }

  for(int i = 1; i < 1001; i++) {
    if(totalY[i] == 1) {
      cout << i << "\n";
      break;
    }
  }

  return 0;
}