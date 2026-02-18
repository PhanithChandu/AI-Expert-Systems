% -------- FACTS --------

bird(sparrow).
bird(pigeon).
bird(eagle).
bird(parrot).
bird(penguin).
bird(ostrich).

% -------- EXCEPTIONS (Cannot Fly) --------

cannot_fly(penguin).
cannot_fly(ostrich).

% -------- RULE --------

can_fly(Bird) :-
    bird(Bird),
    \+ cannot_fly(Bird).
