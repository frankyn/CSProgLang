
inter([],[],X):- append([],[],X).
inter([],List,X):- inter([],[],X).
inter([Element|Rem],List,X):- (member(Element,List)),
							  append([Element],X1,X),
							  inter(Rem,List,X1).
inter([_|Rem],List,X):- inter(Rem,List,X).

union([],X,X).
union([],[],X).
union([Element|Rem],List,X):- (\+member(Element,List)),
							  append([Element],List,X1),
							  union(Rem,X1,X).
union([_|Rem],List,X):- union(Rem,List,X).

countZeros([],N):- N is 0.
countZeros([Head|Rem],N):- Head is 0, 
						   countZeros(Rem,N1), 
						   N is 1 + N1.
countZeros([_|Rem],N):- countZeros(Rem,N1), 
						N is N1.

sumAll([],S):- S is 0.
sumAll([Head|Rem],S):- sumAll(Rem,S1), 
					   S is Head + S1.