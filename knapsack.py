def knapSack(W , wt , val , n):

	
	if n == 0 or W == 0 :
		return 0

	
	if (wt[n-1] > W):
		return knapSack(W , wt , val , n-1)

	
	else:
		return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
				knapSack(W , wt , val , n-1))



# To test above function
val = [5,2,4,8]  #values of corresponding items
wt = [2,4,8,5]   #weights of corresponding items
W = 5
n = len(val)
print (knapSack(W , wt , val , n))
