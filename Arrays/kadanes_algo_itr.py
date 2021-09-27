def func(arr):
    max_=arr[0]
    max_till_now_k= arr[0]

    for i in range(1,len(arr)):
        max_till_now_k=max(max_till_now_k+arr[i],arr[i])
        max_=max(max_,max_till_now_k)

    print(max_)

arr=[-2, -3, 4, -1, -2, 1, 5, -3]
func(arr)
a = [9 , -51 ,-20, -13 ,-51 ,40 ,-21, 75 ,-24 ,29 ,-86 ,5 ,-38 ,15 ,48 ,-87, -9, 42 ,39, 64, 47, -63, 22, -81, -20, -100 ,28]
func(a)
a1=[52,-81,8,-47,-10]
func(a1)