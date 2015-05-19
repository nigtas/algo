import time
import random

#O(V^2)
def dijksta(graph, src, goal):
	dist = {vertex: float('inf') if vertex != src else 0 for vertex in graph['vertices']}
	route = {vertex: '' for vertex in graph['vertices']}
	neighbours = {vertex: set() for vertex in graph['vertices']}
	q = graph['vertices'].copy()

	for start, end, cost in graph['edges']:
		neighbours[start].add((end, cost))
		neighbours[end].add((start,cost))

	while q:
		u = min(q, key=lambda vertex: dist[vertex])
		# print(u)
		# print(dist)
		q.remove(u)
		if u == goal:
			break;
		for v, cost in neighbours[u]:
			alt = dist[u] + cost
			if alt < dist[v]:
				dist[v] = alt
				route[v] = u
		# print(route)
	lst = []
	for v in graph['vertices']:
		lst.append(dist[v])
	# print(lst)
	# print(route)
	return route

def findVerticesWithOddDegree(vertices, edges):
	degree = {vertex: 0 for vertex in graph['vertices']}
	lst = []

	for v in vertices:
		for e in edges:
			if e.count(v) == 1 and e.count(0) == 0:
				degree[v] = degree[v] + 1
		if degree[v] % 2:
			lst.append(v)
	return lst

def fleury(edges, vertices, start, end):
	# print(start)
	e = edges.copy()
	route = []
	s = start
	bridge = bool
	st = ''
	en = ''
	weight = 0
	route.append(s)
	# i = 0
	while len(e):
		# i = i+1
		print(len(e))
		# bridge = False
		for (st, en, weight) in e:
			# print(e)
			# print('a')
			# print('FLEURY VERTIVES ', vertices)
			# search for a start vertice
			if st != s and en != s:
				continue
			# print('aaa')
			# e.remove((st,en,weight))
			# valid = isValidEdge(st, en)
			# remove vertice if there are no edges
			# if not any(st in edge for edge in e):
			# 	vertices.remove(st)
			# if not any(en in edge for edge in e):
			# 	vertices.remove(en)
			# check if edge is a bridge
			# print(st)
			if st == s:
				valid = isValidEdge(st, en, e, vertices)
			elif en == s:
				valid = isValidEdge(en, st, e, vertices)
			# print(st)
			# print(valid)
			# print('b')
			# print('BRIDGE: ', bridge, st, en)
			# if bridge:
				# e.append((st,en,weight))  # add this edge back and try another
				# add back vertices
				# if not st in vertices:
				# 	vertices.append(st)
				# if not en in vertices:
				# 	vertices.append(en)
			if valid:
				# print(neighbours)
				# neighbours[st].remove((en, weight))
				# neighbours[en].remove((st, weight))
				e.remove((st,en,weight))
				if s == st:
					route.append(en)
					s = en
					if not any(st in edge for edge in e):
						vertices.remove(st)
					if not any(en in edge for edge in e):
						vertices.remove(en)
				elif s == en:
					route.append(st)
					s = st
					if not any(st in edge for edge in e):
						vertices.remove(st)
					if not any(en in edge for edge in e):
						vertices.remove(en)
				else:
					print('bad one')
				break  # this edge is good, add vertice to the route, break the for loop 
		# choose bridge if no other options
			# print('c')
		# if bridge:
		# 	if s == st:
		# 		e.remove((st,en,weight))
		# 		route.append(en)
		# 		s = en
		# 		if not any(st in edge for edge in e):
		# 			vertices.remove(st)
		# 		if not any(en in edge for edge in e):
		# 			vertices.remove(en)
		# 	elif s == en:
		# 		e.remove((st,en,weight))
		# 		route.append(st)
		# 		s = st
		# 		if not any(st in edge for edge in e):
		# 			vertices.remove(st)
		# 		if not any(en in edge for edge in e):
		# 			vertices.remove(en)
		# 	else:
		# 		print('bad two')
		# print('d')
	print(route) 


def isValidEdge(start, end, edges, vertices):
	# print(neighbours)
	# print('EDGES: ', start, end)
	# The only adjacent vertex for start
	# count = len(neighbours[start])
	count = 0
	for (s, e, w) in edges:
		if s== start or e == start:
			count = count + 1
	# for (neighbour,weight) in neighbours[start]:
	# 	if st == start or en == start:
	# 		count = count + 1
	# print('NEIGHBOURS', count)

	if count == 1:
		return True
	# Check if a bridge
	visited = {vertex: False for vertex in vertices}
	# print('NEIGHBOURS LENGHT: ', neighbours)
	count1 = dfsCount(start, visited, edges)
	# print('count 1 ', edges)
	# weight = 0
	# for (en, w) in neighbours[start]:
	# 	if en == end:
	# 		neighbours[start].remove((en, w)) 
	# 		weight = w
	# 		break;
	for (s, e, w) in edges:
		if s == start and e == end:
			edges.remove((s, e, w))
			weight = w
			break
		if s == end and e == start:
			edges.remove((s, e, w))
			weight = w
			break
	# print('NEIGHBOURS LENGHT: ', neighbours)
	visited = {vertex: False for vertex in vertices}
	# print('count 2 ', edges)
	count2 = dfsCount(start, visited, edges)

	# neighbours[start].add((end, weight))
	edges.append((s, e, w))
	# print(count1, count2, start, end)
	# print(count1, count2)
	# print(neighbours)
	
	return not(count1 > count2)




def dfsCount(start, visited, edges):
	visited[start] = True
	count = 1

	for (s, e, w) in edges:
		if s == start:
			if not visited[e]:
				count = count + dfsCount(e, visited, edges)
		if e == start:
			if not visited[s]:
				count = count + dfsCount(s, visited, edges)
		# if not visited[neighbour]:
		# 	count = count + dfsCount(neighbour, visited, neighbours)

	return count




def isConnected(vertices, edges):
	result = []
	nodes = set(vertices)

	while nodes:
		print('here')
		n = nodes.pop()
		group = {n}
		queue = [n]
		while queue:
			print('blabla')
			n = queue.pop(0)
			neighbours = [edge for edge in edges if n in edge]
			for el in group:
				if el != n:
					neighbours = [edge for edge in neighbours if el not in edge]
			for (src, dst, val) in neighbours:
				if src != n:
					nodes.difference_update(src)
					group.update(src)
					if src not in queue:
						queue.extend(src)
				else:
					nodes.difference_update(dst)
					group.update(dst)
					if dst not in queue:
						queue.extend(dst)
		result.append(group)
	return len(result) == 1


f = open('data6.txt', 'r')

vertices = f.readline().split()

lines = f.readlines()
edges = []
for line in lines:
	src, dst, cost = line.strip().split()
	edges.append((src,dst,int(cost)))

f.close()


graph = {
	'vertices': vertices,
	'edges': edges
}
# neighbours = {vertex: set() for vertex in graph['vertices']}


# for st, end, cost in edges:
# 	neighbours[st].add((end, cost))
# 	neighbours[end].add((st, cost))

# print(neighbours)
# print(edges)

startTime = time.clock()
oddDegreeVertices = findVerticesWithOddDegree(vertices, edges)
if len(oddDegreeVertices) == 2:
	print('odd: ', oddDegreeVertices[0], oddDegreeVertices[1])
	start = oddDegreeVertices[0]
	end = oddDegreeVertices[1]
	route = dijksta(graph, oddDegreeVertices[0], oddDegreeVertices[1])
	# print(route)
	while route[end] != '':
		start = end
		end = route[end]
		for (x,y,z) in edges:
			if x == end and y == start:
				# print(neighbours)
				edges.append((end, start, z))
				# neighbours[end].add((start, z))
				# neighbours[start].add((end, z))
				# print(neighbours)
				break
			if x == start and y == end:
				# print(neighbours)
				edges.append((start, end, z))
				# neighbours[start].add((end, z))
				# neighbours[end].add((start, z))
				# print(neighbours)
				break
	# print(edges)
	if len(findVerticesWithOddDegree(vertices, edges)) > 0:
		print('Something went wrong!!', findVerticesWithOddDegree(vertices, edges))
	# print('EDGES: ', edges, oddDegreeVertices, vertices)
	fleury(edges, vertices, oddDegreeVertices[0], oddDegreeVertices[1])

elif len(oddDegreeVertices) > 2:
	print('There are more than 2 vertices with odd degrees!')
else:
	print('There are vertices with odd degrees: ', len(oddDegreeVertices))
	fleury(edges, vertices, random.choice(vertices), random.choice(vertices))
elapsed = (time.clock() - startTime)
print(elapsed)

# times = 1

# sum = 0
# for x in range(times):
# 	start = time.clock()
# 	print(dijksta(graph, 'a', 'd'))
# 	elapsed = (time.clock() - start)
# 	sum += elapsed
# print(sum/times)

