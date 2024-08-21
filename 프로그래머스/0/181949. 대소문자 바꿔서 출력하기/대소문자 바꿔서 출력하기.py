str = input()

answer = []
for s in str:
    if ord(s) < 97: # chr(97)은 s
        answer.append(s.lower())
    else:
        answer.append(s.upper())
print(''.join(answer))