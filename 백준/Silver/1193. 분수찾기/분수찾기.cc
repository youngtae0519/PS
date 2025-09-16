#include <bits/stdc++.h>

using namespace std;

int X;
int idx = 1;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> X;
  // 몇 번째 대각선에 있는지 확인
  while(true) {
    if(X - idx <= 0) {
      break;
    }
    X -= idx;
    idx++;
  }

  // 짝수번째 대각선이면
  if(idx % 2 == 0) {
    // 위에서 아래로 내려오는 방향
    cout << X << "/" << idx + 1 - X << "\n";
  } 
  // 홀수번째 대각선이면
  else {
    // 아래에서 위로 올라가는 방향
    cout << idx + 1 - X << "/" << X << "\n";
  }

  return 0;
}