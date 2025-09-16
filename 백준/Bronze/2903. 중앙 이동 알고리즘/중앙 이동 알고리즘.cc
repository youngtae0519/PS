#include <bits/stdc++.h>

using namespace std;

int N;
// arr[i] : i번째 과정 후 정사각형 한 변의 점의 개수
int arr[16];

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N;
  arr[1] = 3;
  // i번째 과정에서 정사각형 한 변의 점의 개수(arr[i])는
  // 이전(i - 1번쨰) 과정에서 정사각형 한 변의 점의 개수(arr[i - 1])와
  // 이전 과정에서 정사각형 한 변의 각 점 사이에 새로운 점(arr[i - 1] + 1)의 합으로 이루어짐
  for(int i = 2; i <= N; i++) {
    arr[i] = arr[i - 1] + arr[i - 1] - 1;
  }

  // N번째 과정 후 정사각형 한 변의 점의 개수를 구한 후 그 수를 제곱
  cout << arr[N] * arr[N] << "\n";

  return 0;
}