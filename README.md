# Projeto Integrador: Monitoramento de Sensores com MQTT e Python

Este projeto foi desenvolvido como parte do **Curso Técnico em Desenvolvimento de Sistemas**, com o objetivo de criar uma solução completa de monitoramento de dados ambientais utilizando o protocolo **MQTT** para comunicação entre dispositivos e um banco de dados relacional para persistência.

## 🚀 Tecnologias Utilizadas

*   **Linguagem:** Python 3
*   **Protocolo de Comunicação:** MQTT (Message Queuing Telemetry Transport)
*   **Banco de Dados:** SQLAlchemy (MySQL/PostgreSQL)
*   **Visualização:** Streamlit / Dash
*   **Arquitetura:** Microserviços de coleta e API de consulta

## 🛠️ Funcionalidades

*   **Coleta em Tempo Real:** Recebimento de dados de sensores (temperatura, umidade, CO2, poeira, pressão e altitude).
*   **Processamento de Dados:** Tratamento de timestamps e conversão de unidades.
*   **API REST:** Endpoints para consulta histórica dos dados registrados.
*   **Dashboard Interativo:** Visualização gráfica dos dados coletados para análise em tempo real.

## 📂 Estrutura do Projeto

*   `main.py`: Ponto de entrada da aplicação e configuração do servidor.
*   `query.py`: Lógica de interação com o banco de dados.
*   `dash.py`: Interface de visualização dos dados.

## 🎓 Contexto Acadêmico

Este projeto demonstra a aplicação prática de conceitos de **IoT (Internet das Coisas)**, **Sistemas Distribuídos** e **Persistência de Dados**, fundamentais na formação de um Desenvolvedor de Sistemas.
