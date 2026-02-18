:- dynamic fact/1.

% -------- INITIAL FACTS --------
fact(raining).

% -------- RULES --------

rule(wet_ground, [raining]).
rule(dirty_shoes, [wet_ground]).

% -------- FORWARD CHAINING ENGINE --------

forward_chain :-
    rule(Conclusion, Conditions),
    \+ fact(Conclusion),
    check_conditions(Conditions),
    assertz(fact(Conclusion)),
    write('Derived: '), write(Conclusion), nl,
    forward_chain.

forward_chain.

% -------- CHECK ALL CONDITIONS TRUE --------

check_conditions([]).
check_conditions([H|T]) :-
    fact(H),
    check_conditions(T).
