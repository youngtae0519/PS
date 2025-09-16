#include <iostream>

using namespace std;

string s;
string arr[] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
int idx = 0;
int ans = 0;
bool check;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> s;

  // idx가 입력받은 s의 길이보다 작으면 실행
  while(idx < s.length()) {
    // 초기 check 값을 false로 설정
    // s[idx]가 모든 arr[i][0]가 다르다고 가정
    check = false;
    // arr를 하나씩 탐색
    for(int i = 0; i < 8; i++) {
      if(s[idx] == arr[i][0]) {
        // s[idx] == arr[i][0]인 경우(첫 글자가 같은 경우)가 발견되면 check를 true로 변경
        check = true;
        // 첫 글자부터 마지막 글자까지 동일한지 확인
        for(int j = 1; j < arr[i].length(); j++) {
          // s의 길이를 넘어가거나 중간에 글자가 일치하지 않으면 check를 false로 변경
          if(idx + j > s.length() || s[idx + j] != arr[i][j]) {
            check = false;
            break;
          }
        }
        // 위 for문에서 check가 false로 바뀌지 않았다는 의미는 arr[i] 글자가 s[idx]부터 시작해서 포함되어 있다는 뜻
        if(check) {
          ans++;
          // 때문에 idx를 arr[i]의 길이만큼 증가
          idx += arr[i].length();
          // break문으로 각 arr 글자와 비교하는 반복문 탈출
          break;
        }
      }
    }
    // s[idx]가 모든 arr[i][0]과 다른 경우 ans와 idx를 1씩 증가
    if(!check) {
      ans++;
      idx++;
    }
  }

  cout << ans << "\n";

  return 0;
}