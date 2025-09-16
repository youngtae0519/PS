#include <iostream>
#include <ctype.h>

using namespace std;

char c;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> c;

  cout << toascii(c) << '\n';

  return 0;
}