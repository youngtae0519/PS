#include <bits/stdc++.h>

using namespace std;

long long int N;
int ans = 1;
int idx = 1;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N;

  // 벌집 정중앙이 아닐 경우
  if(N > 1) {
    N--;
    // 한 겹씩 확인
    while(true) {
      ans++;
      // 한 겹 커질때마다 6의 배수로 방의 개수 증가
      if(N - (6 * idx) <= 0) {
        break;
      }
      N -= 6 * idx;
      idx++;
    }
  }

  cout << ans << "\n";

  return 0;
}