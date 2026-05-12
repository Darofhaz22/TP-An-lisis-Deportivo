
import pandas as pd

# Leer dataset
df = pd.read_csv("datos/dataset.csv")

# Crear tabla
tabla = {}

# Recorrer partidos
for i, partido in df.iterrows():

    local = partido["equipo_local"]
    visitante = partido["equipo_visitante"]

    goles_local = partido["goles_local"]
    goles_visitante = partido["goles_visitante"]

    # Crear equipos si no existen
    for equipo in [local, visitante]:

        if equipo not in tabla:

            tabla[equipo] = {
                "Puntos": 0,
                "Victorias": 0,
                "Empates": 0,
                "Derrotas": 0,
                "Goles_Favor": 0,
                "Goles_Contra": 0,
                "Diferencia_Gol": 0
            }

    # Goles
    tabla[local]["Goles_Favor"] += goles_local
    tabla[local]["Goles_Contra"] += goles_visitante

    tabla[visitante]["Goles_Favor"] += goles_visitante
    tabla[visitante]["Goles_Contra"] += goles_local

    # Resultados
    if goles_local > goles_visitante:

        tabla[local]["Puntos"] += 3
        tabla[local]["Victorias"] += 1

        tabla[visitante]["Derrotas"] += 1

    elif goles_visitante > goles_local:

        tabla[visitante]["Puntos"] += 3
        tabla[visitante]["Victorias"] += 1

        tabla[local]["Derrotas"] += 1

    else:

        tabla[local]["Puntos"] += 1
        tabla[visitante]["Puntos"] += 1

        tabla[local]["Empates"] += 1
        tabla[visitante]["Empates"] += 1

    # Diferencia de gol
    tabla[local]["Diferencia_Gol"] = (
        tabla[local]["Goles_Favor"]
        - tabla[local]["Goles_Contra"]
    )

    tabla[visitante]["Diferencia_Gol"] = (
        tabla[visitante]["Goles_Favor"]
        - tabla[visitante]["Goles_Contra"]
    )

# Convertir a DataFrame
tabla_final = pd.DataFrame(tabla).T

# Ordenar tabla
tabla_final = tabla_final.sort_values(
    by=["Puntos", "Diferencia_Gol"],
    ascending=False
)

# Mostrar tabla
# Mostrar todas las columnas
pd.set_option('display.max_columns', None)

# Mostrar tabla
print("TABLA DE POSICIONES")
print(tabla_final)

# Promedio de goles
promedio = (
    df["goles_local"].mean()
    + df["goles_visitante"].mean()
) / 2

print("\nPromedio de goles:", round(promedio, 2))
