% -------- FACTS --------

fact(raining).

% -------- RULES --------

rule(wet_ground, [raining]).
rule(dirty_shoes, [wet_ground]).

% -------- BACKWARD CHAINING ENGINE --------

prove(Goal) :-
    fact(Goal).                 % If goal is already a fact

prove(Goal) :-
    rule(Goal, Conditions),     % If goal can be derived from rule
    prove_all(Conditions).

% -------- PROVE ALL SUBGOALS --------

prove_all([]).
prove_all([H|T]) :-
    prove(H),
    prove_all(T).
