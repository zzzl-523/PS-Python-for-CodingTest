# 최소 며칠이 걸리는지 구해야 하므로 BFS (최단거리)

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]

def bfs(graph, start, visited):
    queue = deque(graph[start])
    tomato_list = queue.popleft()

    