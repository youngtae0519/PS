#include <iostream>
#include <vector>

using namespace std;

int N, M, num;
// 2차원 배열 a, b 선언
int** a;
int** b;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> M;

  // 2차원 배열 중 행(row)만 먼저 선언
  a = new int*[N];
  b = new int*[N];

  // 각 row에 대해
  for(int i = 0; i < N; i++) {
    // 열(col)을 선언
    a[i] = new int[M];
    // col 선언 후 0으로 초기화
    fill_n(a[i], M, 0);
    for(int j = 0; j < M; j++) {
      // 숫자를 하나씩 입력받을 때마다 2차원 배열에 바로 저장
      cin >> a[i][j];
    }
  }

  for(int i = 0; i < N; i++) {
    b[i] = new int[M];
    fill_n(b[i], M, 0);
    for(int j = 0; j < M; j++) {
      cin >> b[i][j];
    }
  }

  for(int i = 0; i < N; i++) {
    for(int j = 0; j < M; j++) {
      cout << a[i][j] + b[i][j] << " ";
    }
    cout << "\n";
  }

  return 0;
}