import sys, json, datetime as dt, collections
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow, TRANSFER_TOPIC
rpc=RPC(min_interval=0.5)
ZERO='0x'+'0'*64
def ts(bn):
    b=rpc.call('eth_getBlockByNumber',[hex(bn),False]); return dt.datetime.fromtimestamp(int(b['timestamp'],16),dt.timezone.utc)
print('query_time_utc', utcnow())
TF='0x4e1f41613c9084fdb9e34e11fae9412427480e56'
M=rpc.get_logs(TF,[TRANSFER_TOPIC,ZERO],13_600_000,26_186_000,step=2_000_000)
print('Terraforms mints',len(M))
bl=sorted(int(l['blockNumber'],16) for l in M)
print('first',bl[0],ts(bl[0]).isoformat(),'last',bl[-1],ts(bl[-1]).isoformat())
# deciles
for q in [0.1,0.5,0.9,0.99]:
    b=bl[int(q*len(bl))-1]; print('q',q,b,ts(b).date())
# mints after first 30 days
late=[b for b in bl if b>bl[0]+200_000]
print('mints >~30 days after first:', len(late), (ts(late[0]).date() if late else None), (ts(late[-1]).date() if late else None))
