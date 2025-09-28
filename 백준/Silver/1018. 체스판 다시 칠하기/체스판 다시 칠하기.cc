#include <bits/stdc++.h>

using namespace std;

// tmp[8][8] : 만들고자하는 8 x 8 모양의 체스판
// **arr : 2차원 배열 초기화
int N, M, tmp[8][8], **arr, cnt0, cnt1;
string s;
int row = 0, col = 0, ans = INT_MAX;


int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> M;

  // 2차원 배열 동적 할당
  int** arr = new int*[N];
  for(int i = 0; i < N; i++) {
    arr[i] = new int[M];
  }

  // 1 : W, 0 : B로 치환해서 만들고자하는 8 x 8 모양의 체스판 생성
  // (첫 줄 기준) 1 0 1 0 1 0 1 0 / 0 1 0 1 0 1 0 1 두 경우를 모두 만들지 않는 이유
  // 두 경우는 서로 반대이기 때문에 나중에 비교할 때 같다(==) / 다르다(!=) 만 바꿔서 비교해주면 됨
  // 그래서 일단 tmp 배열은 0(B)가 시작인 2차원 배열로 생성
  for(int i = 0; i < 8; i++) {
    for(int j = 0; j < 8; j++) {
      tmp[i][j] = (i + j) % 2;
    }
  }

  for(int i = 0; i < N; i++) {
    cin >> s;
    for(int j = 0; j < M; j++) {
      if(s[j] == 'W') {
        arr[i][j] = 1;
      } else {
        arr[i][j] = 0;
      }
    }
  }

  while(true) {
    // cnt0 : 배열의 시작 위치가 0(B)일 떄 바꿔야 할 정사각형 개수
    // cnt1 : 배열의 시작 위치가 1(W)일 떄 바꿔야 할 정사각형 개수
    cnt0 = 0;
    cnt1 = 0;
    for(int i = 0; i < 8; i++) {
      for(int j = 0; j < 8; j++) {
        if(tmp[i][j] != arr[row + i][col + j]) {
          cnt0++;
        } else {
          cnt1++;
        }
      }
    }
    // 이전 위치 기준 바꿔야할 최소 개수 & 현재 위치 기준으로 어떤 색깔로 시작하는 체스판을 만드는게 더 적게 바꾸는지 확인
    ans = min(ans, min(cnt0, cnt1));
    // 입력받은 배열에서 확인할 수 있는 마지막 위치인지 확인
    if(row == N - 8 && col == M - 8) {
      break;
    }
    // 아니면 col 1 증가
    if(col < M - 8) {
      col++;
    }
    // 확인할 수 있는 마지막 col이면 row 1 증가 & col 0으로 설정
    else {
      row++;
      col = 0;
    }
  }

  cout << ans << "\n";

  return 0;
}