% -------- GRAPH --------

edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(e, g).
edge(f, g).

% -------- HEURISTIC VALUES --------

h(a, 6).
h(b, 4).
h(c, 5).
h(d, 3).
h(e, 2).
h(f, 4).
h(g, 0).

% -------- BEST FIRST SEARCH --------

best_first(Start, Goal, Path) :-
    search([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

% If head of path is goal
search([[Goal|Rest]|_], Goal, [Goal|Rest]).

% Expand first path
search([CurrentPath|OtherPaths], Goal, SolutionPath) :-
    CurrentPath = [CurrentNode|_],
    findall(
        [Next,CurrentNode|Rest],
        (edge(CurrentNode, Next),
         \+ member(Next, CurrentPath),
         CurrentPath = [CurrentNode|Rest]),
        NewPaths),
    add_heuristic(NewPaths, SortedPaths),
    append(OtherPaths, SortedPaths, UpdatedPaths),
    search(UpdatedPaths, Goal, SolutionPath).

% -------- SORT BY HEURISTIC --------

add_heuristic(Paths, Sorted) :-
    map_list_to_pairs(path_heuristic, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_heuristic([Node|_], H) :-
    h(Node, H).
