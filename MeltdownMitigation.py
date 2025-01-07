# definimos las funciones para que el codigo funcione 

# definicion de variables
# aqui vemos si la criticidad del reactor esta controlada o no
def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

# en esta  funcion hacemnos un if para verifgicar si esta bien o mal nuestro reactor realizando una coparacion con funciones matematicas
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= 80:
            return "green"
    elif 60 <= efficiency < 80:
            return "orange"
    elif 30 <= efficiency < 60:
            return "red"
    else:
            return "black"

# aqui definimos la funcion para que el reactor se active o desactive
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    critical_value = temperature * neutrons_produced_per_second
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold

    if critical_value < lower_bound:
        return "LOW"
    elif lower_bound <= critical_value <= upper_bound:
        return "NORMAL"
    else:
        return "DANGER"
    
if __name__ : "__main__"
# Hacemos los prints para que funcione
print("¿El reactor está en criticidad equilibrada?")
print("Caso 1 (750 K, 600 neutrones):", is_criticality_balanced(750, 600))
print ("La efficiencia del reactor es buena ?", reactor_efficiency(200,50,15000))
print("El estado de criticidad es", fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))
