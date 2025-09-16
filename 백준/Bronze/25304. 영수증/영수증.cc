#include <iostream>

using namespace std;

int main() {
  int X, N, a, b;
  int total = 0;
  string ans;

  cin >> X >> N;

  while(N--) {
    cin >> a >> b;
    total += a * b;
  }

  ans = (X == total) ? "Yes" : "No";

  cout << ans << endl;

  return 0;
}