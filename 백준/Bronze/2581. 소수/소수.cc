#include <bits/stdc++.h>

using namespace std;

int N, M, total, minPrime;
bool isPrime;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  total = 0, minPrime = -1;

  cin >> N >> M;

  for(int i = N; i <= M; i++) {
    if(i == 1) {
      continue;;
    }

    isPrime = true;
    for(int j = 2; j * j <= i; j++) {
      if(i % j == 0) {
        isPrime = false;
        break;
      } 
    }

    if(isPrime) {
      total += i;
      if(minPrime == -1) {
        minPrime = i;
      }
    }
  }

  if(minPrime == -1) {
    cout << -1 << "\n";
  } else {
    cout << total << "\n" << minPrime << "\n";
  }

  return 0;
}