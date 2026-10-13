import sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow
from keccak import sel, keccak256
rpc=RPC(min_interval=0.4)
A='0xa858ddc0445d8131dac4d1de01f834ffcba52ef1'
V2='0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb'; V1='0x6ba6f2207e343923ba692e5cae646fb0f566db8d'
print('query_time_utc', utcnow())
for name,c in [('V2 punks',V2),('V1 punks',V1),('BAYC','0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'),('WPV1 wrapper','0x282bdd42f4eb70e7a9d9f40c8fea0825b7f68c5d')]:
    r=rpc.call('eth_call',[{'to':c,'data':sel('balanceOf(address)')+A[2:].rjust(64,'0')},'latest']); print(name,'balance of',A,int(r,16))
# V1 PunkTransfer events from A since 2022-03-01 (block 14,300,000)
PT='0x'+keccak256(b'PunkTransfer(address,address,uint256)').hex()
T='0x'+keccak256(b'Transfer(address,address,uint256)').hex()
topicA='0x'+A[2:].rjust(64,'0')
for nm,topic in [('PunkTransfer',PT),('Transfer',T)]:
    out=rpc.get_logs(V1,[topic,topicA],14_300_000,26_186_000,step=3_000_000)
    inn=rpc.get_logs(V1,[topic,None,topicA],14_300_000,26_186_000,step=3_000_000)
    print(nm,'out from A',len(out),'in to A',len(inn))
    for l in (inn+out)[:6]: print(' ',int(l['blockNumber'],16),l['topics'][1][-40:],'->',l['topics'][2][-40:])
