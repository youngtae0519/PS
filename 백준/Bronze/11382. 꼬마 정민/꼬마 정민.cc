#include <iostream>

using namespace std;

int main() {
  // c++에서 int는 4Byte(32bit)
  // int로는 문제에서 주어지는 10^12까지 커버하지 못함
  // 그래서 더 넓은 범위인 long long(8Byte = 64bit)으로 처리
  long long A, B, C; cin >> A >> B >> C;

  cout << A + B + C << endl;

  return 0;
}