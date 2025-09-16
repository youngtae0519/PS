#include <iostream>

using namespace std;

string s;
int arr[26];
int ans = 0;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  arr[0] = 3;
  arr[1] = 3;
  arr[2] = 3;

  arr[3] = 4;
  arr[4] = 4;
  arr[5] = 4;

  arr[6] = 5;
  arr[7] = 5;
  arr[8] = 5;

  arr[9] = 6;
  arr[10] = 6;
  arr[11] = 6;

  arr[12] = 7;
  arr[13] = 7;
  arr[14] = 7;

  arr[15] = 8;
  arr[16] = 8;
  arr[17] = 8;
  arr[18] = 8;

  arr[19] = 9;
  arr[20] = 9;
  arr[21] = 9;

  arr[22] = 10;
  arr[23] = 10;
  arr[24] = 10;
  arr[25] = 10;

  cin >> s;

  for(auto it = s.begin(); it != s.end(); it++) {
    ans += arr[int(*it) - 65];
  }

  cout << ans << '\n';

  return 0;
}