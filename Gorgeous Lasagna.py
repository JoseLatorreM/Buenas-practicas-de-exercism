# Ejercicio 2 de https://exercism.org/tracks/python

# Constante ya que es el tiempo de coccion total y este no cambia
EXPECTED_BAKE_TIME = 40

# Función para calcular el tiempo restante de horneado
def bake_time_remaining(elapsed_bake_time):
    """Calcula el tiempo restante de horneado."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# Función para calcular el tiempo de preparación
def preparation_time_in_minutes(number_of_layers):
    """Calcula el tiempo de preparación en minutos."""
    return number_of_layers * 2

# Función para calcular el tiempo total transcurrido
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcula el tiempo total transcurrido."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

# Ejemplo de uso
if __name__ == "__main__":
    print("Tiempo de Cocción es de", str(EXPECTED_BAKE_TIME), "minutos")

    elapsed_bake_time = 30
    remaining_time = bake_time_remaining(elapsed_bake_time)
    print("Quedan", str(remaining_time), "minutos para que esté listo")

    layers = 2
    prep_time = preparation_time_in_minutes(layers)
    print("Calculando las capas se demora un total de", str(prep_time), "minutos")

    total_time = elapsed_time_in_minutes(layers, 20)
    print("El tiempo total fue de", str(total_time), "minutos")