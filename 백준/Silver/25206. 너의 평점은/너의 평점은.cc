#include <iostream>
// stringstream을 사용하기 위한 헤더 선언
#include <sstream>
// map을 사용하기 위한 헤더 선언
#include <map>

using namespace std;

// grade : 각 과목별 등급
string s, name, grade;
// credit : 각 과목별 학점
double credit;
// credits : 학점 총합
double credits = 0;
// scores : (학점 * 과목평점)의 합
double scores = 0;
// map : key, value 쌍으로 이루어진 트리
// 선언 방법 : map<key type, value type> <name>
// 특징
// 1. 중복을 허용하지 않음
// 2. key 기준으로 오름차순 정렬
map<string, double> m;


int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  // map에 key, value 쌍 저장
  // m.insert({key, value})로도 저장 가능
  m["A+"] = 4.5;
  m["A0"] = 4.0;
  m["B+"] = 3.5;
  m["B0"] = 3.0;
  m["C+"] = 2.5;
  m["C0"] = 2.0;
  m["D+"] = 1.5;
  m["D0"] = 1.0;
  m["F"] = 0.0;

  for(int i = 0; i < 20; i++) {
    // 공백을 포함한 문자열을 받기 위해 getline 함수 사용
    getline(cin, s);
    // stringstream : 문자열을 공백을 기준으로 분리
    stringstream ss(s);
    // 분리된 문자열을 각각 새로운 문자열에 저장
    ss >> name >> credit >> grade;
    if(grade == "P") {
      continue;
    }
    credits += credit;
    // m[key]로 해당 value 값에 접근 가능
    scores += m[grade] * credit;
  }

  cout << scores / credits << "\n";

  return 0;
}