# -*- coding: utf-8 -*-
from collections import deque

# ����Ʈ�ε� ������ �� ������ �ð����⵵�� ������
# ť�� �����ϱ� ���ؼ� deque ���̺귯�� ����ϱ�
# deque �� ���ð� ť�� ������ ��� ����

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# deque �� __str__() �� �����Ǿ� ����
print(queue)    
queue.reverse
print(queue)