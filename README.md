# Setup & Running
To run the code, the first step is to clone the repository.
```
git init
git clone https://github.com/henriquegalva0/clarify-data-augmentation.git
```
After that, create and activate your venv, then download all requirements.
```
python3 -m venv .venv
.venv/Scripts/Activate.ps1
pip install -r requirements.txt
```
Type your own google api key at [api_call.py](main/api_call.py) by changing the content of _google_api_key_:
```
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key="CHANGEME" <--- API KEY
)
```
Run the script [main.py](main/main.py) and you're ready to augmentate the dataset!

## Disclaimers
Be careful! If you are trying to run the code for the second time and have already created/updated the file [augmented_dataset.csv](augmented_dataset.csv) with new data, **remove** the following line inside [load_data.py](main/load_data.py) or else you're losing the data you have just created:
```
parsed_dataset.to_csv("augmented_dataset.csv",index=False)
```
Also, if you want to generate more than 1052 data per label, consider changing the target size threshold number in the following line from [main.py](main/main.py):
```
data_size_target=int(1052) <--- Target size by label
```

## Notes
* More info about the SemEval's Task can be obtained on [CLARITY-SemEval-2026](https://konstantinosftw.github.io/CLARITY-SemEval-2026/).
* The file [augmented_dataset.csv](augmented_dataset.csv) is the augmented version of the original dataset [QEvasion](https://huggingface.co/datasets/ailsntua/QEvasion).
* To edit the prompt used to generate [augmented_dataset.csv](augmented_dataset.csv), just modify the file [prompt.txt](main/prompt.txt).
