from collections import defaultdict, deque

def checkBound(N, index):
	return  0 <= index < N

def makeGraph(n, inComing, outGoing):
	graph = defaultdict(list)
	
	for city in range(n):
		prv = city-1
		nxt = city+1
		if outGoing[city] == 'Y' and checkBound(n, nxt) and inComing[nxt] == 'Y':
			graph[city].append(nxt)
		if outGoing[city] == 'Y' and checkBound(n, prv) and inComing[prv] == 'Y':
			graph[city].append(prv)
	return graph

def bfs(graph, city, route):
	visited = set()
	queue = deque([city])
	visited.add(city)
	while queue:
		current = queue.popleft()
		for nxt in graph[current]:
			if nxt not in visited:
				visited.add(nxt)
				route[city][nxt] = 'Y'
				queue.append(nxt)
	
def solve(tc):
	n = int(input())
	inComing = input()
	outGoing = input()
	route = [ ['N' for _ in range(n)] for _ in range(n)]
	graph = makeGraph(n, inComing, outGoing)
	#print(graph)	
	for city in range(n):
		bfs(graph, city, route)

	for i in range(n):
		for j in range(n):
			if i == j: route[i][j] = 'Y'
				
				
	print("Case #%d: " % (tc+1))
	for i in route:
		print("".join(i))
		
for i in range(int(input())):
	
	solve(i)
