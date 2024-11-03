import requests
import pandas as pd
import time

api_key = 'd763e4bd5b913259f481be9cc597ddf2'
city_name = 'São Paulo'
start_date = '2023-01-01'
end_date = '2023-05-01'

# Converter datas para timestamps
start_timestamp = int(time.mktime(time.strptime(start_date, '%Y-%m-%d')))
end_timestamp = int(time.mktime(time.strptime(end_date, '%Y-%m-%d')))

# Lista para armazenar os dados
data = []

# Loop através dos dias para coletar dados históricos
current_timestamp = start_timestamp
while current_timestamp <= end_timestamp:
    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=-23.5505&lon=-46.6333&dt={current_timestamp}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        for hourly_data in weather_data['hourly']:
            data.append({
                'date': time.strftime('%Y-%m-%d', time.localtime(hourly_data['dt'])),
                'temperature': hourly_data['temp'],
                'humidity': hourly_data['humidity']
            })
    else:
        print(f"Erro ao buscar dados para o timestamp: {current_timestamp}")

    # Avançar um dia (86400 segundos)
    current_timestamp += 86400

# Converter a lista de dados em um DataFrame
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('historical_weather_data.csv', index=False)
