# IMPORTAÇÃO DAS BIBLIOTECAS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os

# CARREGANDO AS VARIÁVEIS DE AMBIENTE
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")

#1 CRIAR O MODELO GROQ
llm = ChatGroq(
    model = "Gemma2-9b-It", # MODELO DE LLM UTILIZADO
    groq_api_key = groq_api_key, # CHAVE DE API DO GROQ
)

#2 PARSER DE SAÍDA : isso é necessário para que o sistema entenda a saída do modelo
parser = StrOutputParser()

#3 Prompt Template: Usando LCEL - Chain the Components
generic_template = "Traduza a seguinte frase em {language}"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", generic_template),
        ("user", "{text}")
    ]
)

# O que é uma chain? 
# Uma cadeia é uma sequência de componentes que são executados em ordem.

chain = prompt | llm | parser

# Executar a chain
print(chain.invoke({'language':'German', 'text':'Como você está?'}))