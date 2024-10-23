# 🌅 Planejamento de Atividades com Horário Solar

Este projeto é uma aplicação web desenvolvida em **Flask** que fornece sugestões de atividades ao ar livre com base nos horários de nascer e pôr do sol para uma localização e data especificadas.

## 🚀 Sobre o Projeto

A aplicação permite o planejamento de atividades como caminhadas, piqueniques, e observação de estrelas, ajustando os horários das atividades de acordo com o fuso horário desejado. Para isso, o sistema consulta uma API externa para obter os horários do nascer e pôr do sol com base nas coordenadas geográficas fornecidas.

### Funcionalidades:

- Consultar o nascer e pôr do sol de uma localização especificada.
- Converter os horários para o fuso horário desejado.
- Gerar sugestões de atividades ao ar livre.

## 💻 Tecnologias Utilizadas

### Back-end

- **Python**: Linguagem utilizada para construir a aplicação.
- **Flask**: Framework web utilizado para desenvolver a aplicação.
- **Requests**: Para realizar requisições HTTP à API de terceiros.
- **Pytz**: Biblioteca para conversão de fusos horários.

### API Utilizada

- **Sunrise-Sunset API**: Utilizada para consultar os horários de nascer e pôr do sol com base nas coordenadas geográficas.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/projeto-sunrise
    ```

2. **Entre no diretório do projeto:**

    ```bash
    cd projeto-sunrise
    ```

3. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

4. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Execute a aplicação:**

    ```bash
    python app.py
    ```

A aplicação estará disponível em `localhost:5000`.

### Exemplo de Requisição:

Você pode testar o projeto utilizando uma ferramenta como **Postman** ou a extensão **Thunder Client** no VSCode.

**Exemplo de requisição POST:**

```json
POST http://127.0.0.1:5000/plan-activity
Content-Type: application/json

{
  "latitude": 36.7201600,
  "longitude": -4.4203400,
  "date": "2021-12-25"
}
```
**Exemplo de Resposta:**

```
{
  "sunrise": "7:26:47 AM",
  "sunset": "5:08:55 PM",
  "activities": [
    "Caminhada ao nascer do sol às 7:26 AM",
    "Piquenique durante o dia",
    "Fotografia ao pôr do sol às 5:08 PM",
    "Observação de estrelas após o pôr do sol"
  ]
}
```
## 📧 Contato

Este é um projeto feito para um desafio de estágio, mas está aberto para qualquer ideia, melhoria e funcionalidade nova.

Para mais informações ou dúvidas, entre em contato:

- **LinkedIn:** [Lucas Ribeiro Arruda](https://www.linkedin.com/in/lucasaarruda/)

Obrigado por conferir o projeto! 