def min_index(L):
	smallest = 1
	for i in range(0,len(L)):
		if L[i] < L[smallest]:
			smallest = i
	return smallest

def selection_sort(L):
	pivot = 0
	while pivot < len(L):
		for i in range(pivot+1,len(L)):
			if L[i] < L[pivot]:
				tmp = L[i]
				L[i] = L[pivot]
				L[pivot] = tmp
				i = len(L)
		pivot = pivot + 1
	return L

def partitions(L,n):
	output_list = []
	sub_list = []
	for i in range(0,len(L)):
		if i%n == 0 and i > 0:
			output_list.append(sub_list)
			sub_list = []
		sub_list.append(L[i])
	output_list.append(sub_list)
	return output_list

def my_row(L,n):
	return L[n]

def my_col(L,n):
	output_col = []
	for i in range(len(L)):
		output_col.append(L[i][n])
	return output_col

def dot_product(M1,M2):
	prod = 0
	for i in range(0,len(M1)):
		prod = prod + M1[i]*M2[i]
	return prod

print "min_index([3,5,1,8,9,2])"
print min_index([3,5,1,8,9,2])

print "min_index([0,3,5,1,8,4,2,9,6])"
print min_index([0,3,5,1,8,4,2,9,6])

print "min_index([3,5,1,8,4,2,0])"
print min_index([3,5,1,8,4,2,0])

print "min_index([3,5,2,8,4,1,9,6])"
print min_index([3,5,2,8,4,1,9,6])

print "selection_sort([4,3,1,0,9,8,100,2,10])"
print selection_sort([4,3,1,0,9,8,100,2,10])

print "selection_sort([10,5,8,2,19,0,20])"
print selection_sort([10,5,8,2,19,0,20])

print "selection_sort([100,50,20,34,2,9,6,10])"
print selection_sort([100,50,20,34,2,9,6,10])

print "selection_sort([10,5])"
print selection_sort([10,5])

print "partitions([2,4,6,8,10,12,14,16], 2)"
print partitions([2,4,6,8,10,12,14,16], 2)

print "partitions([0,1,2,3,4,5,6,7,8,9],5)"
print partitions([0,1,2,3,4,5,6,7,8,9],5)

print "partitions([2,4,6,8,10,12,14,16], 3)"
print partitions([2,4,6,8,10,12,14,16], 3)

print "partitions([0,1,2,3,4,5,6,7,8,9],3)"
print partitions([0,1,2,3,4,5,6,7,8,9],3)

mat = [
[1, 2, 3],
[4, 5, 6], [7, 8, 9], [0, 1, 2]
]

print "my_row(mat,0)"
print my_row(mat,0)

print "my_row(mat,2)"
print my_row(mat,2)

print "my_row(mat,1)"
print my_row(mat,1)

print "my_row(mat,3)"
print my_row(mat,3)

mat = [
[1, 2, 3, 5],
[4, 5, 6, 7], [7, 8, 9, 9], [0, 1, 2, 3]
]

print "my_col(mat,0)"
print my_col(mat,0)

print "my_col(mat,2)"
print my_col(mat,2)

print "my_col(mat,1)"
print my_col(mat,1)

print "my_col(mat,3)"
print my_col(mat,3)

print "dot_product([1,4,7],[2,5,8])"
print dot_product([1,4,7],[2,5,8])

print "dot_product([2,6],[8,9])"
print dot_product([2,6],[8,9])

print "dot_product([3,6,9],[2,4,8])"
print dot_product([3,6,9],[2,4,8])

print "dot_product([2],[8])"
print dot_product([2],[8])

