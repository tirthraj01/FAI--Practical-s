
% Step 1: Define parent relationships
parent(john, mary).
parent(john, bob).
parent(mary, alice).
parent(bob, sam).

% Step 2: Define gender
male(john).
male(bob).
male(sam).

female(mary).
female(alice).

% Step 3: Define father relationship
father(X, Y) :-
    parent(X, Y),
    male(X).

% Step 4: Define mother relationship
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Step 5: Define sibling relationship
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% Step 6: Define grandparent relationship
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
