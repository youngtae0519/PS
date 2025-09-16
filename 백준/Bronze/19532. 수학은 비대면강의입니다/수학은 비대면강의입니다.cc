#include <bits/stdc++.h>

using namespace std;

int a, b, c, d, e, f, x, y;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> a >> b >> c >> d >> e >> f;

  x = (c * e - f * b) / (a * e - d * b);
  if(b == 0) {
    y = (f - d * x) / e;
  } else {
    y = (c - a * x) / b;
  }

  cout << x << " " << y << "\n";

  return 0;
}