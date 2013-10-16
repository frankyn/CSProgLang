import math

def f1 ( n ):
	return 'log('+str(n)+')='+str(round(math.log(n,2),1))

def f2 ( n ):
	return 'log^2('+str(n)+')='+str(round(math.log(n,2)**2,1))

def f3 ( n ):
	return str(n)+'log('+str(n)+')='+str(round(n*math.log(n,2),1))

def f4 ( n ):
	return str(n)+'^2('+str(n)+')='+str(n**2)

def f5 ( n ):
	return '2^'+str(n)+'('+str(n)+')='+str(2**n)

def f6 ( n ):
	return str(n)+'!('+str(n)+')='+str(reduce(lambda a,b:a*b,range(1,n+1)))

def f7 ( n ):
	return str(n)+'^'+str(n)+'('+str(n)+')='+str(n**n)

def printGraph ( f1 , f2 , n ):
	for i in range(1,n+1):
		print f1(i)+"\t"+f2(i)

def printGraph2 ( l , n ):
	for x in range(1,n+1):
		str_out = ''
		for i in range(len(l)):
			str_out = str_out + l[i](x) + "\t"
		print str_out	

print 'Testing'

print 'f1(8)'
print f1(8)

print 'f1(16)'
print f1(16)

print 'f1(10)'
print f1(10)

print 'f1(32)'
print f1(32)

print 'f2(8)'
print f2(8)

print 'f2(16)'
print f2(16)

print 'f2(10)'
print f2(10)

print 'f2(32)'
print f2(32)

print 'f3(8)'
print f3(8)

print 'f3(16)'
print f3(16)

print 'f3(10)'
print f3(10)

print 'f3(32)'
print f3(32)

print 'f4(2)'
print f4(2)

print 'f4(3)'
print f4(3)

print 'f4(4)'
print f4(4)

print 'f4(5)'
print f4(5)

print 'f5(2)'
print f5(2)

print 'f5(3)'
print f5(3)

print 'f5(4)'
print f5(4)

print 'f5(5)'
print f5(5)

print 'f6(2)'
print f6(2)

print 'f6(4)'
print f6(4)

print 'f6(6)'
print f6(6)

print 'f6(7)'
print f6(7)

print 'f7(2)'
print f7(2)

print 'f7(3)'
print f7(3)

print 'f7(4)'
print f7(4)

print 'f7(5)'
print f7(5)

print 'printGraph(f1,f3,9)'
printGraph(f1,f3,9)

print 'printGraph(f2,f1,9)'
printGraph(f2,f2,9)

print 'printGraph(f5,f6,6)'
printGraph(f5,f6,6)

print 'printGraph(f6,f7,7)'
printGraph(f6,f7,7)

print 'printGraph2([f1,f2,f3],10)'
printGraph2([f1,f2,f3],10)

print 'printGraph([f2,f3,f4,f5,f6,f7],5)'
printGraph2([f2,f3,f4,f5,f6,f7],5)

print 'printGraph2([f5,f6,f7],10)'
printGraph2([f5,f6,f7],10)

print 'printGraph2([f2,f4,f6],5)'
printGraph2([f2,f4,f6],5)

print 'printGraph([f7],40)'
printGraph2([f7],40)

