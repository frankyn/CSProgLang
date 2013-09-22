sorted([]).
sorted([Element]).
sorted([Head,Next|Tail]):- Head < Next,
						   sorted([Next|Tail]).

reverse([],L):- append([],[],L).
reverse([Head|Tail],Output):- reverse(List, Output1),
							  append(Output1,[Head],Output).

remove_duplicates([],L):- append([],[],L).
remove_duplicates([Head|Tail],L):- member(Head,Tail),
								   remove_duplicates(Tail,L).
remove_duplicates([Head|Tail],L):- \+member(Head,Tail),
								   remove_duplicates(Tail,L1),							
								   append([Head],L1,L).

merge([],[],L):- append([],[],L).
merge([H1|L1],[],L):- append([H1|L1],[],L).
merge([],[H1|L1],L):- append([H1|L1],[],L).
merge([H1|L1],[H2|L2],L):-  H1 < H2,
							merge(L1,[H2|L2],L3),
							append([H1],L3,L). 
merge([H1|L1],[H2|L2],L):- 	H2 < H1,
							merge([H1|L1],L2,L3),
							append([H2],L3,L).
merge([H1|L1],[H2|L2],L):- 	H1 is H2,
							merge(L1,L2,L3),
							append([H1,H2],L3,L).