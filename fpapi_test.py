from hasl import *

api = fpapi()

for traffic in ('PT','RB','TVB','SB','LB','SpvC','TB1','TB2','TB3'):
    try:
        print("["+traffic+"] OK")
    except Exception as e:
        print("["+traffic+"] Error: " + e.details)
