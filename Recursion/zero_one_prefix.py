def func(num,ext_one,rem_places):

	if rem_places == 0:
		print(num)
		return

	func(num+"1",ext_one+1,rem_places-1)

	if ext_one > 0:
		func(num+"0",ext_one-1,rem_places-1)


rem_places = int(input("Enter n : "))
num = ""
ext_one = 0

func(num,ext_one,rem_places)