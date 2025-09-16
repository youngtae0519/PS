#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int A, B;

  // 이번에 읽은 줄이 EOF(End Of File)인지 확인
  while(!(cin >> A >> B).eof()) {
    cout << A + B << "\n";
  }

  return 0;
}