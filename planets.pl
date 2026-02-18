% -------- PLANET DATABASE --------
planet(mercury, 57.9, terrestrial, 0).
planet(venus, 108.2, terrestrial, 0).
planet(earth, 149.6, terrestrial, 1).
planet(mars, 227.9, terrestrial, 2).
planet(jupiter, 778.5, gas_giant, 95).
planet(saturn, 1434, gas_giant, 83).
planet(uranus, 2871, ice_giant, 27).
planet(neptune, 4495, ice_giant, 14).

% -------- RULES --------

% Find distance of a planet from the Sun
distance_from_sun(Planet, Distance) :-
    planet(Planet, Distance, _, _).

% Find all terrestrial planets
terrestrial_planet(Planet) :-
    planet(Planet, _, terrestrial, _).

% Find planets with more than N moons
planets_with_many_moons(Planet, N) :-
    planet(Planet, _, _, Moons),
    Moons > N.

% Find planets farther than Earth
farther_than_earth(Planet) :-
    planet(earth, EarthDist, _, _),
    planet(Planet, Dist, _, _),
    Dist > EarthDist.
