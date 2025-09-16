#include <bits/stdc++.h>

using namespace std;

// day : 달팽이가 하루에 올라갈 수 있는 높이(올라간 높이 - 내려간 높이)
// lastV : 도착 지점 직전에 달팽이가 있어야 할 최소 높이(lastV 높이 이상에 위치할 경우 하루만 더 올라가면 도착)
int A, B, V, day, lastV, ans;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> A >> B >> V;

  if(A == V) {
    ans = 1;
  } else {
    day = A - B;
    lastV = V - A;

    // day로 lastV까지 얼마나 걸리는지 계산
    ans = lastV / day;
    
    // 나머지가 0이 아닌 경우 하루를 더 소비
    if(lastV % day != 0) {
      ans++;
    }

    // lastV 이상에서 도착 지점까지 올라가는데 하루 더 소비
    ans++;
  }

  cout << ans << "\n";

  return 0;
}