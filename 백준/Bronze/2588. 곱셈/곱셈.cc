#include <iostream>

using namespace std;

int main() {
  int a, b; cin >> a >> b;
  int total = a * b;

  cout << a * (b % 10) << endl;
  b = b / 10;
  cout << a * (b % 10) << endl;
  b = b / 10;
  cout << a * (b % 10) << endl;

  cout << total << endl;

  return 0;
}