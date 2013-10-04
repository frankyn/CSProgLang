import math

def euclideanDistance ( X, Y ):
	total = 0
	for index in range(len(X)):
		total = total + ( X[index] - Y[index] ) * ( X[index] - Y[index] )

	total = math.sqrt ( total )
	return total

def series(N):
	sum_total = 0
	power_of_two = 2
	for index in range(N):
		sum_total = sum_total + 1./power_of_two
		power_of_two = power_of_two * 2

	return sum_total

def tuple(N):
	sum_total = []
	power_of_two = 2
	for index in range(N):
		sum_total = sum_total + ([1./power_of_two])
		power_of_two = power_of_two * 2
		
	return sum_total
print "**********************"
print "1. To define a function you use def in python"
print "2. You can define variables in this form x,y=1,2. Where x = 1 and y = 2 after this line"
print "3. toString ( ) is defined by __str__()"
print "4. You can use ** to raise a number to a certain power"
print "5. A constructor for a class in python is defined by __init__ ( )"
print "**********************"
print "Test: euclideanDistance([0],[3])"
print euclideanDistance([0],[3])

print "Test: euclideanDistance([1,3],[1,5])"
print euclideanDistance([1,3],[1,5])

print "Test: euclideanDistance([3,4,5], [6,8,10])"
print euclideanDistance([3,4,5], [6,8,10])

print "Test: euclideanDistance([1,2,3,4,5], [10,11,12,13,14])"
print euclideanDistance([1,2,3,4,5], [10,11,12,13,14])

print "Test: euclideanDistance([0,0],[3,3])"
print euclideanDistance([0,0],[3,3])

print "Test: euclideanDistance([3,4], [0,0])"
print euclideanDistance([3,4], [0,0])

print "Test: euclideanDistance([1,3,5],[6,8,10])"
print euclideanDistance([1,3,5],[6,8,10])

print "Test: euclideanDistance([1,3,5,7],[2,4,6,8])"
print euclideanDistance([1,3,5,7],[2,4,6,8])

print "Test: series(1)"
print series(1)

print "Test: series(3)"
print series(3)

print "Test: series(5)"
print series(5)

print "Test: series(7)"
print series(7)

print "Test: series(2)"
print series(2)

print "Test: series(4)"
print series(4)

print "Test: series(6)"
print series(6)

print "Test: series(8)"
print series(8)

print "Test: tuple(1)"
print tuple(1)

print "Test: tuple(3)"
print tuple(3)

print "Test: tuple(5)"
print tuple(5)

print "Test: tuple(7)"
print tuple(7)

print "Test: tuple(2)"
print tuple(2)

print "Test: tuple(4)"
print tuple(4)

print "Test: tuple(6)"
print tuple(6)

print "Test: tuple(8)"
print tuple(8)

