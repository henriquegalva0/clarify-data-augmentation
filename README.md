to run the code, clone the repository
```
git init
git clone https://github.com/henriquegalva0/clarify-data-augmentation.git
```
create your venv, activate it and download all requirements
```
python3 -m venv .venv
.venv/Scripts/Activate.ps1
pip install -r requirements.txt
```
type your own google api key at [api_call.py](main/api_call.py)
```
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key="CHANGEME" <--- API KEY
)
```
choose your target label at [data_config.py](main/data_config.py)
```
target_label="Partial/half-answer"
```
run [api_call.py](main/api_call.py). The new data will be in a .csv file that you can print while running [main/print_data.py](print_data.py)
```
df = pd.read_csv("CHANGEME.csv") <--- change this corresponding to your output
```
