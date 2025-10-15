import pandas as pd
from datasets import load_dataset

target_label="Partial/half-answer"

dataset = load_dataset("ailsntua/QEvasion", split='train')

full_dataset = dataset.to_pandas()

parsed_dataset = full_dataset[["interview_question", "interview_answer", "evasion_label"]]
parsed_dataset.to_csv("augmented_dataset.csv",index=False)