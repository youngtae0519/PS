// bits/stdc++.h : c++에서 자주 사용하는 표준 헤더들을 모아놓음
#include <bits/stdc++.h>

using namespace std;

int B, len, num;
long long int ans;
string N;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> B;

  len = N.length() - 1;
  ans = 0;
  for(auto it = N.begin(); it != N.end(); it++) {
    // c++에서는 isdigit() 사용
    // isnumber 함수는 없음
    num = (isdigit(*it)) ? int(*it) - 48 : int(*it) - 55;
    ans += num * pow(B, len);
    len--;
  }

  cout << ans << "\n";

  return 0;
}