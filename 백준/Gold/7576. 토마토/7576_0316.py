from sys import stdin
from collections import deque
input = stdin.readline
que = deque()
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
