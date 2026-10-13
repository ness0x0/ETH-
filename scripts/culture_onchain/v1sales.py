import sys, datetime as dt, collections, bisect
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow
from keccak import keccak256
rpc=RPC(min_interval=0.3)
V1='0x6ba6f2207e343923ba692e5cae646fb0f566db8d'
PB='0x'+keccak256(b'PunkBought(uint256,uint256,address,address)').hex()
print('query_time_utc', utcnow(), 'weekday 2026-07-09:', dt.date(2026,7,9).strftime('%A'))
latest=rpc.block_number(); start=latest-1_100_000
anch=list(range(start,latest+1,100_000))+[latest]
T=[int(rpc.call('eth_getBlockByNumber',[hex(b),False])['timestamp'],16) for b in anch]
def bdate(b):
    i=max(1,min(len(anch)-1,bisect.bisect_left(anch,b))); b0,b1=anch[i-1],anch[i]
    return dt.datetime.fromtimestamp(T[i-1]+(b-b0)*(T[i]-T[i-1])/max(1,(b1-b0)),dt.timezone.utc)
L=rpc.get_logs(V1,[PB],start,latest,step=500_000)
print('PunkBought events on V1 contract last ~150 days:',len(L))
by=collections.Counter()
for l in L:
    pid=int(l['topics'][1],16); val=int(l['data'][2:66],16)/1e18
    to='0x'+l['topics'][3][-40:]; fr='0x'+l['topics'][2][-40:]
    d=bdate(int(l['blockNumber'],16)).date()
    by[d.strftime('%Y-%m')]+=1
    if val>0: by["paid_"+d.strftime("%Y-%m")]+=1
    if val>=10 or pid==2890: print(d, 'punk',pid,'value',val,'from',fr[:10],'to',to[:10])
print(dict(by))
