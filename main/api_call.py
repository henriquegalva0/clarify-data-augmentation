from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import pandas as pd
from random import randint
import json

from load_data import parsed_dataset

def target_sample(fewshot_dataset): 
    max_length=fewshot_dataset["evasion_label"].count()
    num=randint(0,max_length-1)
    row_data = fewshot_dataset.iloc[num]
    
    return str("{{" + f'"interview_question": "{row_data["interview_question"]}", "interview_answer": "{row_data["interview_answer"]}", "evasion_label": "{row_data["evasion_label"]}"' + "}}")

with open("clarify-data-augmentation/main/prompt.txt","r",encoding="utf-8") as prompt_txt:
    template_prompt = prompt_txt.read()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.45,
    google_api_key="CHANGEME"
)

template_text = (template_prompt)
prompt = PromptTemplate(
    input_variables=["sample1", "sample2", "sample3", "sample4", "sample5"],
    template=template_text
)

qa_chain = prompt | llm | StrOutputParser()

def generate_data(target_label):
    
    fewshot_dataset = parsed_dataset[parsed_dataset["evasion_label"] == target_label]
    fewshot_dataset.reset_index(drop=True, inplace=True)
    
    resposta = qa_chain.invoke({
        "sample1": target_sample(fewshot_dataset),
        "sample2": target_sample(fewshot_dataset),    
        "sample3": target_sample(fewshot_dataset),
        "sample4": target_sample(fewshot_dataset),
        "sample5": target_sample(fewshot_dataset)
    })
    output=resposta.replace("```","").replace("json","")

    dict_data = json.loads(output)
    
    return pd.DataFrame(dict_data)
