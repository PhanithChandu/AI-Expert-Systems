% -------- DISEASE RULES --------

disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_ache).

disease(cold) :-
    symptom(cough),
    symptom(sneezing),
    symptom(runny_nose).

disease(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating).

disease(typhoid) :-
    symptom(fever),
    symptom(headache),
    symptom(stomach_pain).

% -------- INTERACTION --------

diagnose :-
    write('Answer yes. or no. for the following symptoms.'), nl,
    check(fever),
    check(cough),
    check(body_ache),
    check(sneezing),
    check(runny_nose),
    check(chills),
    check(sweating),
    check(headache),
    check(stomach_pain),
    nl,
    disease(D),
    write('You may have: '), write(D), nl.

% -------- SYMPTOM CHECK --------

:- dynamic symptom/1.

check(Symptom) :-
    write('Do you have '), write(Symptom), write('? '),
    read(Response),
    Response = yes,
    assertz(symptom(Symptom)).

check(_) :-
    true.
