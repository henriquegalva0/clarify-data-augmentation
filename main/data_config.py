import pandas as pd
from datasets import load_dataset

target_label="Partial/half-answer"

dataset = load_dataset("ailsntua/QEvasion", split='train')

full_dataset = dataset.to_pandas()

parsed_dataset = full_dataset[["interview_question", "interview_answer", "evasion_label"]]

fewshot_dataset = parsed_dataset[parsed_dataset["evasion_label"] == target_label]
fewshot_dataset.reset_index(drop=True, inplace=True)

print(fewshot_dataset,parsed_dataset["evasion_label"].value_counts())

#print(full_dataset["president"].value_counts())

#Explicit               1052
#Dodging                 706
#Implicit                488
#General                 386
#Deflection              381
#Declining to answer     145
#Claims ignorance        119
#Clarification            92
#Partial/half-answer      79