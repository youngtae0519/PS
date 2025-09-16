#include <bits/stdc++.h>

using namespace std;

int N, num, ans;
bool isPrime;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  ans = 0;
  
  cin >> N;

  for(int i = 0; i < N; i++) {
    cin >> num;

    if(num < 2) {
      continue;
    }

    isPrime = true;
    for(int j = 2; j * j <= num; j++) {
      if(num % j == 0) {
        isPrime = false;
        break;
      }
    }

    if(isPrime) {
      ans++;
    }
  }

  cout << ans << "\n";

  return 0;
}