import sys

input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    S = input().rstrip()
    
    if S == 'end':
        break
    
    has_vowel = False
    for v in vowel:
        if v in S:
            has_vowel = True
            break
    
    if not has_vowel:
        print(f'<{S}> is not acceptable.')
    else:
        is_vowel = False
        is_constant = False
        
        cnt = 1
        if S[0] in vowel:
            is_vowel = True
        else:
            is_constant = True
            
        is_triple = False
        
        for i in range(1, len(S)):
            if S[i] in vowel:
                if is_vowel:
                    cnt += 1
                    if cnt == 3:
                        is_triple = True
                        break
                else:
                    cnt = 1
                    is_vowel = True
                    is_constant = False
            else:
                if is_constant:
                    cnt += 1
                    if cnt == 3:
                        is_triple = True
                        break
                else:
                    cnt = 1
                    is_vowel = False
                    is_constant = True
       
        if is_triple:
            print(f'<{S}> is not acceptable.')
        else:
            is_same = False
            for i in range(1, len(S)):
                if S[i] == S[i - 1]:
                    if S[i] != 'e' and S[i] != 'o':
                        is_same = True
                        break
                        
            if is_same:
                print(f'<{S}> is not acceptable.')
            else:
                print(f'<{S}> is acceptable.')