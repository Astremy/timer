from pypresence import Presence
from datetime import datetime
import time

client_id = '647842390089924619'
RPC = Presence(client_id)
RPC.connect()

event = datetime(2020,1,1)

#start_time = time.time()

while True:
    now = datetime.now()
    td = event - now

    date = {}

    date["jours"] = td.days
    date["h"] = td.seconds // 3600
    date["mins"] = td.seconds // 60 % 60
    date["s"] = td.seconds % 60

    etat = []

    for i,j in date.items():
        if j:
            etat.append(f"{j} {i}")

    state = ", ".join(etat[:-1])
    
    if len(etat) > 1:
        state += f" et {etat[-1]}"
    else:
        state = etat[-1]

    RPC.update(details = "Attends la nouvelle année", state = state, large_image = "rem")#, start=start_time)

    time.sleep(1)
    
