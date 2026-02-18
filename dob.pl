% ----- Database -----
person(john, date(15, 5, 2002)).
person(anna, date(21, 8, 2001)).
person(rahul, date(3, 12, 2000)).
person(meena, date(10, 1, 2003)).

% ----- Rule to get DOB -----
get_dob(Name, DOB) :-
    person(Name, DOB).

% ----- Rule to get people born in a specific year -----
born_in_year(Name, Year) :-
    person(Name, date(_, _, Year)).
