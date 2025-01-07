# Ejercicio 5 de https://exercism.org/tracks/python

# Intercambio de Divisas EUR a Dolar, el tipo de cambio es 1.2
def exchange_money(budget, exchange_rate):
    return float(budget / exchange_rate)

budget = 127.5
exchange_rate = 1.2
print("El total del cambio de moneda es de",(exchange_money(budget, exchange_rate)), "Dollares")

# Cuando Dinero Queremos Intercambiar, budget sigue siendo nuestro presupuesto, exchangin_value es lo que queremos la cantidad de dinero a cambiar
def get_change(budget, exchanging_value):
    return float(budget - exchanging_value)

budget = 127.5
exchanging_value = 120
print("El dinero acambiar son",(exchanging_value),"Euros")


# Intercambio de Dinero denomitation es el valor un billete, y number _of_bills es la cantidad de billetes
def get_value_of_bills(denomination, number_of_bills):
    return int(denomination * number_of_bills)

denomination = 5
number_of_bills = 128
print ("El total de dinero que tenemos es",(get_value_of_bills(denomination, number_of_bills)) ,"Euros")

# amount es el valor inicial que tenemos y denomination representa los billetes al cambio, por ejemplo si tengo 10 USD en Euros me Deberia dar 8 Billetes
def get_number_of_bills(amount, denomination):
    return int(amount // denomination)

amount = 127.5
denomination = 5
print ("El cantidad a recibir despues del cabmio es",(get_number_of_bills(amount, denomination)) ,"Billetes")

# amount es el valor inicial, denomitaion es el valor de un solo billete y en este caso necesitamos obtener el sobrante del cambio actual
def get_leftover_of_bills(amount, denomination):
    return float(amount % denomination)

amount = 127.5
denomination = 20
print("El sobrante del cambio es de ",(get_leftover_of_bills(amount, denomination)), "Euros")

def exchangeable_value(budget, exchange_rate, spread, denomination):
    # Calcula la tasa de cambio real incluyendo el spread
    actual_exchange_rate = exchange_rate * (1 + spread / 100)
    
    # Calcula el valor total en la nueva moneda
    total_value = budget / actual_exchange_rate
    
    # Calcula el valor máximo redondeado según la denominación
    exchangeable_value = int(total_value // denomination) * denomination
    
    return exchangeable_value


print(exchangeable_value(127.25, 1.20, 10, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))