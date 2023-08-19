#https://www.codingame.com/training/hard/max-rect
#max-rect
#concept: DP
def kadane(arr,start,finish,n)
  sum,maxSum=0,-10**9
  finish[0]=-1
  local_start=0

  for i in (0...n)
    sum+=arr[i]
    if sum<0
      sum=0
      local_start=i+1
    elsif sum>maxSum
      maxSum=sum
      start[0]=local_start
      finish[0]=i
    end
  end

  if finish[0]!=-1
    return maxSum
  end

  maxSum=arr[0]
  start[0]=finish[0]=0

  for i in (1...n)
    if arr[i]>maxSum
      maxSum=arr[i]
      start[0]=finish[0]=i
    end
  end
  return maxSum
end

#Sum subretangle in mtrix
def findMaxSum(mtrix,row,col)
  maxSum=-10**9
  sum=0
  start=[0]
  finish=[0]
  for left in (0...col)
    temp=[0]*row
    for right in (left...col)
      # Find the maximum sum subarray in
      # temp[]. The kadane() function also
      # sets values of start and finish.
      (0...row).map{|i|temp[i]+=mtrix[i][right]}
      maxSum=[kadane(temp,start,finish,row),maxSum].max
    end
  end
  print(maxSum)
end

col,row=gets.split.map &:to_i
mtrix=[]
row.times{mtrix+=[gets.split.map(&:to_i)]}
findMaxSum(mtrix,row,col)
