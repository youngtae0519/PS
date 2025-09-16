#include <iostream>

using namespace std;

string s;
int len, head, tail;
int ans = 1;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> s;

  head = 0;
  tail = s.length() - 1;

  while(true) {
    if(s[head] != s[tail]) {
      ans = 0;
      break;
    }
    head++;
    tail--;
    if(head >= tail) {
      break;
    }
  }

  cout << ans << "\n";

  return 0;
}