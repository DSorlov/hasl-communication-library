from hasl import *

api = haslapi()
tl2 = tl2api('')
ri4 = ri4api('', 0, 60)
si2 = si2api('', 0, "")

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


print("Completed.")
