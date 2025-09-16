#include <bits/stdc++.h>

using namespace std;

long long n;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> n;

  // 1 : 최상단 길이
  // n * 2 : 좌우 세로 길이의 합
  // n - 1 : 최상단 & 최하단을 제외한 중간 가로 길이의 합
  // n : 최하단 길이
  cout << 1 + n * 2 + (n - 1) + n << "\n";

  return 0;
}