#include <bits/stdc++.h>

using namespace std;

int n, total;
vector<int> arr;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  while(true) {
    cin >> n;

    if(n == -1) {
      break;
    }

    total = 0;
    arr.clear();

    for(int i = 1; i < n; i++) {
      if(n % i == 0) {
        total += i;
        arr.push_back(i);
      }
    }

    if(total == n) {
      cout << n << " = ";
      for(int i = 0; i < arr.size(); i++) {
        cout << arr.at(i);
        if(i != arr.size() - 1) {
          cout << " + ";
        }
      }
    } else {
      cout << n << " is NOT perfect.";
    }
    
    cout << "\n";
  }

  return 0;
}