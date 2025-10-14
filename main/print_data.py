import pandas as pd

df = pd.read_csv("newdata85026.csv") 

for i in range(df["evasion_label"].count()):
    print(df['interview_question'].iloc[i])
    print("\n\n"+df['interview_answer'].iloc[i])
    print("\n\n"+df['evasion_label'].iloc[i])