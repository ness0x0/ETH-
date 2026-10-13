import sys, json, collections
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow
from keccak import sel
rpc=RPC(min_interval=0.5)
MC='0xcA11bde05977b3631167028862bE2a173976CA11'
V1='0x6ba6f2207e343923ba692e5cae646fb0f566db8d'
S=sel('punkIndexToAddress(uint256)')[2:]
def enc_aggregate(calls):
    # aggregate((address,bytes)[]) 
    head='0x252dba42'+hex(32)[2:].rjust(64,'0')
    n=len(calls); body=hex(n)[2:].rjust(64,'0')
    elems=[]
    for t,data in calls:
        d=data[2:] if data.startswith('0x') else data
        e=t[2:].rjust(64,'0')+hex(64)[2:].rjust(64,'0')+hex(len(d)//2)[2:].rjust(64,'0')+d+('0'*((64-len(d)%64)%64))
        elems.append(e)
    offs=[]; cur=32*n
    for e in elems: offs.append(hex(cur)[2:].rjust(64,'0')); cur+=len(e)//2
    return head+body+''.join(offs)+''.join(elems)
def dec_aggregate(r):
    d=r[2:]; w=lambda i:int(d[i*64:(i+1)*64],16)
    # (uint256 blockNumber, bytes[] returnData)
    off=w(1)//32; n=w(off); out=[]
    for k in range(n):
        eo=off+1+w(off+1+k)//32; ln=w(eo); out.append(d[(eo+1)*64:(eo+1)*64+ln*2])
    return out
print('query_time_utc', utcnow())
bn=rpc.block_number(); print('block',bn)
owners={}
for start in range(0,10000,400):
    calls=[(V1,'0x'+S+hex(i)[2:].rjust(64,'0')) for i in range(start,min(10000,start+400))]
    r=rpc.call('eth_call',[{'to':MC,'data':enc_aggregate(calls)},hex(bn)])
    for i,x in zip(range(start,start+400),dec_aggregate(r)): owners[i]='0x'+x[-40:]
c=collections.Counter(owners.values())
print('distinct owner addresses on V1 contract',len(c))
for a,n in c.most_common(15): print(a,n)
json.dump(owners,open('os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'raw', 'onchain_culture', 'v1_owner_map.json')','w'))
