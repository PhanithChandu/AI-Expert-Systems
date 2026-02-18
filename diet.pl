% -------- DISEASE FACTS --------

disease(diabetes).
disease(hypertension).
disease(obesity).
disease(anemia).
disease(gastric).

% -------- DIET RULES --------

diet(diabetes, 'Low sugar diet, high fiber, whole grains, avoid sweets.').
diet(hypertension, 'Low salt diet, avoid processed food, eat fruits and vegetables.').
diet(obesity, 'Low calorie diet, avoid junk food, regular exercise.').
diet(anemia, 'Iron rich foods like spinach, red meat, dates.').
diet(gastric, 'Avoid spicy food, eat light meals, drink plenty of water.').

% -------- SUGGESTION RULE --------

suggest_diet(Disease) :-
    disease(Disease),
    diet(Disease, Advice),
    write('Recommended Diet: '), nl,
    write(Advice), nl.

% If disease not found
suggest_diet(Disease) :-
    \+ disease(Disease),
    write('Disease not found in database.'), nl.
