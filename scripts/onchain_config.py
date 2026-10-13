"""On-chain collector analysis: shared configuration.

HEAD_BLOCK is fixed for reproducibility: eth_blockNumber returned 0x18f927e (26,186,366) on both the Tenderly public
gateway and the NodeReal public endpoint at ~2026-10-13T21:50Z (analysis date 2026-10-13). All "as of head" metrics
use the state after this block.
"""
import os
from common import ROOT, RAW, PROC

HEAD_BLOCK = 26_186_366
HEAD_TS = 1_791_928_163  # block timestamp of HEAD_BLOCK = 2026-10-13T21:49:23Z (eth_getBlockByNumber, Tenderly)
ANALYSIS_DATE = "2026-10-13"

TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
ZERO = "0x0000000000000000000000000000000000000000"
DEAD = {"0x0000000000000000000000000000000000000000", "0x000000000000000000000000000000000000dead",
        "0x0000000000000000000000000000000000000001"}

BLEND = "0x29469395eaf6f95920e59f858042f0e28d98a20b"
BLUR_POOL = "0x0000000000a39bb272e79075ade125fd351887ac"
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
SEAPORT = {"0x00000000000000adc04c56bf30ac9d3c0aaf14dc": "seaport1.5",
           "0x0000000000000068f116a894984e2db1123eb395": "seaport1.6",
           "0x00000000000001ad428e4906ae43d8f9852d0dd6": "seaport1.4",
           "0x00000000006c3852cbef3e08e8df289169ede581": "seaport1.1"}
BLUR_V2 = "0xb2ecfe4e4d61f8790bbb9de2d1259b9e2410cea5"
BLUR_V1 = "0x000000000000ad05ccc4f10045630fb830b95127"

# key: (contract, npf slug, display name, start block for log scan, token filter note)
COLLECTIONS = {
    "milady":           ("0x5af0d9827e0c53e4799bb226655a1de152a425a5", "milady", "Milady Maker"),
    "remilio":          ("0xd3d9ddd0cf0a5f0bfb8f7fceae075df687eaebab", "remilio-babies", "Redacted Remilio Babies"),
    "cryptodickbutts":  ("0x42069abfe407c60cf4ae4112bedead391dba1cdb", "cryptodickbutts", "CryptoDickbutts"),
    "pudgy":            ("0xbd3531da5cf5857e7cfaa92426877b022e612cf8", "pudgy-penguins", "Pudgy Penguins"),
    "azuki":            ("0xed5af388653567af2f388e6224dc7c4b3241c544", "azuki", "Azuki"),
    "terraforms":       ("0x4e1f41613c9084fdb9e34e11fae9412427480e56", "terraforms-by-mathcastles", "Terraforms"),
    "chromie_squiggle": ("0x059edd72cd353df5106d2b9cc5ab83a52287ac3a", "chromie-squiggle-art-blocks-curated",
                         "Chromie Squiggle (Art Blocks V1, project 0)"),
    "v1punks":          ("0x282bdd42f4eb70e7a9d9f40c8fea0825b7f68c5d", "v1-cryptopunks-wrapped",
                         "V1 CryptoPunks (official wrapper)"),
    "lil_pudgys":       ("0x524cab2ec69124574082676e6f654a18df49a048", "lil-pudgys", "Lil Pudgys"),
}
KEYS = list(COLLECTIONS)
SALES_PRIORITY = ["milady", "pudgy", "chromie_squiggle", "terraforms", "cryptodickbutts", "azuki", "v1punks",
                  "remilio", "lil_pudgys"]


def token_filter(key, token_id):
    """Chromie Squiggles share the Art Blocks V1 contract with projects 1-2: keep tokenId < 1,000,000 (project 0)."""
    if key == "chromie_squiggle":
        return token_id < 1_000_000
    return True


RAW_ON = os.path.join(RAW, "onchain")
PROC_ON = os.path.join(PROC, "onchain")
os.makedirs(RAW_ON, exist_ok=True)
os.makedirs(PROC_ON, exist_ok=True)
SCAN_START = 11_000_000  # 2020-10-06; precedes deployment of every contract above (Art Blocks V1 = Nov 2020)
