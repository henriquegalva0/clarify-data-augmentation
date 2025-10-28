import os
import pandas as pd
from datasets import load_dataset

dataset = load_dataset("ailsntua/QEvasion", split='train')

full_dataset = dataset.to_pandas()

parsed_dataset = full_dataset[["interview_question", "interview_answer", "evasion_label"]]

if os.path.exists("clarify-data-augmentation/augmented_dataset.csv"):
    print("Augmented dataset already exists. Loading from 'augmented_dataset.csv'.")
else:
    parsed_dataset.to_csv("augmented_dataset.csv",index=False)