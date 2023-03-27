# -*- coding: utf-8 -*-
from collections import deque

# 리스트로도 구현할 수 있지만 시간복잡도가 높아짐
# 큐를 구현하기 위해선 deque 라이브러리 사용하기
# deque 는 스택과 큐의 장점을 모두 가짐

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# deque 의 __str__() 도 구현되어 있음
print(queue)    
queue.reverse
print(queue)