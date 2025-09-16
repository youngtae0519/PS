#include <bits/stdc++.h>

using namespace std;

int a1, a0, c, n0;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> a1 >> a0 >> c >> n0;

  if(a1 == c) {
    if(a0 <= 0) {
      cout << "1\n";
    } else {
      cout << "0\n";
    }
  } else if(a1 < c) {
    if(n0 >= a0 / (c - a1)) {
      cout << "1\n";
    } else {
      cout << "0\n";
    }
  } else {
    cout << "0\n";
  }

  return 0;
}