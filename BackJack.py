# Ejercicio 5 de https://exercism.org/tracks/python


#Determina el valor de una carta.
def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)
    
# Determina qué carta tiene mayor valor.
def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return (card_one, card_two)

# Calcula el valor más ventajoso para el As.
def value_of_ace(card_one, card_two):
    # Comprobar si ya hay un as en la mano inicial
    if card_one == 'A' or card_two == 'A':
        return 1
    
    # Sumar el valor de las dos cartas iniciales
    total = value_of_card(card_one) + value_of_card(card_two)
    
    # Si el as como 11 no causa que se pase de 21, usar 11
    if total + 11 <= 21:
        return 11
    return 1

# Determina si la mano es un blackjack natural.
def is_blackjack(card_one, card_two):
    has_ace = card_one == 'A' or card_two == 'A'
    has_ten = (card_one in ['10', 'J', 'Q', 'K']) or (card_two in ['10', 'J', 'Q', 'K'])
    
    return has_ace and has_ten

# Determina si se pueden dividir las cartas en pares.
def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)

# Determina si se puede doblar la apuesta.
def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]

# Ejemplos
print(higher_card('A', 'K')) 
print(value_of_ace('5', '5'))
print(is_blackjack('A', 'K'))
print(can_split_pairs('Q', 'K'))
print(can_double_down('5', '6'))