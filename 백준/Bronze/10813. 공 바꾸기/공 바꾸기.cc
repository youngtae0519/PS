#include <iostream>
#include <vector>

using namespace std;

int N, M, i, j, tmp;
vector<int> v;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> M;

  v.resize(N);
  for(int i = 0; i < N; i++) {
    v[i] = i + 1;
  }

  for(int p = 0; p < M; p++) {
    cin >> i >> j;
    tmp = v[i - 1];
    v[i - 1] = v[j - 1];
    v[j - 1] = tmp;
  }

  for(auto it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
  }

  return 0;
}