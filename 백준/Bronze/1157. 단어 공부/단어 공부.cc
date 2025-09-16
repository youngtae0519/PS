#include <iostream>

using namespace std;

string s;
int arr[26];
int cnt = 0;
int num;
char ans;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> s;

  for(auto it = s.begin(); it != s.end(); it++) {
    num = toupper(*it) - 65;
    arr[num]++;
    if(arr[num] > cnt) {
      cnt = arr[num];
      ans = toupper(*it);
    } else if(arr[num] == cnt) {
      ans = '?';
    }
  }

  cout << ans << "\n";

  return 0;
}