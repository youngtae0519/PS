#include <iostream>

using namespace std;

int N, ans;
string s;
// c : 직전 글자
char c;
// arr[i] == 0 : 해당 글자는 이전에 등장한 적 없음
// arr[i] == 1 : 해당 글자는 이전에 등장한 적 있음
int arr[26];

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N;
  ans = N;

  for(int i = 0; i < N; i++) {
    cin >> s;
    // arr 배열을 0으로 초기화
    fill(arr, arr + 26, 0);
    // s의 첫번째 글자로 c와 arr 값 설정
    c = s[0];
    arr[int(c) - 97] = 1;
    // 입력받은 s를 한 글자씩 탐색
    for(auto it = s.begin(); it != s.end(); it++) {
      // 현재 글자가 연속된 글자면 continue
      if(c == *it) {
        continue;
      }
      // 현재 글자가 연속되지 않은 새로운 글자이면서
      // 해당 글자에 대한 arr 값이 0이 아니면(이전에 이미 나왔던 글자면)
      // 정답 개수를 1 감소
      if(arr[int(*it) - 97] != 0) {
        ans--;
        break;
      }
      // 그 외의 경우
      // 즉, 현재 글자가 연속되지 않은 새로운 글자이면서
      // 해당 글자에 대한 arr 값이 0인 경우(최초로 등장한 경우)
      // arr 값을 1로 바꿔주고, c 값을 현재 글자로 변경
      arr[int(*it) - 97] = 1;
      c = *it;
    }
  }

  cout << ans << "\n";

  return 0;
}