#include <iostream>

using namespace std;

int N;
string s;
int ans = 0;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> s;

  for(int i = 0; i < N; i++) {
    ans += int(s[i]) - 48;
  }

  cout << ans << '\n';

  return 0;
}