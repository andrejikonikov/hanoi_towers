class Tower:
	def __init__(self, disks, name):
		self.disks = disks
		self.name = name

def num(s):
	try:
		return int(s)
	except ValueError:
		return str(s)

def print_state(s):
	print s, a.name,a.disks, b.name,b.disks, c.name,c.disks

def hb(x,y,z,n):
	global counter
	if n > 0:
		hb(x,z,y,n - 1)
		counter += 1
		disk = x.disks.pop()
		z.disks.append(disk)
		print counter, "disk", disk, "moved from", x.name, "to", z.name
		print_state("state: ")	
		print
		hb(y,x,z,n-1)

def initiate_towers(n):
	arr = []
	for i in range(1, n + 1):
		arr.append((n + 1) - i)
	global a
	a = Tower(arr, "A")
	global b 
	b = Tower([], "B")
	global c
	c = Tower([], "C")
	print_state("initial state:")
	hb(a, b, c, n)

counter = 0
while True :

	n = raw_input("insert number of disks, or type quit")
	temp = num(n)

	if type(temp) is int and temp < 11 and temp > 0:
		print "insered: ", temp
		initiate_towers(temp)
		break
	else:
		if type(temp) is str:
			if temp == "quit":
				break
		print("bad input!!!")