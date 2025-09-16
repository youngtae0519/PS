#include <bits/stdc++.h>

using namespace std;

// cur : 현재 수(ans)의 분해합
int N, tmp, cur;
int ans = 1;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N;

  while(true) {
    // 현재 수가 입력받은 N과 같으면 0 출력
    // N 이상의 수는 N의 분해합이 될 수 없음
    if(ans == N) {
      ans = 0;
      break;
    }

    tmp = ans;
    // cur에 tmp(= ans) 대입
    cur = tmp;

    // tmp의 각 자리수를 cur에 더함
    while(tmp > 0) {
      cur += (tmp % 10);
      tmp /= 10;
    }

    // 분해합인 cur이 N과 같은지 확인
    if(cur == N) {
      break;
    }

    ans++;
  }

  cout << ans << "\n";

  return 0;
}