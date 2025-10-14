from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from data_config import fewshot_dataset
import pandas as pd
from random import randint
import json

naming_samples_index=""

def exemplo_alvo():
    global naming_samples_index 

    max_length=fewshot_dataset["evasion_label"].count()
    num=randint(0,max_length-1)
    row_data = fewshot_dataset.iloc[num]
    naming_samples_index=naming_samples_index+str(num)
    
    return str("{{" + f'"interview_question": "{row_data["interview_question"]}", "interview_answer": "{row_data["interview_answer"]}", "evasion_label": "{row_data["evasion_label"]}"' + "}}")

with open("clarify-data-augmentation/main/prompt.txt","r",encoding="utf-8") as prompt_txt:
    template_prompt = prompt_txt.read()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key="CHANGEME"
)

template_text = (template_prompt)
prompt = PromptTemplate(
    input_variables=["exemplo1", "exemplo2", "exemplo3"],
    template=template_text
)

qa_chain = prompt | llm | StrOutputParser()

resposta = qa_chain.invoke({
    "exemplo1": exemplo_alvo(),
    "exemplo2": exemplo_alvo(),
    "exemplo3": exemplo_alvo()
})
output=resposta.replace("```","").replace("json","")
dict_data = json.loads(output)
new_data = pd.DataFrame(dict_data)
new_data.to_csv(f'newdata{naming_samples_index}.csv', index=False, encoding='utf-8')