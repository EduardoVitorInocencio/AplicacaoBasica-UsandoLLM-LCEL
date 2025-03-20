# Projeto: LangFlow - Superchatbot Integrado

## Índice
1. [Introdução](#introdução)
2. [Pré-requisitos](#pré-requisitos)
3. [Instalação](#instalação)
4. [Explicação do Código](#explicação-do-código)
5. [Glossário](#glossário)
6. [Como Contribuir](#como-contribuir)
7. [Licença](#licença)

## Introdução
LangFlow é um superchatbot projetado para integrar diversas ferramentas e APIs externas, permitindo automação de processos e respostas inteligentes. O projeto usa a biblioteca LangChain para estruturar interações com modelos de linguagem grande (LLMs).

## Pré-requisitos
Antes de iniciar, certifique-se de ter instalado:
- Python 3.8+
- pip
- Conta e chave de API da Groq

## Instalação
Para instalar e configurar o projeto, siga os passos abaixo:

1. Clone o repositório:
```sh
 git clone https://github.com/seu-usuario/langflow.git
```
2. Acesse o diretório do projeto:
```sh
 cd langflow
```
3. Crie um ambiente virtual (opcional, mas recomendado):
```sh
 python -m venv venv
 source venv/bin/activate  # Para Linux/Mac
 venv\Scripts\activate  # Para Windows
```
4. Instale as dependências:
```sh
 pip install -r requirements.txt
```
5. Configure suas variáveis de ambiente:
   - Crie um arquivo `.env`
   - Adicione sua chave de API:
     ```sh
     GROQ_API_KEY=sua_chave_aqui
     ```

## Explicação do Código

### 1. Importação das Bibliotecas
```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os
```
Essas bibliotecas são essenciais para o funcionamento do chatbot. `LangChain` é usado para estruturar a interação com o modelo, `dotenv` carrega as variáveis de ambiente e `os` manipula essas variáveis no código.

### 2. Carregamento das Variáveis de Ambiente
```python
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")
```
Aqui, o código busca a chave da API armazenada no arquivo `.env`.

### 3. Criação do Modelo LLM
```python
llm = ChatGroq(
    model="Gemma2-9b-It",
    groq_api_key=groq_api_key,
)
```
O objeto `llm` usa o modelo `Gemma2-9b-It` para processar textos.

### 4. Parser de Saída
```python
parser = StrOutputParser()
```
O `StrOutputParser` ajuda a interpretar e formatar a saída do modelo.

### 5. Definição do Template de Prompt
```python
generic_template = "Traduza a seguinte frase em {language}"

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_template),
    ("user", "{text}")
])
```
O template define como a entrada do usuário será formatada para o modelo de IA.

### 6. Definição da Chain
```python
chain = prompt | llm | parser
```
A `chain` une os componentes: entrada do usuário → modelo de IA → formatação da resposta.

### 7. Execução da Chain
```python
print(chain.invoke({'language':'German', 'text':'Como você está?'}))
```
Aqui, a chain recebe os parâmetros e retorna a tradução da frase.

## Glossário
- **LLM (Large Language Model):** Modelo de IA treinado para processar e gerar texto.
- **LangChain:** Framework para compor aplicações de IA usando LLMs.
- **Prompt Template:** Estrutura usada para padronizar entradas do usuário.
- **Chain:** Sequência de operações que processam e refinam os dados.
- **Parser:** Componente que interpreta e formata a saída do modelo.

## Como Contribuir
1. Faça um fork do repositório.
2. Crie uma branch para suas alterações:
   ```sh
   git checkout -b minha-feature
   ```
3. Faça commit das suas mudanças:
   ```sh
   git commit -m "Adicionei uma nova funcionalidade"
   ```
4. Envie as mudanças para o repositório:
   ```sh
   git push origin minha-feature
   ```
5. Crie um Pull Request.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

