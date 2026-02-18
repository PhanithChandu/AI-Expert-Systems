% -------- FACTS --------

fruit_colour(apple, red).
fruit_colour(apple, green).
fruit_colour(banana, yellow).
fruit_colour(grapes, green).
fruit_colour(grapes, purple).
fruit_colour(orange, orange).
fruit_colour(mango, yellow).
fruit_colour(cherry, red).

% -------- RULE --------

find_colour(Fruit, Colour) :-
    fruit_colour(Fruit, Colour).
