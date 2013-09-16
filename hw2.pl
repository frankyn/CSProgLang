equal([]).
equal([Head|[]]).
equal([Head|Tail]):- member(Head, Tail),
					  equal(Tail).


drop([]).
drop(X,[Head|List],L):- \+dif(1,X),
						append(List,[],L).
drop(X,[Head|List],L):- X1 is X-1,
						drop(X1, List, L).

range(X,X,[X]).
range(X,X,List):- append([],[X],List).
range(Min,Max,List):- dif(Min,Max),
					  M is Min+1,
					  range(M,Max,List1),
					  append([Min],List1,List).

element(X,[Head|List],E):- \+dif(1,X),
							E is Head.
element(X,[_|List],E):- X1 is X-1,
						element(X1, List, E).
