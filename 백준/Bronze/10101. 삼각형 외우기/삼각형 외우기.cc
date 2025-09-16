#include <bits/stdc++.h>

using namespace std;

int a, b, c;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> a >> b >> c;

  if(a + b + c != 180) {
    cout << "Error\n";
  } else if(a == b && b == c && a == c) {
    cout << "Equilateral\n";
  } else if(a != b && b != c && a != c) {
    cout << "Scalene\n";
  } else {
    cout << "Isosceles\n";
  }

  return 0;
}