% -------- GOAL STATE --------
goal(state(_, _, _, has)).

% -------- MOVES --------

% 1. Monkey walks
move(
    state(P1, on_floor, B, H),
    walk(P1, P2),
    state(P2, on_floor, B, H)
) :-
    P1 \= P2.

% 2. Monkey pushes box
move(
    state(P, on_floor, P, H),
    push(P, P2),
    state(P2, on_floor, P2, H)
) :-
    P \= P2.

% 3. Monkey climbs box
move(
    state(P, on_floor, P, H),
    climb,
    state(P, on_box, P, H)
).

% 4. Monkey grabs banana
move(
    state(middle, on_box, middle, has_not),
    grab,
    state(middle, on_box, middle, has)
).

% -------- SOLUTION --------

solve(State, []) :-
    goal(State).

solve(State, [Action | Rest]) :-
    move(State, Action, NewState),
    solve(NewState, Rest).
