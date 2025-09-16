#include <bits/stdc++.h>

using namespace std;

int a, b, c, maxNum;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  while(true) {
    cin >> a >> b >> c;

    if(a == 0) {
      break;
    }

    maxNum = max(a, max(b, c));

    if(maxNum >= a + b + c - maxNum) {
      cout << "Invalid\n";
    } else if(a == b && b == c && a == c) {
      cout << "Equilateral\n";
    } else if(a != b && b != c && a != c) {
      cout << "Scalene\n";
    } else {
      cout << "Isosceles\n";
    }
  }

  return 0;
}