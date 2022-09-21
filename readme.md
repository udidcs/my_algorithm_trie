1. 자모음 두벌식 유니코드 테이블 

cho = [chr(i) for i in range(0x1100, 0x1113)]

jung = [chr(i) for i in range(0x1161, 0x1176)]

jong = [''] + [chr(i) for i in range(0x11A8, 0x11C3)]

2. 자모음 두벌식 유니코드 -> 초성, 중성, 종성의 유니코드로 변환

print(cho[b//588])

print(jung[b//28%21])

print(jong[b%28])

3. 초성, 중성, 종성 유니코드 -> 음절 복원

print(chr(b//588*588+b//28%21*28+b%28 + ord('가')))

4. 트라이 자료구조

add, getallwords, findnode

add를 통해 단어를 트라이에 저장

findnode를 통해 일부 단어를 전달해주고 그 깊이 까지 들어가 해당 딕셔너리(노드)

getallwords를 통해 모든 단어 찾기
