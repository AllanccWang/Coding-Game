#https://www.codingame.com/training/hard/max-rect
#MAX RECT
#concept: Dynamic programming
def kadane(arr,start,finish,n):
	Sum=0
	maxSum=-999999999999

	finish[0] = -1
	local_start = 0

	for i in range(n):
		Sum+=arr[i]
		if Sum<0:
			Sum=0
			local_start=i+1
		elif Sum>maxSum:
			maxSum=Sum
			start[0]=local_start
			finish[0]=i

	if finish[0]!=-1:
		return maxSum

	maxSum=arr[0]
	start[0]=finish[0] = 0

	for i in range(1,n):
		if arr[i]>maxSum:
			maxSum=arr[i]
			start[0]=finish[0]=i
	return maxSum

def findMaxSum(M):
	global ROW,COL
	maxSum=-999999999999

	temp=[None]*ROW
	Sum=0
	start=[0]
	finish=[0]

	for left in range(COL):
		temp=[0]*ROW
		for right in range(left,COL):
			for i in range(ROW):
				temp[i]+=M[i][right]
			Sum=kadane(temp,start,finish,ROW)
			if Sum>maxSum:
				maxSum=Sum
	print(maxSum)

M=[]
COL,ROW=[int(i) for i in input().split()]
for i in range(ROW):
    M+=[[int(x) for x in input().split()]]

findMaxSum(M)
