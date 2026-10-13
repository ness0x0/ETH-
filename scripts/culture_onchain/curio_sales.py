"""Recent Curio Card (wrapper 0x73da73ef...) sale prices per card, decoded from Seaport OrderFulfilled events."""
import sys, json, collections, datetime as dt
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, utcnow
from keccak import keccak256
rpc=RPC(min_interval=0.3)
W='0x73da73ef3a6982109c4d5bdb0db9dd3e3783f313'
TS='0x'+keccak256(b'TransferSingle(address,address,address,uint256,uint256)').hex()
TB='0x'+keccak256(b'TransferBatch(address,address,address,uint256[],uint256[])').hex()
OF='0x'+keccak256(b'OrderFulfilled(bytes32,address,address,address,(uint8,address,uint256,uint256)[],(uint8,address,uint256,uint256,address)[])').hex()
WETH='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
print('query_time_utc', utcnow())
latest=rpc.block_number(); start=latest-1_300_000  # ~180 days
print('blocks',start,latest)
lb=rpc.call('eth_getBlockByNumber',[hex(latest),False]); lt=int(lb['timestamp'],16)
sb=rpc.call('eth_getBlockByNumber',[hex(start),False]); st=int(sb['timestamp'],16)
def bdate(b): return dt.datetime.fromtimestamp(st+(b-start)*(lt-st)/(latest-start),dt.timezone.utc).date().isoformat()
L=rpc.get_logs(W,[TS],start,latest,step=500_000)
print('TransferSingle logs',len(L))
txs=collections.OrderedDict()
for l in L: txs.setdefault(l['transactionHash'],int(l['blockNumber'],16))
print('unique txs',len(txs))
def words(data):
    d=data[2:]; return [d[i:i+64] for i in range(0,len(d),64)]
sales=[]
for i,(h,b) in enumerate(txs.items()):
    try: r=rpc.call('eth_getTransactionReceipt',[h],retries=4)
    except Exception as e: continue
    for lg in r['logs']:
        if lg['topics'][0]!=OF: continue
        w=words(lg['data'])
        # data: orderHash, recipient, offerOffset, considerationOffset, ...
        offo=int(w[2],16)//32; cono=int(w[3],16)//32
        n=int(w[offo],16); offer=[]
        for k in range(n):
            base=offo+1+4*k; offer.append((int(w[base],16),'0x'+w[base+1][-40:],int(w[base+2],16),int(w[base+3],16)))
        m=int(w[cono],16); cons=[]
        for k in range(m):
            base=cono+1+5*k; cons.append((int(w[base],16),'0x'+w[base+1][-40:],int(w[base+2],16),int(w[base+3],16)))
        cur_off=[x for x in offer if x[1]==W]; cur_con=[x for x in cons if x[1]==W]
        if cur_off:  # seller listing: offer curio, consideration = payment
            pay=sum(x[3] for x in cons if x[0] in (0,1) and (x[0]==0 or x[1]==WETH))
            for x in cur_off: sales.append((bdate(b),x[2],x[3],pay/1e18/sum(y[3] for y in cur_off),h))
        elif cur_con: # bid accepted: offer = WETH
            pay=sum(x[3] for x in offer if x[0]==1 and x[1]==WETH)
            for x in cur_con: sales.append((bdate(b),x[2],x[3],pay/1e18/sum(y[3] for y in cur_con),h))
print('decoded sale lines',len(sales))
json.dump(sales,open('os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'raw', 'onchain_culture', 'curio_sales_180d_rawlist.json')','w'))
by=collections.defaultdict(list)
for d,tid,amt,unit,h in sales:
    if unit>0: by[tid].append((d,unit,amt))
for tid in sorted(by):
    v=sorted(by[tid]); last=v[-5:]
    print(f"token {tid}: n={len(v)} last={[(a,round(b,4),c) for a,b,c in last]}")
