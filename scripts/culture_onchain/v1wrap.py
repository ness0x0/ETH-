import sys, json, datetime as dt, collections, bisect
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow, TRANSFER_TOPIC
rpc=RPC(min_interval=0.3)
ZERO='0x'+'0'*64
print('query_time_utc', utcnow())
anch=list(range(13_600_000,26_200_001,250_000))
T=[]
for b in anch:
    x=rpc.call('eth_getBlockByNumber',[hex(min(b,26_186_000)),False]); T.append(int(x['timestamp'],16))
def bdate(b):
    i=max(1,min(len(anch)-1,bisect.bisect_left(anch,b)))
    b0,b1=anch[i-1],anch[i]; t=T[i-1]+(b-b0)*(T[i]-T[i-1])/(b1-b0)
    return dt.datetime.fromtimestamp(t,dt.timezone.utc)
for name,addr in [('WPV1 new 0x282b','0x282bdd42f4eb70e7a9d9f40c8fea0825b7f68c5d'),('WPUNKS1 old 0xf4a4','0xf4a4644e818c2843ba0aabea93af6c80b5984114')]:
    M=rpc.get_logs(addr,[TRANSFER_TOPIC,ZERO],13_600_000,26_186_000,step=2_000_000)
    B=rpc.get_logs(addr,[TRANSFER_TOPIC,None,ZERO],13_600_000,26_186_000,step=2_000_000)
    print(name,'mints(wraps)',len(M),'burns(unwraps)',len(B))
    if M: print(' first wrap', bdate(int(M[0]['blockNumber'],16)).date(), 'last wrap', bdate(int(M[-1]['blockNumber'],16)).date())
    if B: print(' first unwrap', bdate(int(B[0]['blockNumber'],16)).date(), 'last unwrap', bdate(int(B[-1]['blockNumber'],16)).date())
    mm=collections.Counter(); bb=collections.Counter()
    for l in M: mm[bdate(int(l['blockNumber'],16)).strftime('%Y-%m')]+=1
    for l in B: bb[bdate(int(l['blockNumber'],16)).strftime('%Y-%m')]+=1
    ks=sorted(set(mm)|set(bb))
    print(' month wraps/unwraps:', ' '.join(f"{k}:{mm[k]}/{bb[k]}" for k in ks))
