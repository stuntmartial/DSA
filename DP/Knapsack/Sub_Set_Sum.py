global t 
def sub_set_sum(arr,sum_):
	
	t = list()

	#creating empty array
	for i in range(len(arr) + 1):
		t.append([-1] * (sum_ + 1))

	#initiaizing matrix
	for i in range(len(arr) + 1):
		for j in range(sum_ + 1):
			if j == 0:
				t[i][j] = 1
			elif i == 0:
				t[i][j] = 0

	#Coding the choice diagram
	for i in range(1,len(arr) + 1):
		for j in range(1 , sum_ + 1):

			if arr[i - 1] <= j:
				t[i][j] = t[i-1][j - arr[i -1]] + t[i - 1][j]
			else:
				t[i][j] = t[i-1][j]

	for i in range(len(arr) + 1):
		for j in range(sum_ + 1):
			print(t[i][j] , end = '\t')
		print()


	#printing selected elements
	w = sum_
	res = t[len(arr)][sum_]
	print("Res---->",res)
	selected_weights = list()	
	for i in range (len(arr),0,-1):
		
		if w <= 0:
			break

		elif res == t[i-1][w]:
			continue

		else:
			selected_weights.append(arr[i-1])
			res = t[i-1][w-arr[i-1]] 
			w = w - arr[i-1]
			
	print(selected_weights)
			
arr = [1,2,3,4,5]
sum_ = 5
sub_set_sum(arr,sum_)




'''
<div class="form-group row">        
                  <label for="tweet" class="col-form-label" style="font-size: 50px;">Tweet</label> 
                    <div class="col-12">       
                      <input type="text" id="search" class="form-control" height="200" width="700" onchange="hideIcon(this);" autocomplete="off" style="border: 2px solid black;">
                    </div>
                </div>  
                  <div class="form-group row">

'''