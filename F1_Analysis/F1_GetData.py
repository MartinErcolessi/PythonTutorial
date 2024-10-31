import requests
import pandas as pd

# Función para obtener datos de la API de Ergast
def fetch_ergast_data(endpoint, params=None):
    """
    Función que se conecta a la API de Ergast y devuelve los datos en formato JSON.
    """
    base_url = "https://ergast.com/api/f1/"
    url = base_url + endpoint
    response = requests.get(url, params=params, headers={"Accept": "application/json"})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos de {url}")
        return None

# Obtener datos de la temporada 2024 (puedes cambiar el año)
# Pilotos
drivers_data = fetch_ergast_data("2024/drivers.json")
drivers_list = drivers_data['MRData']['DriverTable']['Drivers'] if drivers_data else []

# Equipos (Constructores)
constructors_data = fetch_ergast_data("2024/constructors.json")
constructors_list = constructors_data['MRData']['ConstructorTable']['Constructors'] if constructors_data else []

# Circuitos
circuits_data = fetch_ergast_data("2024/circuits.json")
circuits_list = circuits_data['MRData']['CircuitTable']['Circuits'] if circuits_data else []

# Convertir los datos a DataFrames para análisis
drivers_df = pd.DataFrame(drivers_list)
constructors_df = pd.DataFrame(constructors_list)
circuits_df = pd.DataFrame(circuits_list)

# Guardar en archivos CSV para su posterior análisis
drivers_df.to_csv("drivers_2024.csv", index=False)
constructors_df.to_csv("constructors_2024.csv", index=False)
circuits_df.to_csv("circuits_2024.csv", index=False)

print("Datos guardados como CSV")
