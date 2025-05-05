# Peso dos ingredientes em gramas
peso_queijo = 50
peso_presunto = 50
peso_hamburguer = 100

# Solicitar a quantidade de sanduíches
quantidade_sanduiches = int(input("Digite a quantidade de sanduíches a fazer: "))

# Calcular a quantidade total de cada ingrediente necessário em quilos
total_queijo = (2 * peso_queijo * quantidade_sanduiches) / 1000  # kg
total_presunto = (peso_presunto * quantidade_sanduiches) / 1000    # kg
total_hamburguer = (peso_hamburguer * quantidade_sanduiches) / 1000 # kg

# Exibir os resultados
print(f"Quantidade de queijo necessária: {total_queijo:.2f} kg")
print(f"Quantidade de presunto necessária: {total_presunto:.2f} kg")
print(f"Quantidade de hambúrguer necessária: {total_hamburguer:.2f} kg")