#include <iostream>

using namespace std;

int main() {
  string id; cin >> id;

  // ??! 이걸 그대로 출력하면 Trigraph 오류 발생
  // Trigraph(삼중자) 오류 : C 언어에서 3개의 연속된 문자를 하나의 다른 문자로 변경하는 것(??! -> |)
  // 그래서 이 오류를 해결하려면 문자열 중간에 \(역슬래시)를 넣어주면 됨
  cout << id + "?\?!" << endl;

  return 0;
}