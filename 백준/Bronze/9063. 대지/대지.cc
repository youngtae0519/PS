#include <bits/stdc++.h>

using namespace std;

int n, x, y;
int minX = 10001, minY = 10001, maxX = -10001, maxY = -10001;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> n;

  // 입력받은 좌표 중에서 가장 큰 x, y와 가장 작은 x, y를 구함
  // 입력받은 좌표가 모두 포함되려면 입력받은 좌표로 만들 수 있는 가장 큰 사각형이 되어야 함
  for(int i = 0; i < n; i++) {
    cin >> x >> y;
    minX = min(x, minX);
    minY = min(y, minY);
    maxX = max(x, maxX);
    maxY = max(y, maxY);
  }

  cout << (maxX - minX) * (maxY - minY) << "\n";
  return 0;
}