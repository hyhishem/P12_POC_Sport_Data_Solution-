import pandas as pd
import json
import re
from datetime import datetime

with open("input.json", "r") as f:
  data_str = f.read()
cleaned_str = (
  data_str.replace("key:", '"key":')
  .replace("value:", '"value":')
  .replace("topic:", '"topic":')
  .replace("headers:", '"headers":')
  .replace("partition:", '"partition":')
  .replace("timestamp:", '"timestamp":"')
  .replace(",offset:", '","offset":')
  .replace('\\"', "'")
)

# 2. Charger le dictionnaire principal
data_dict = json.loads(cleaned_str)

record = data_dict["value"]
record = json.loads(record.replace("'", '"'))


message = f"{record['prenom']}  {record['nom']} a fait {record['duration_minutes']} minutes de {record['type_sport']}"


with open("output.txt", "w") as f:
  f.write(message)
