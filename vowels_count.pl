% Check if character is a vowel
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).
vowel(A).
vowel(E).
vowel(I).
vowel(O).
vowel(U).

% Base case
count_vowels([], 0).

% If head is vowel
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, Rest),
    Count is Rest + 1.

% If head is not vowel
count_vowels([H|T], Count) :-
    \+ vowel(H),
    count_vowels(T, Count).
