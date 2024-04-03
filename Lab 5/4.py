import pandas as pd
import json

def json_2_pdf(path: str):
    with open(path, "r", encoding="utf-8") as file:
        df = pd.DataFrame(json.load(file))
    df.to_csv(path.replace(".json", ".csv"), index=False)

json_2_pdf(input("json_2_pdf: "))