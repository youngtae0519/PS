#include <bits/stdc++.h>

using namespace std;

// cnt5 : 5kg 봉지 개수
// cnt3 : 3kg 봉지 개수
// rest : 5kg 봉지를 최대한 많이 쓰고 남은 설탕 무게
int N, cnt5, cnt3, rest;
int ans = INT32_MAX;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N;

  // 최대로 많이 쓸 수 있는 5Kg 봉지 개수를 구함
  cnt5 = N / 5;

  // 5kg 봉지 개수를 하나씩 줄이면서 봉지의 최소 개수를 구함
  while(cnt5 >= 0) {
    // 5kg 봉지를 사용하고 남은 설탕 무게 확인
    rest = N - (5 * cnt5);
    // 설탕의 무게가 3으로 나눠 떨어지면
    if(rest % 3 == 0) {
      // 3kg 봉지 개수를 구함
      cnt3 = rest / 3;
      // 이전 봉지의 개수와 비교해서 더 작은 값을 구함
      ans = min(ans, cnt5 + cnt3);
    }
    cnt5--;
  }

  // ans가 한번도 변하지 않으면 만들 수 없는 무게이므로 -1 출력
  if(ans == INT32_MAX) {
    ans = -1;
  }

  cout << ans << "\n";

  return 0;
}