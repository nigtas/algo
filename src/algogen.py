from random import randint

def next_string(s):
    strip_zs = s.rstrip('z')
    if strip_zs:
        return strip_zs[:-1] + chr(ord(strip_zs[-1]) + 1) + 'a' * (len(s) - len(strip_zs))
    else:
        return 'a' * (len(s) + 1)

def genVertex(num):
	lst = []
	start = 'a'
	for _ in range(num):
		lst.append(start)
		start = next_string(start)
	return lst

def genPairs(list):
	lst = []
	for i in range(len(list)):
		for j in range(i+1, len(list)):
			lenght = randint(1, 10)
			if lenght > 0:
				lst.append((list[i], list[j], lenght))
	return lst

vertices = genVertex(201)
edges = genPairs(vertices)

f = open('data6.txt', 'w')

for vertex in vertices:
	f.write('%s ' % vertex)

f.write("\n")

for edge in edges:
	f.write('%s %s %d\n' % (edge))

f.close()