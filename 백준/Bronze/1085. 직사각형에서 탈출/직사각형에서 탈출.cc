#include <bits/stdc++.h>

using namespace std;

int x, y, w, h, disX, disY;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> x >> y >> w >> h;

  disX = min(x, w - x);
  disY = min(y, h - y);

  cout << min(disX, disY) << "\n";

  return 0;
}