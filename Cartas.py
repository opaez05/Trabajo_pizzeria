import random

class Cartas:
    def __init__(self, categoria, color, valor):
        self.categoria = categoria
        self.color = color
        self.valor = valor
    
    def __repr__(self):
        mapa_valores = {1: 'As', 11: 'J', 12: 'Q', 13: 'K'}
        nombre_carta = mapa_valores.get(self.valor, str(self.valor))
        return f"({nombre_carta} de {self.categoria})"

def crear_baraja():
    categorias = ['corazones', 'diamantes', 'tréboles', 'picas']
    colores = {'corazones': 'rojo', 'diamantes': 'rojo', 'tréboles': 'negro', 'picas': 'negro'}
    baraja = []
    for categoria in categorias:
        for valor in range(1, 14):
            baraja.append(Cartas(categoria, colores[categoria], valor))
    return baraja

def bubble_sort(cartas):
    n = len(cartas)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if cartas[j].valor > cartas[j + 1].valor:
                cartas[j], cartas[j + 1] = cartas[j + 1], cartas[j]
    return cartas

def ordenar_baraja(baraja):
    baraja_por_categoria = {
        'corazones': [],
        'diamantes': [],
        'tréboles': [],
        'picas': []
    }
    for carta in baraja:
        baraja_por_categoria[carta.categoria].append(carta)
    
    baraja_final_ordenada = []
    orden_categorias = ['corazones', 'diamantes', 'tréboles', 'picas']
    
    for categoria in orden_categorias:
        monton_ordenado = bubble_sort(baraja_por_categoria[categoria])
        baraja_final_ordenada.extend(monton_ordenado)
    
    return baraja_final_ordenada

# Ejemplo de uso
baraja_completa = crear_baraja()
random.shuffle(baraja_completa)

print("Baraja Aleatoria")
print(baraja_completa)

baraja_ordenada = ordenar_baraja(baraja_completa)

print("\n Baraja Organizada")
print(baraja_ordenada)