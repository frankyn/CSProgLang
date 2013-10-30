def scalar_product ( s , V ):
	V2 = []
	for i in range(len(V)):
		V2.append ( s*V[i] )
	return V2

#list comprehention version of scalar_product
def scalar_product_lc ( s , V ):
	return [V[i]*s for i in range(len(V))]

def vector_sum ( V1 , V2 ):
	V3 = []
	for i in range(len(V1)):
		V3.append ( V1[i] + V2[i] )
	return V3

#list comprehention version of vector_sum
def vector_sum_lc ( V1 , V2 ):
	return [V1[i]+V2[i] for i in range(len(V1))]

def matrix_sum ( M1 , M2 ):
	M3 = []
	for i in range(len(M1)):
		R = []
		for b in range(len(M1[i])):
			R.append ( M1[i][b] + M2[i][b] )
		M3.append ( R )
	return M3

def matrix_sum_lc ( M1 , M2 ):
	return list(([M1[i][b]+M2[i][b] for b in range(len(M1[0]))] for i in range(len(M1))))

print "Test Cases:"

print "V = [1, 3, 7, 8, 10]"
V = [1, 3, 7, 8, 10]

print "scalar_product(0.5, V)"
print scalar_product(0.5, V)

print "scalar_product(1.5, V)"
print scalar_product(1.5, V)

print "scalar_product(2, V)"
print scalar_product(2, V)

print "scalar_product(1, V)"
print scalar_product(1, V)

print "scalar_product_lc(0.5, V)"
print scalar_product_lc(0.5, V)

print "scalar_product_lc(1.5, V)"
print scalar_product_lc(1.5, V)

print "scalar_product_lc(2, V)"
print scalar_product_lc(2, V)

print "scalar_product_lc(1, V)"
print scalar_product_lc(1, V)

print "vector_sum([0,2,4,6],[1,1,1,1])"
print vector_sum([0,2,4,6],[1,1,1,1])

print "vector_sum([1,5],[0.5,0.5])"
print vector_sum([1,5],[0.5,0.5])

print "vector_sum([0,2,4,6],[2,2,2,2])"
print vector_sum([0,2,4,6],[2,2,2,2])

print "vector_sum([1,5],[0.1,0.1])"
print vector_sum([1,5],[0.1,0.1])

print "vector_sum_lc([0,2,4,6],[1,1,1,1])"
print vector_sum_lc([0,2,4,6],[1,1,1,1])

print "vector_sum_lc([1,5],[0.5,0.5])"
print vector_sum_lc([1,5],[0.5,0.5])

print "vector_sum_lc([0,2,4,6],[2,2,2,2])"
print vector_sum_lc([0,2,4,6],[2,2,2,2])

print "vector_sum_lc([1,5],[0.1,0.1])"
print vector_sum_lc([1,5],[0.1,0.1])


print "M = [\
[1, 2, 3],\
[4, 5, 6], [7, 8, 9], [0, 1, 2]\
]"
M = [
[1, 2, 3],
[4, 5, 6], [7, 8, 9], [0, 1, 2]
]

print "N = [\
[1, 2, 2],\
[1, 1, 2], [2, 1, 2], [2, 1, 1]\
]"
N = [
[1, 2, 2],
[1, 1, 2], [2, 1, 2], [2, 1, 1]
]

print "matrix_sum(M,N)"
print matrix_sum(M,N)

print "matrix_sum_lc(M,N)"
print matrix_sum_lc(M,N)