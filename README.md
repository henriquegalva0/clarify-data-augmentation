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
Type your own google API keys at [api_call.py](main/api_call.py) by removing, adding or changing keys on _api_keys_:
```
google_target_api_key=0
api_keys=[
    "CHANGEME1",     <--- API KEY
    "CHANGEME2",     <--- API KEY
    "CHANGEME3"      <--- API KEY
    ]
```
Run the script [main.py](main/main.py) and you're ready to augmentate the dataset!

## Disclaimers
Be careful! If you're trying to run the code for the second time and have already created/updated _augmented_dataset.csv_ with new data, **do not edit the name of this file** or else when running the script, the progress made **will not be considered**.
```
if os.path.exists("clarify-data-augmentation/augmented_dataset.csv"):
    print("Augmented dataset already exists. Loading from 'augmented_dataset.csv'.")
else:
    parsed_dataset.to_csv("augmented_dataset.csv",index=False)    <--- New augmentation from the scratch
```
Also, if you want to generate more than 1052 data per label, consider changing the target size threshold number in the following line from [main.py](main/main.py):
```
data_size_target=int(1052)    <--- Target size by label
```

## Notes
* More info about the SemEval's Task can be obtained on [CLARITY-SemEval-2026](https://konstantinosftw.github.io/CLARITY-SemEval-2026/).
* To edit the prompts used, just modify the *.txt* files on [prompts](main/prompts/). Each file corresponds to each class.
