import sys, datetime as dt
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow, TRANSFER_TOPIC
from keccak import sel
rpc=RPC(min_interval=0.35)
AB='0x059edd72cd353df5106d2b9cc5ab83a52287ac3a'
print('query_time_utc', utcnow())
ids=[1458,4697,8929,2685,2394,1698,2557,8064,7583]
own={}
for t in ids:
    r=rpc.call('eth_call',[{'to':AB,'data':sel('ownerOf(uint256)')+hex(t)[2:].rjust(64,'0')},'latest']); own[t]='0x'+r[-40:]
print(own)
def ts(b):
    x=rpc.call('eth_getBlockByNumber',[hex(b),False]); return dt.datetime.fromtimestamp(int(x['timestamp'],16),dt.timezone.utc).date()
for t in [4697,7583,1458]:
    L=rpc.call('eth_getLogs',[{'address':AB,'fromBlock':hex(11_300_000),'toBlock':'latest','topics':[TRANSFER_TOPIC,None,None,'0x'+hex(t)[2:].rjust(64,'0')]}])
    last=L[-1]; b=int(last['blockNumber'],16)
    print('token',t,'transfers',len(L),'last transfer',ts(b),'from',last['topics'][1][-40:],'to',last['topics'][2][-40:],'tx',last['transactionHash'])
