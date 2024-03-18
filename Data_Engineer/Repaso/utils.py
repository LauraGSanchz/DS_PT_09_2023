import pandas as pd
import matplotlib as plt
import seaborn as sns

def explore_data(df):
    print('-------'*100)
    print('Data Set Shape:',df.shape)
    print('-------'*100)
    print('Data Columns list:',df.columns)
    print('-------'*100)
    print('Null data:',df.isna().sum())
    print('-------'*100)
    df.info()


def duplicated_info(df, sort_by=None):
    print(df.duplicated().sum())
    print(df.duplicated().value_counts())
    
    if sort_by:
        duplicated_rows = df[df.duplicated()].sort_values(by=sort_by)
    else:
        duplicated_rows = df[df.duplicated()]
    
    return duplicated_rows

def explore_data2(data):
    """
    Función para explorar los datos cargados.
    """
    # Muestra las primeras filas del DataFrame
    print("Primeras filas del DataFrame:")
    print(data.head())

    # Información sobre las columnas y tipos de datos
    print("\nInformación del DataFrame:")
    print(data.info())

    # Resumen estadístico de las variables numéricas
    print("\nResumen estadístico de variables numéricas:")
    print(data.describe())

    # Resumen de las variables categóricas
    print("\nResumen de variables categóricas:")
    print(data.describe(include='object'))

    # Resumen de los tipos de variables
    print("\nResumen de tipos de variables:")
    print(data.dtypes)


def data_report(df):
    '''Esta funcion describe los campos de un dataframe de pandas de forma bastante clara, crack'''
    # Sacamos los NOMBRES
    cols = pd.DataFrame(df.columns.values, columns=["COL_N"])

    # Sacamos los TIPOS
    types = pd.DataFrame(df.dtypes.values, columns=["DATA_TYPE"])

    # Sacamos los MISSINGS
    percent_missing = round(df.isnull().sum() * 100 / len(df), 2)
    percent_missing_df = pd.DataFrame(percent_missing.values, columns=["MISSINGS (%)"])

    # Sacamos los VALORES UNICOS
    unicos = pd.DataFrame(df.nunique().values, columns=["UNIQUE_VALUES"])
    
    percent_cardin = round(unicos['UNIQUE_VALUES']*100/len(df), 2)
    percent_cardin_df = pd.DataFrame(percent_cardin.values, columns=["CARDIN (%)"])

    concatenado = pd.concat([cols, types, percent_missing_df, unicos, percent_cardin_df], axis=1, sort=False)
    concatenado.set_index('COL_N', drop=True, inplace=True)


    return concatenado.T



def plot_distribution(data, column):
    """
    Función para trazar la distribución de una columna.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribución de {column}')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    return plt.show()

def plot_correlation_heatmap(data):
    """
    Función para trazar un mapa de calor de correlación.
    """
    # Create a mask to hide the upper triangle (including the diagonal)
    mask = np.tri(corr_matrix.shape[0], k=-1, dtype=bool)
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.corr(), annot=True, mask=mask,cmap='coolwarm', fmt=".2f")
    plt.title('Mapa de calor de correlación')
    plt.show()




def plot_distribution(data, column):
    """
    Función para trazar la distribución de una columna.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribución de {column}')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    plt.show()

def plot_correlation_heatmap(data):
    """
    Función para trazar un mapa de calor de correlación.
    """
    # Create a mask to hide the upper triangle (including the diagonal)
    mask = np.tri(corr_matrix.shape[0], k=-1, dtype=bool)
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.corr(), annot=True, mask=mask,cmap='coolwarm', fmt=".2f")
    plt.title('Mapa de calor de correlación')
    plt.show()