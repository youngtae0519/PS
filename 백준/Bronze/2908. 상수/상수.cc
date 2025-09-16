#include <iostream>

using namespace std;

int A, B;
int a = 0;
int b = 0;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> A >> B;

  for(int i = 0; i < 3; i++) {
    a *= 10;
    a += (A % 10);
    A /= 10;

    b *= 10;
    b += (B % 10);
    B /= 10;
  }

  cout << max(a, b) << '\n';

  return 0;
}