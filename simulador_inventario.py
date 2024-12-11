# Simulador financiero básico
saldo_inicial = float(input("Ingrese el saldo inicial: "))
ahorro_mensual = float(input("Ingrese el ahorro mensual: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
anios = int(input("Ingrese el número de años: "))

saldo = saldo_inicial
for anio in range(1, anios + 1):
    saldo += ahorro_mensual * 12
    saldo += saldo * (tasa_interes_anual / 100)
    print(f"Año {anio}: ${saldo:.2f}")
