import json

data = []
with open("input.json", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            data.append(json.loads(line))

messages = []
for record in data:
    value = json.loads(record["value"])  
    msg = (
        f"{value['prenom']} {value['nom']} a fait "
        f"{value['duration_minutes']} minutes de {value['type_sport']}"
    )
    messages.append(msg)

with open("output.txt", "w") as f:
    f.write("\n".join(messages))
