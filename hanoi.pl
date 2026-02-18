% Base case: Only one disk
hanoi(1, Source, Destination, _) :-
    write('Move disk 1 from '),
    write(Source),
    write(' to '),
    write(Destination), nl.

% Recursive case
hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    N1 is N - 1,

    % Step 1: Move N-1 disks to auxiliary peg
    hanoi(N1, Source, Auxiliary, Destination),

    % Step 2: Move largest disk to destination
    write('Move disk '),
    write(N),
    write(' from '),
    write(Source),
    write(' to '),
    write(Destination), nl,

    % Step 3: Move N-1 disks to destination
    hanoi(N1, Auxiliary, Destination, Source).
