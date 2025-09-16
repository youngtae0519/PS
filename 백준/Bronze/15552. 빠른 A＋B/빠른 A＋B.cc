#include <iostream>

using namespace std;

int main() {
  // C++의 표춘 입출력 스트림(iostreams, cin, cout)과 C 언어의 표준 입출력 함수(stdio, scanf, printf)의 동기화 해제
  // 이걸 사용하면 scanf, printf 등 C 언어의 함수 사용하면 안됨(순서가 보장 안됨)
  // 대신 동기화가 비활성화되기 때문에 cin / cout이 더 빠르고 효율적으로 동작함
  ios::sync_with_stdio(false);

  // cin과 cout의 연결을 끊음
  // 기본적으로 cin은 입력받기 전에 cout의 버퍼를 비우도록(flash) 설정되어 있음
  // cin.tie(0)을 호출하면 cin이 cout을 자동으로 flash하는 동작을 비활성화시킴
  // 그래서 cin을 입력받을 때마다 cout을 비우는 오버헤드가 사라져 입출력 속도 향상
  cin.tie(0);

  int T, A, B;

  cin >> T;

  while(T--) {
    cin >> A >> B;
    
    // endl을 사용하면 std::flush를 호출해 출력 스트림 버퍼를 강제로 비움
    // 때문에 속도 향상을 위해 \n 사용
    cout << A + B << "\n";
  }

  return 0;
}