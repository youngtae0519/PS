#include <iostream>

using namespace std;

int main() {
  double A, B; cin >> A >> B;

  // 소수점 이하 10자리까지 표시
  cout.precision(10);

  // 실수를 고정소수점 형식으로 출력(1.23e+06 X)
  cout << fixed;
  
  cout << A / B << endl;

  return 0;
}