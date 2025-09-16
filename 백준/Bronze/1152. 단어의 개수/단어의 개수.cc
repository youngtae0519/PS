#include <iostream>

using namespace std;

string s;
bool check = false;
int ans = 0;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  // getline : 공백을 포함한 문자열 받기
  getline(cin, s);

  // 공백을 기준으로 단어 구분
  for(int i = 0; i < s.length(); i++) {
    // 현재 공백 이전에 단어가 있는지 없는지 확인
    if(s[i] == ' ' && check) {
      ans++;
      check = false;
    } else if(s[i] != ' ') {
      check = true;
    }
  }

  // 공백을 만날때마다 단어 수를 증가시키기 때문에 맨 마지막 단어가 포함 안될수도 있음
  // 이러한 경우를 대비해서 마지막 단어만 한번 더 확인
  if(check) {
    ans++;
  }

  cout << ans << '\n';

  return 0;
}