# definimos las funciones para que nuesrto codigo funcione 

# funcion para saber si pacman puede comer al fantasma
def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

# funcion para saber si pacman puede comer un punto
def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot

# funcion para saber si a perdido
def lose(power_pellet_active, touching_ghost):
    return touching_ghost and not power_pellet_active

# funcion para saber si a ganado
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

# probamos las funciones
if __name__ == "__main__":

# definimos los valores de las variables dentro de las funciones

    power_pellet_active = False
    touching_ghost = True
    has_eaten_all_dots = False
    touching_power_pellet = True
    touching_dot = False

    # probamos las funciones
    print("PacMan se puede comer a un fantasma?", eat_ghost(power_pellet_active, touching_ghost))
    print("PacMan se puede comer a un punto?", score(touching_power_pellet, touching_dot))
    print("PacMan ha perdido?", lose(power_pellet_active, touching_ghost))
    print("PacMan ha ganado?", win(has_eaten_all_dots, power_pellet_active, touching_ghost))