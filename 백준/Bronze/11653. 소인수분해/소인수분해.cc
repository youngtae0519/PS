#include <bits/stdc++.h>

using namespace std;

int N;
vector<int> arr;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N;

  while(true) {
    if(N == 1) {
      break;
    }

    for(int i = 2; i <= N; i++) {
      if(N % i == 0) {
        arr.push_back(i);
        N /= i;
        break;
      }
    }
  }

  for(auto it = arr.begin(); it != arr.end(); it++) {
    cout << *it << "\n";
  }

  return 0;
}