import pandas as pd
from api_call import generate_data

augmented_dataset=pd.read_csv("augmented_dataset.csv")

for label,value in (augmented_dataset["evasion_label"].value_counts()).items():
    if int(value)<1052:
        while len(augmented_dataset[augmented_dataset["evasion_label"]==label]) < 1052:
            new_data=generate_data(label)
            augmented_dataset = pd.concat([augmented_dataset, new_data], ignore_index=True)
            new_data.to_csv("augmented_dataset.csv", mode='a', header=False, index=False)
            augmented_dataset=pd.read_csv("augmented_dataset.csv")
            
            print(augmented_dataset["evasion_label"].value_counts())

#Explicit               1052
#Dodging                 706
#Implicit                488
#General                 386
#Deflection              381
#Declining to answer     145
#Claims ignorance        119
#Clarification            92
#Partial/half-answer      79