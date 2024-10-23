from flask import Flask, request
import requests
from datetime import datetime
import pytz
import json
from collections import OrderedDict

app = Flask(__name__)

# Função utilizada para converter de UTC para America/Sao_Paulo
def converter_para_fuso_horario(horario_utc, fuso_horario):

    horario_utc = datetime.strptime(horario_utc, '%I:%M:%S %p')
    fuso_utc = pytz.timezone('America/Sao_Paulo')
    horario_com_fuso_utc = fuso_utc.localize(horario_utc)
    
    fuso_destino = pytz.timezone(fuso_horario)

    horario_completo = horario_com_fuso_utc.astimezone(fuso_destino).strftime('%I:%M:%S %p')
    horario_sem_segundos = horario_com_fuso_utc.astimezone(fuso_destino).strftime('%I:%M %p')

    return horario_completo.lstrip("0"), horario_sem_segundos.lstrip("0")

# Define a rota /plan-activity utilizando o metodo POST
@app.route('/plan-activity', methods=['POST'])

# Extrai os dados da requisição JSON
def planejar_atividade():
    dados = request.get_json()
    latitude = dados.get('latitude')
    longitude = dados.get('longitude')
    data = dados.get('date')

    # Faz a requisição na API externa
    url_api = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date={data}&formatted=1"
    resposta = requests.get(url_api)

    # Respostas da API em JSON
    dados_sol = resposta.json().get('results')
    nascer_sol_utc = dados_sol.get('sunrise')
    por_sol_utc = dados_sol.get('sunset')

    # Conversão para o fuso horário local
    nascer_sol_completo, nascer_sol_sem_segundos = converter_para_fuso_horario(nascer_sol_utc, 'America/Sao_Paulo')
    por_sol_completo, por_do_sol_sem_segundos = converter_para_fuso_horario(por_sol_utc, 'America/Sao_Paulo')

    atividades = [
        f"Caminhada ao nascer do sol às {nascer_sol_sem_segundos}",
        "Piquenique durante o dia",
        f"Fotografia ao pôr do sol às {por_do_sol_sem_segundos}",
        "Observação de estrelas após o pôr do sol"
    ]

# Monta a resposta final em JSON, mantendo a ordem da forma solicitada
    resposta_final = OrderedDict({
        "sunrise": nascer_sol_completo,
        "sunset": por_sol_completo,
        "activities": atividades
    })

    # Retorna a resposta em formato JSON
    return app.response_class(
        response=json.dumps(resposta_final),
        mimetype='application/json'
    )

app.run(debug=True)
