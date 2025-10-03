#include <bits/stdc++.h>

using namespace std;

int N, tmp;
// ans : 현재 숫자
// cnt : 현재 숫자에서 6이 연속으로 몇개 나오는지 확인
// num : 현재 숫자가 몇 번째로 작은 종말의 수인지 확인
int cnt = 0, num = 0, ans = 666;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);
  
  cin >> N;

  while(true) {
    tmp = ans;
    cnt = 0;
    // tmp의 각 자리가 6인지 아닌지 확인(1의 자리부터 확인)
    while(tmp > 0) {
      // tmp의 1의 자리가 6인지 확인
      if(tmp % 10 == 6) {
        cnt++;
        // 6이 연속해서 3개 나오면 num 증가
        // 1의 자리부터 확인하기 때문에 가장 작은 종말의 수부터 차례로 확인할 수 있음
        if(cnt == 3) {
          num++;
        }
      } 
      // 6이 아니면 cnt 0으로 설정
      else {
        cnt = 0;
      }
      // tmp를 10으로 나눈 몫으로 설정
      tmp /= 10;
    }
    // num이 입력받은 N과 같으면 break
    if(num == N) {
      break;
    }
    // 현재 숫자 1 증가
    ans++;
  }

  cout << ans << "\n";
  
  return 0;
}