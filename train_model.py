import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Ler os dados históricos do arquivo CSV
data = pd.read_csv('historical_weather_data.csv')

# Preparar os dados para treinamento
# X será a umidade (feature) e y será a temperatura (target)
X = data[['humidity']]  # Usando a umidade como feature
y = data['temperature']  # Usando a temperatura como target

# Dividir os dados em conjuntos de treinamento e teste
# 80% para treinamento e 20% para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões nos dados de teste
y_pred = model.predict(X_test)

# Avaliar o modelo usando o Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Salvar o modelo treinado para uso futuro
joblib.dump(model, 'weather_prediction_model.pkl')
print("Modelo treinado e salvo com sucesso!")
