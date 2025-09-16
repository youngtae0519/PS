#include <bits/stdc++.h>

using namespace std;

long long int N;
int B;
map<int, char> m;
stack<char> s;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> B;

  for(int i = 0; i < 10; i++) {
    m[i] = char(i + '0');
  }

  for(int i = 10; i < 36; i++) {
    m[i] = char(i + '7');
  }

  while(N > 0) {
    s.push(m[N % B]);
    N = N / B;
  }

  while(!s.empty()) {
    cout << s.top();
    s.pop();
  }

  cout << "\n";

  return 0;
}