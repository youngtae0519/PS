#include <bits/stdc++.h>

using namespace std;

int a, b, c, maxNum;
int sum = 0;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> a >> b >> c;

  maxNum = max(a, max(b, c));

  if(a + b + c - maxNum > maxNum) {
    cout << a + b + c << "\n";
  } else {
    cout << (a + b + c - maxNum) * 2 - 1 << "\n";
  }

  return 0;
}