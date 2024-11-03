# Importar bibliotecas necessárias
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Carregar os dados históricos (exemplo)
# Suponha que você tenha um CSV com dados históricos
data = pd.read_csv('historical_weather_data.csv')  # Certifique-se de ter um arquivo CSV com seus dados históricos

# Pré-processamento dos dados
X = data[['humidity']].values  # Usando umidade como entrada
y = data['temperature'].values  # Usando temperatura como saída

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construir o modelo
model = Sequential()
model.add(Dense(64, input_dim=1, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compilar o modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinar o modelo
model.fit(X_train, y_train, epochs=50, batch_size=10, validation_data=(X_test, y_test))

# Salvar o modelo
model.save('weather_prediction_model.h5')
