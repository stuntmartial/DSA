n = int(input("Enter no of disks :"))
s = 'source '
d = 'destination '
h = 'helper '

def solve(s,d,h,n):

	if n == 0:
		return

	solve(s,h,d,(n-1))

	print("Move 1 disk from " , s , "to " ,d)

	solve(h,d,s,n-1)

solve(s,d,h,n)
