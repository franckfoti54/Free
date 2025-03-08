from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI

from langchain_core.prompts import ChatPromptTemplate



llm = ChatOpenAI(model="gpt-4o-mini", api_key='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')   

# Create a chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
            [
                        ("system", "You are a geography expert that returns the colors present in a country's flag en francais."),
                                ("human", "France"),
                                        ("ai", "blue, white, red"),
                                                ("human", "{country}")
                                                    ]
            )

# Chain the prompt template and model, and invoke the chain
llm_chain = prompt_template | llm

country = "Cameroon"
response = llm_chain.invoke({"country": country})
print("les couleurs que l'on tetrouve sur le drapau de ce pays sont: "+response.content)
