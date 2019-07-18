from hasl import *

api = haslapi()
tl2 = tl2api('')
ri4 = ri4api('', 0, 60)
si2 = si2api('', 0, "")
tp3 = tp3api('')
pu1 = pu1api('')

print("Testing pyHASL v" + api.version())

try:
    tl2.request()
    print("[TL2] OK")
except Exception as e:
    print("[TL2] Error: " + e.details)

try:
    ri4.request()
    print("[RI4] OK")
except Exception as e:
    print("[RI4] Error: " + e.details)

try:
    si2.request()
    print("[SI2] OK")
except Exception as e:
    print("[SI2] Error: " + e.details)

try:
    pu1.request('Slussen')
    print("[PU1] OK")
except Exception as e:
    print("[PU1] Error: " + e.details)

try:
    tp3.request(9192,9141,'','','','')
    print("[TP3] OK")
except Exception as e:
    print("[TP3] Error: " + e.details)

print("Completed.")
