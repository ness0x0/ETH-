import sys, json, datetime as dt, collections
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow, TRANSFER_TOPIC
rpc=RPC(min_interval=0.4)
ZERO='0x'+'0'*64
AB='0x059edd72cd353df5106d2b9cc5ab83a52287ac3a'
print('query_time_utc', utcnow())
L=rpc.get_logs(AB,[TRANSFER_TOPIC,ZERO],11_300_000,26_186_000,step=2_000_000)
print('mint logs',len(L))
sq=[(int(l['topics'][3],16),int(l['blockNumber'],16)) for l in L if int(l['topics'][3],16)<10000]
print('squiggle mints',len(sq))
# block->year mapping via sample timestamps
cache={}
def ts(bn):
    if bn not in cache:
        b=rpc.call('eth_getBlockByNumber',[hex(bn),False]); cache[bn]=dt.datetime.fromtimestamp(int(b['timestamp'],16),dt.timezone.utc)
    return cache[bn]
sq.sort(key=lambda x:x[1])
print('first', sq[0], ts(sq[0][1]).isoformat(), 'last', sq[-1], ts(sq[-1][1]).isoformat())
# mints after 2021-12-31 
late=[x for x in sq if x[1]>13_916_000]
print('mints after block 13916000 (~2022-01-01):', len(late))
for t,b in late[:40]: print(t,b,ts(b).date())
# count by bands
import bisect
for bnd,label in [(11_600_000,'<~2021-01-06'),(12_000_000,'<~2021-03-08'),(13_000_000,'<~2021-08-10'),(13_916_000,'<2022-01-01')]:
    print(label, sum(1 for x in sq if x[1]<bnd))
print('----- late mint detail by date and recipient')
rec=collections.Counter(); bydate=collections.Counter()
for l in L:
    t=int(l['topics'][3],16); b=int(l['blockNumber'],16)
    if t<10000 and b>13_916_000:
        d=ts(b).date().isoformat()
        bydate[d]+=1; rec[l['topics'][2][-40:]]+=1
for d in sorted(bydate): print(d, bydate[d])
print(rec.most_common(10))
