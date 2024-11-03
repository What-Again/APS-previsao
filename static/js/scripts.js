// Chave da API disponibilizada pelo site OpenWeatherMap
const key = "d763e4bd5b913259f481be9cc597ddf2";

// Função para inserir dados climáticos na página
function insereDados(dados) {
    // Atualiza o nome da cidade no HTML
    document.querySelector(".cidade").innerHTML = "Tempo em " + dados.name;
    // Atualiza a temperatura no HTML
    document.querySelector(".temp").innerHTML = "Temperatura em " + Math.floor(dados.main.temp) + "°C";
    // Atualiza a descrição do clima no HTML
    document.querySelector(".texto-previsao").innerHTML = dados.weather[0].description;
    // Atualiza a umidade no HTML
    document.querySelector(".umidade-valor").innerHTML = dados.main.humidity + "%";
    // Atualiza a imagem de previsão do tempo no HTML
    document.querySelector(".img-previsao").src = `https://openweathermap.org/img/wn/${dados.weather[0].icon}.png`;
}

// Adiciona um evento de clique ao botão de busca
document.querySelector(".botao-buscar").addEventListener("click", async function() {
    // Captura o nome da cidade inserido pelo usuário
    const cidade = document.querySelector(".input-cidade").value;
    // Chama a função para buscar dados climáticos para a cidade
    await buscaCidade(cidade);
});

async function buscaCidade(cidade) {
    // Buscar os dados meteorológicos atuais da cidade
    const dados = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cidade}&appid=${key}&lang=pt_br&units=metric`).then(resposta => resposta.json());
    console.log(dados);
    // Inserir os dados climáticos atuais na página
    insereDados(dados);

    // Extrair a umidade dos dados obtidos
    const umidade = dados.main.humidity;
    
    // Enviar a umidade para o servidor Python e obter a previsão de temperatura
    const response = await fetch('http://localhost:5000/predict_temperature', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ humidity: umidade })
    });

    // Converter a resposta em JSON
    const previsao = await response.json();
    console.log('Previsão de temperatura:', previsao);

    // Atualizar a previsão de temperatura na página
    document.querySelector('.temp-previsao').innerHTML = `Previsão de Temperatura: ${previsao.temperature}°C`;
}