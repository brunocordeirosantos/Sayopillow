# SaYoPillow

SaYoPillow é um projeto que utiliza dados de um dispositivo IoT para monitorar e analisar a relação entre o sono e os níveis de estresse. Este projeto inclui uma aplicação interativa desenvolvida com Streamlit para visualizar os dados e extrair insights valiosos.

## Descrição do Projeto

A SaYoPillow ajuda a entender a relação entre estresse e sono através da análise de parâmetros fisiológicos como faixa de ronco, taxa de respiração, temperatura corporal, movimento dos membros, níveis de oxigênio no sangue, movimento dos olhos, horas de sono e frequência cardíaca.

## Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Seaborn
- Matplotlib

## Como Executar o Projeto

### Pré-requisitos

- Python 3.7 ou superior

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/teste.git
   cd teste
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate # Para Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Executando a Aplicação

Para executar a aplicação Streamlit, utilize o comando abaixo:
```bash
streamlit run SayoPillow.py
```

### Acessando a Aplicação Online

Você pode acessar a aplicação diretamente através do link:
(https://sayopillow.streamlit.app/?embed=true)

## Estrutura do Repositório

```
.
├── .devcontainer
├── data
│   └── BaseSayoPillow.csv
├── LICENSE
├── README.md
├── SayoPillow.py
├── requirements.txt
└── streamlit_app.py
```

## Resultados

- **Correlação entre Horas de Sono e Nível de Estresse:** Identificamos que a quantidade de sono tem uma correlação inversa com os níveis de estresse, destacando a importância de uma boa noite de sono.
- **Distribuição da Frequência Cardíaca:** Analisamos as variações na frequência cardíaca durante a noite, que podem estar associadas a diferentes estágios do sono e níveis de estresse.

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request para melhorias.

## Licença

Este projeto está licenciado sob a Licença Apache 2.0 - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato através de [brunocordeirosantosbcs@gmail.com].
```
