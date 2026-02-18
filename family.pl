% -------- FACTS --------

% Gender
male(john).
male(paul).
male(mike).
male(tom).

female(mary).
female(linda).
female(susan).
female(anna).

% Parent relationships
parent(john, paul).
parent(mary, paul).

parent(john, linda).
parent(mary, linda).

parent(paul, mike).
parent(susan, mike).

parent(paul, anna).
parent(susan, anna).

parent(linda, tom).

% -------- RULES --------

% Father
father(F, C) :-
    male(F),
    parent(F, C).

% Mother
mother(M, C) :-
    female(M),
    parent(M, C).

% Grandparent
grandparent(GP, GC) :-
    parent(GP, X),
    parent(X, GC).

% Grandfather
grandfather(GF, GC) :-
    male(GF),
    grandparent(GF, GC).

% Grandmother
grandmother(GM, GC) :-
    female(GM),
    grandparent(GM, GC).

% Siblings
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% Brother
brother(B, X) :-
    male(B),
    sibling(B, X).

% Sister
sister(S, X) :-
    female(S),
    sibling(S, X).
