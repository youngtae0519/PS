#include <bits/stdc++.h>

using namespace std;

int currentHP, currentTime, cnt;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    currentHP = health;
    
    for(auto it = attacks.begin(); it != attacks.end(); it++) {
        cnt = it[0][0] - currentTime - 1;
        currentHP += bandage[1] * cnt;
        if(cnt >= bandage[0]) {
            currentHP += bandage[2] * (cnt / bandage[0]);
        }
        if(currentHP > health) {
            currentHP = health;
        }
        currentHP -= it[0][1];
        if(currentHP <= 0) {
            return -1;
        }
        currentTime = it[0][0];
    }
    
    return currentHP;
}