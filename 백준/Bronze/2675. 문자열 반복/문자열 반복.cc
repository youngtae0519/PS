#include <iostream>

using namespace std;

int T, R;
string S, ans;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> T;

  for(int tc = 0; tc < T; tc++) {
    cin >> R >> S;

    ans = "";

    for(int i = 0; i < S.length(); i++) {
      for(int j = 0; j < R; j++) {
        ans += S[i];
      }
    }

    cout << ans << '\n';
  }

  return 0;
}