import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración inicial de visualización
sns.set(style="whitegrid")

# 1. Carga de Datos
drivers_df = pd.read_csv("drivers_2024.csv")
constructors_df = pd.read_csv("constructors_2024.csv")
circuits_df = pd.read_csv("circuits_2024 .csv")

# 2. Exploración de los Datos
print("Datos de Pilotos")
print(drivers_df.head())
print("\nDatos de Equipos")
print(constructors_df.head())
print("\nDatos de Circuitos")
print(circuits_df.head())

# 3. Limpieza y Preprocesamiento (si es necesario)
# Aquí podrías realizar operaciones de limpieza como eliminar duplicados,
# verificar valores nulos o normalizar columnas si es necesario.
# Por ejemplo, revisaremos valores nulos en cada dataframe:
print("\nValores Nulos en Pilotos:", drivers_df.isnull().sum())
print("\nValores Nulos en Equipos:", constructors_df.isnull().sum())
print("\nValores Nulos en Circuitos:", circuits_df.isnull().sum())

# 4. Análisis y Visualizaciones

# Análisis de Pilotos por Equipo
# Ver cuántos pilotos hay por equipo
if 'constructorId' in drivers_df.columns:
    pilot_count_by_team = drivers_df['constructorId'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=pilot_count_by_team.index, y=pilot_count_by_team.values, palette="viridis")
    plt.title("Número de Pilotos por Equipo en 2021")
    plt.xlabel("Equipo")
    plt.ylabel("Cantidad de Pilotos")
    plt.xticks(rotation=45)
    plt.show()

# Distribución de Circuitos por País
# Graficar cuántos circuitos hay por país
if 'Location.country' in circuits_df.columns:
    circuits_by_country = circuits_df['Location.country'].value_counts()
    plt.figure(figsize=(12, 8))
    sns.barplot(x=circuits_by_country.index, y=circuits_by_country.values, palette="cubehelix")
    plt.title("Cantidad de Circuitos por País en 2021")
    plt.xlabel("País")
    plt.ylabel("Cantidad de Circuitos")
    plt.xticks(rotation=90)
    plt.show()

# Estadísticas Descriptivas de los Pilotos
# Revisamos la nacionalidad de los pilotos y su distribución
if 'nationality' in drivers_df.columns:
    plt.figure(figsize=(12, 8))
    sns.countplot(data=drivers_df, y='nationality', order=drivers_df['nationality'].value_counts().index, palette="magma")
    plt.title("Distribución de Nacionalidades de Pilotos en 2021")
    plt.xlabel("Cantidad de Pilotos")
    plt.ylabel("Nacionalidad")
    plt.show()

# Análisis de Equipos (Constructores)
# Aquí podemos ver la distribución de nacionalidades de los equipos
if 'nationality' in constructors_df.columns:
    plt.figure(figsize=(8, 6))
    sns.countplot(data=constructors_df, y='nationality', palette="coolwarm")
    plt.title("Nacionalidad de los Equipos de F1 en 2021")
    plt.xlabel("Cantidad de Equipos")
    plt.ylabel("Nacionalidad")
    plt.show()

# Estadísticas Descriptivas Generales
# Información resumida de los pilotos, equipos y circuitos
print("\nResumen Estadístico de Pilotos:")
print(drivers_df.describe(include='all'))

print("\nResumen Estadístico de Equipos:")
print(constructors_df.describe(include='all'))

print("\nResumen Estadístico de Circuitos:")
print(circuits_df.describe(include='all'))
