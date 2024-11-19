import pandas as pd
import matplotlib.pyplot as plt


def procesar(df):

    df = df[ df['Glucose'] != 0]

    return df

def mostrar_datos(df):

    datos_nulos = df.isnull().sum()

    print(datos_nulos)

    maximos = df.apply(lambda col: col.max())
    print(maximos)

    datos_0 = df.apply(lambda col: (col == 0).sum())

    print(datos_0)


    print(df.corr())

    df = df.sort_values(by='Glucose')

    diabeticos = df[ df['Outcome'] == 1]
    no_diabeticos = df[ df['Outcome'] == 0]


    plt.boxplot([diabeticos.Glucose, no_diabeticos.Glucose], labels=['diabeticos', 'nos diabeticos'])
    plt.title('glucosa')
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('./diabetes.csv')

    df = procesar(df)
    mostrar_datos(df)