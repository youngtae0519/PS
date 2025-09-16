#include <iostream>

using namespace std;

string S;
int ans[26];

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> S;

  for(int i = 0; i < 26; i++) {
    ans[i] = -1;
  }
  for(int i = 0; i < S.length(); i++) {
    if(ans[int(S[i]) - 97] == -1) {
      ans[int(S[i]) - 97] = i;
    }
  }

  for(int i = 0; i < 26; i++) {
    cout << ans[i] << ' ';
  }

  return 0;
}