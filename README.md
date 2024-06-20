# SaYoPillow

SaYoPillow é um projeto que utiliza dados de um dispositivo IoT para monitorar e analisar a relação entre o sono e os níveis de estresse. Este projeto inclui uma aplicação interativa desenvolvida com Streamlit para visualizar os dados e extrair insights valiosos. Esta solução foi inicialmente desenvolvida por Laavanya Rachakonda Professora assistente da Universidade da Carolina do Norte. O desenvolvimento do nosso projeto foi voltado para estudos acadêmicos.

### Resumo do Projeto

O SaYoPillow é uma aplicação inovadora que integra tecnologias de IoT e machine learning para monitorar e analisar a qualidade do sono e os níveis de estresse dos usuários. Utilizando dados fisiológicos capturados por sensores, a aplicação realiza uma análise detalhada dos padrões de sono, identifica possíveis distúrbios e prevê níveis de estresse para o dia seguinte. As visualizações geradas pela aplicação, como gráficos de dispersão e histogramas, oferecem insights valiosos sobre a relação entre sono e estresse. Este projeto demonstra como tecnologias avançadas podem ser aplicadas para melhorar a saúde e o bem-estar das pessoas, proporcionando uma ferramenta poderosa para a gestão do sono e do estresse.proporcionando uma ferramenta poderosa para a gestão do sono e do estresse.

O dataset utilizado neste projeto foi extraído do Kaggle e pode ser acessado [aqui](https://www.kaggle.com/datasets/laavanya/human-stress-detection-in-and-through-sleep).

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
   git clone https://github.com/brunocordeirosantos/Sayopillow.git
   cd Sayopillow
Crie um ambiente virtual e ative-o:

### Copiar código

python -m venv venv
source venv/bin/activate # Para Windows, use `venv\Scripts\activate`

### Instale as dependências:

### Copiar código

pip install -r requirements.txt

### Executando a Aplicação
Para executar a aplicação Streamlit, utilize o comando abaixo:

streamlit run SayoPillow.py

### Acessando a Aplicação Online
Você pode acessar a aplicação diretamente através do link:
https://sayopillow.streamlit.app/?embed=true

### Estrutura do Repositório

.
├── .devcontainer
├── data
│   └── BaseSayoPillow.csv
├── LICENSE
├── README.md
├── SayoPillow.py
├── requirements.txt
└── streamlit_app.py

### Resultados
Correlação entre Horas de Sono e Nível de Estresse: Identificamos que a quantidade de sono tem uma correlação inversa com os níveis de estresse, destacando a importância de uma boa noite de sono.
Distribuição da Frequência Cardíaca: Analisamos as variações na frequência cardíaca durante a noite, que podem estar associadas a diferentes estágios do sono e níveis de estresse.

### Contribuições
Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request para melhorias.

### Licença
Este projeto está licenciado sob a Licença Apache 2.0 - veja o arquivo LICENSE para mais detalhes.

### Contato
Para mais informações, entre em contato através de [brunocordeirosantosbcs@gmail.com].
