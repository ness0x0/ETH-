# Source registry

_Deduplicated registry of every external URL cited in the research files (`dossiers/_research/*.md`, `reports/*.md`),
grouped by source type. Each claim's context, publication date and access date (2026-10-13) are in the citing file.
Data APIs and on-chain endpoints are listed separately with what was fetched._

## A. Data sources (APIs, on-chain)

| Source | Endpoint | Used for | Raw archive |
|---|---|---|---|
| Binance public market data | `https://data-api.binance.vision/api/v3/klines` (ETHBTC, BTCUSDT, ETHUSDT, 1d) | Price history 2017→2026-10-13 | `data/raw/binance/` |
| OpenSea API v2 (keyless) | `/api/v2/collections/{slug}` and `/stats` | Live floors, owners, 1/7/30-day sales, contracts | `data/raw/opensea/` |
| OpenSea API v2 (free key via `POST /api/v2/auth/keys`, stored outside repo) | `/listings/collection/{slug}/best`, `/offers/collection/{slug}` | Order-book depth snapshot 2026-10-13 22:29–22:33 UTC | `data/raw/opensea_book/` |
| NFTPriceFloor | `https://api-bff.nftpricefloor.com/projects` and `/projects/{slug}/charts/all` | Universe stats; 3-day floor/volume/sales history since ~May 2022 | `data/raw/nftpricefloor/` |
| CoinGecko (free) | `/api/v3/nfts/{id}` | ATH cross-check | `data/raw/coingecko/` |
| Ethereum archive RPC | Tenderly public gateway `https://gateway.tenderly.co/public/mainnet`; NodeReal public endpoint | Transfer logs, receipts, eth_call (holders, sales, escrow, contract state) to head block 26,186,366+ | `data/raw/onchain/` (git-ignored; regenerate with `scripts/onchain_*.py`) |
| Blockscout | `https://eth.blockscout.com/api/v2/...` | Holder counts, address labels, contract metadata | `data/raw/onchain*/` |

## B. Primary and official sources (filings, project/official sites, on-chain explorers, museums, auction houses)

- https://blog.remilia.org/
- https://blog.remilia.org/press-feature-the-spectator-us-the-topsy-turvy-world-of-remilia-2025/
- https://blog.remilia.org/remilianet-alpha-design-notes/
- https://cryptodickbutts.substack.com/p/issue-3-math
- https://cryptodickbutts.substack.com/p/somethingishappening
- https://cryptodickbutts.substack.com/p/welcome
- https://data.sec.gov/submissions/CIK0002059693.json
- https://dev.artblocks.io/marfa-weekend
- https://etherscan.io/tx/0x8b52f966d7ec360050ccea1c2c13c4f6b42f826da16c118e43a4ad4950261e91
- https://etherscan.io/tx/0x93b8b1c009d291f81f4bcbbb478d56e739193ee211e73d9726b64177db561882
- https://infiniteimages.toledomuseum.org/artwork/chromie-squiggle-7583
- https://infiniteimages.toledomuseum.org/collection/chromie-squiggle
- https://opensea.io/blog/articles/in-conversation-with-erick-calderon
- https://opensea.io/blog/articles/opensea-digest-november-6-2025
- https://opensea.io/collection/hypercastle-explorers
- https://sothebys.com/en/buy/auction/2023/grails-part-ii/chromie-squiggle-1780
- https://sothebys.com/en/buy/auction/2025/digital-art-day-auction/chromie-squiggle-9871
- https://squiggledao1.substack.com/p/the-squiggledao-times-001
- https://squiggledao1.substack.com/p/the-squiggledao-times-009
- https://v1punks.gitbook.io/cryptopunks-v1-wiki/notable-events-in-2022
- https://v1punks.gitbook.io/cryptopunks-v1-wiki/wrapping
- https://wiki.remilia.org/$CULT
- https://wiki.remilia.org/Milady_Maker
- https://wiki.remilia.org/Remilia_Corporation
- https://wiki.remilia.org/Remilio_Babies
- https://www.artblocks.io/articles/art-basel-hk-2026-recap
- https://www.artblocks.io/articles/art-blocks-500-complete-collection
- https://www.artblocks.io/articles/the-final-three-ab500-comes-full-circle
- https://www.artblocks.io/articles/true-onchain-art
- https://www.businesswire.com/news/home/20260211894271/en/Elena-Velez-Partners-with-Remilia-Corporation-to-Launch-Remilia-Atelier-Debuting-the-Universal-Work-Suit
- https://www.businesswire.com/news/home/20260313786403/en/Remilia-Corporation-Debuts-Luxury-Streetwear-Collection-HIKKI-PUNKS-EXIT-SOCIETY
- https://www.prnewswire.com/news-releases/remilia-corporation-debuts-milady-rave-tokyo-and-announces-momentous-new-nft-bonkler-301793389.html
- https://www.sec.gov/Archives/edgar/data/1872195/000110465925090870/tm2525633d1_ex99-1.htm
- https://www.sec.gov/Archives/edgar/data/1998560/000121390026099901/ea030552101ex99-1.htm
- https://www.sec.gov/rule-release/34-104070
- https://x.com/RogerDickerman/status/1866125456287683046
- https://x.com/cryptopunks/status/1486092138534387712
- https://x.com/mathcastles

## C. Reputable independent reporting

- https://beincrypto.com/abstract-shutdown-pudgy-penguins-nft-floor/
- https://blockworks.co/news/azuki-trading-card-game-packs-nft
- https://cointelegraph.com/news/auction-christies-shuts-digital-art-nft-division
- https://cointelegraph.com/news/digital-archeology-long-dormant-mooncats-project-rides-nft-mania-to-the-moon
- https://cointelegraph.com/news/milady-nft-floor-price-surges-after-elon-musk-tweet
- https://cointelegraph.com/news/pudgy-penguins-expands-retail-footprint-with-target-trading-card-rollout
- https://cointelegraph.com/news/pudgy-penguins-winds-down-pudgy-party-mobile-game
- https://cointelegraph.com/news/robinhood-lists-pengu-popcat-memecoins-crypto-ramp-up
- https://cointelegraph.com/news/yuga-labs-sells-moonbirds-ip-orange-cap-games
- https://decrypt.co/100692/v1-cryptopunks-rarible-marketplace-larva-labs-dispute
- https://decrypt.co/106914/why-cryptodickbutts-ethereum-nft-surging-in-volume
- https://decrypt.co/107740/no-current-plans-for-v1-cryptopunks-nfts-yuga-labs
- https://decrypt.co/121238/lacma-art-museum-nft-donation-cryptopunk-art-blocks
- https://decrypt.co/124848/art-blocks-nft-marketplace-enforced-creator-royalties
- https://decrypt.co/137094/quite-surprise-seeing-cryptopunks-nft-pompidou-larva-labs-co-founder
- https://decrypt.co/139593/elon-musk-tweets-miladys-nft-meme-price-predictably-pumps
- https://decrypt.co/146426/azuki-elementals-nft-drop-yields-38-million-in-just-15-minutes
- https://decrypt.co/149362/moonbirds-mythics-nfts-begin-reveal-last-least-200-days
- https://decrypt.co/214715/art-blocks-acquires-nft-marketplace-sansa
- https://decrypt.co/241125/pudgy-penguins-igloo-raises-11-million-ethereum-layer-2
- https://decrypt.co/293720/art-blocks-nft-project-major-leap-ethereum
- https://decrypt.co/295800/milady-cult-coin-finally-launched-why-did-it-take-so-long-and-whats-next
- https://decrypt.co/296507/pengu-pudgy-penguins-solana-token-airdrop-tokenomics
- https://decrypt.co/300647/azuki-linked-anime-token-ethereum
- https://decrypt.co/301080/anime-azuki-ethereum-token-airdrop-tokenomics
- https://decrypt.co/309506/what-is-milady-edgy-ethereum-nft-community
- https://decrypt.co/323189/bored-ape-maker-sells-moonbirds-gaming-startup
- https://decrypt.co/330150/pudgy-penguins-pengu-token-doubles-in-a-week-amid-etf-hype
- https://decrypt.co/337273/pudgy-penguins-game-pudgy-party-launches-on-ios-and-android
- https://decrypt.co/340424/remilia-launching-milady-social-media-network-serve-4chan-diaspora
- https://decrypt.co/342727/moonbirds-token-birb-take-flight-solana-nft-comeback-continues
- https://decrypt.co/349746/why-billionaire-collector-continues-buy-nfts-2025
- https://decrypt.co/361574/pudgy-penguins-launched-a-new-game-crypto-scammers-made-a-fake-version
- https://decrypt.co/61316/an-ancient-nft-project-called-mooncats-is-eating-up-ethereum
- https://decrypt.co/62231/bots-are-ruining-mooncats-one-of-ethereums-oldest-nft-projects
- https://decrypt.co/92155/cryptopunks-controversy-creators-apologize-v1-ethereum-nft
- https://decrypt.co/92792/the-story-behind-the-cryptodickbutts-ethereum-nfts-resurgence
- https://decrypt.co/99869/twitter-declares-death-azuki-nft-collection-following-price-drop
- https://nftnow.com/features/incredible-staying-power-of-cryptodickbutts-nfts/
- https://nftnow.com/guides/the-ultimate-guide-to-azuki-nfts-everything-you-need-to-know/
- https://nftnow.com/news/cryptodickbutts-reveals-series4-ownership-transfer/
- https://nftnow.com/news/yuga-labs-acquires-proof/
- https://nftnow.com/newsletter/cryptopunks-ip-20-million-yuga-labs-node-foundation/
- https://protos.com/pudgy-penguins-parent-firm-shuts-down-its-own-blockchain/
- https://thedefiant.io/news/nfts-and-web3/azuki-linked-animecoin-airdrop-goes-live
- https://thedefiant.io/news/nfts-and-web3/milady-nfts-soar-amid-nft-market-volatility
- https://thedefiant.io/news/nfts-and-web3/moonbirds-cc0-license-nfts
- https://thedefiant.io/news/nfts-and-web3/moonbirds-debuts-birb-token-tge
- https://unchainedcrypto.com/ethereum-founder-vitalik-buterins-nft-choice-spurs-talk-of-wartime-mode/
- https://www.bankless.com/read/art-blocks-evolves
- https://www.bankless.com/read/v1-cryptopunks-renaissance
- https://www.bankless.com/read/v1-cryptopunks-trade-original-again
- https://www.bankless.com/terraforms-explained-is-this-ethereums-best-onchain-art
- https://www.coindesk.com/learn/what-are-mooncats-the-legacy-nft-project-revived-by-its-community/
- https://www.coindesk.com/markets/2025/07/25/crypto-whale-spends-usd4-3m-on-cryptopunks-as-nft-market-cap-climbs-66-in-30-days
- https://www.coindesk.com/markets/2025/10/10/usd16b-in-longs-liquidated-as-wall-street-sell-off-extends-btc-eth-broader-crypto-market-meltdown
- https://www.coindesk.com/markets/2026/04/27/pudgy-penguins-rally-coincides-with-token-unlock-as-analyst-flags-exit-liquidity-risk
- https://www.coindesk.com/research/pudgy-penguins-a-new-blueprint-for-tokenized-culture
- https://www.coindesk.com/tech/2023/12/10/pudgy-penguins-to-launch-webkinz-like-virtual-world-in-2024
- https://www.coindesk.com/tech/2025/12/12/nft-project-pudgy-penguins-takes-over-las-vegas-sphere-in-holiday-campaign
- https://www.coindesk.com/tech/2026/03/10/pudgy-penguins-launches-its-club-penguin-moment-and-the-game-doesn-t-feel-like-crypto-at-all
- https://www.coindesk.com/tech/2026/10/07/pudgy-penguins-abstract-becomes-second-ethereum-layer-2-to-shut-in-a-week
- https://www.coindesk.com/tech/2026/10/13/once-largest-ethereum-nft-marketplace-blur-is-shutting-down-after-volumes-collapse-99
- https://www.rightclicksave.com/article/art-blocks-embraces-ai-agents-jordan-lyall-interview
- https://www.rightclicksave.com/article/digital-art-acquisitions-in-2025-moma-whitney-centre-pompidou
- https://www.rightclicksave.com/article/larva-labs-to-release-final-art-blocks-curated-project-quine-news
- https://www.theblock.co/amp/post/395541/miladys-loyalty-pledge-unnecessary-culture-schism-ethereum-community
- https://www.theblock.co/news/deals/2024-07-23-peter-thiel-founders-fund-pudgy-penguins-igloo-funding-abstract-306955
- https://www.theblock.co/news/ecosystems/2026-10-06-abstract-ethereum-layer-2-shutting-down-pudgy-penguins-igloo-417855
- https://www.theblock.co/news/ecosystems/2026-10-12-blur-nft-marketplace-shutting-down-frontend-blend-418363
- https://www.theblock.co/news/markets/2024-12-09-cult-memecoin-from-milady-nft-creators-goes-live-at-over-600-million-fdv-329935
- https://www.theblock.co/news/web3/2022-07-19-the-metaverse-that-crashed-into-reality-the-story-of-miya-and-milady-maker-157907
- https://www.theblock.co/post/161819/moonbirds-ruffles-some-holders-feathers-with-abrupt-copyright-switch
- https://www.theblock.co/post/171617/chiru-labs-azuki-creator-30-million-series-a-fundraise
- https://www.theblock.co/post/172991/art-blocks-nft-platform-winds-down-curated-series-plans-branding-refresh
- https://www.theblock.co/post/179636/art-blocks-founder-announces-friendship-bracelet-nft-airdrop
- https://www.theblock.co/post/225954/cryptopunks-210-million-hot-streak-fueled-by-added-liquidity-and-blur-incentives
- https://www.theblock.co/post/230279/elon-musk-milady-price-twitter-meme
- https://www.theblock.co/post/230466/counterculture-nft-collection-milady-maker-surged-in-volume-after-elon-musk-tweet
- https://www.theblock.co/post/236681/azuki-nft-collections-ends-elemental-mint-with-37-5-million-before-it-was-ever-open-to-the-public
- https://www.theblock.co/post/237484/azuki-floor-price-crumbles-with-holders-down-21500-per-nft
- https://www.theblock.co/post/252987/walmart-pudgy-penguins-nft-toys
- https://www.theblock.co/post/277905/bored-apes-creator-yuga-labs-acquires-proof-takes-over-moonbirds-nft-brand
- https://www.theblock.co/post/278347/walmart-pudgy-penguins-expansion
- https://www.theblock.co/post/282972/remilia-founder-charlotte-fang-claims-he-was-hacked-as-treasury-is-drained-of-millions
- https://www.theblock.co/post/329935/cult-memecoin-from-milady-nft-creators-goes-live-at-over-600-million-fdv
- https://www.theblock.co/post/334203/arbitrum-azuki-backed-animecoin-unveils-tokenomics
- https://www.theblock.co/post/354114/yuga-labs-sells-cryptopunks-ip-to-nonprofit-infinite-node-foundation
- https://www.theblock.co/post/383446/moma-adds-cryptopunks-and-chromie-squiggles-nfts-to-permanent-collection-following-coordinated-donation

## D. Secondary, aggregator or low-reliability sources (used only as last resort; flagged where cited)

- https://0xcow.substack.com/p/saved-milady-and-how-we-planned-to
- https://4pillars.io/en/issues/pudgy-penguins-will-inherit-disneys-crown
- https://aijourn.com/former-overwatch-character-art-director-arnold-tsang-unveils-azuki-a-new-original-manga-series/
- https://amycastor.com/2022/06/04/the-early-history-of-nfts-curio-cards/
- https://bigbendsentinel.com/2025/10/16/5th-annual-art-blocks-weekend-to-bring-hundreds-of-visitors/
- https://blockworks.com/news/azuki-missed-the-mark-on-elementals
- https://cardgamer.com/games/tcgs/gates-awakened-first-set-for-tcg-azuki-heads-to-retail/
- https://ccsupply.xyz/
- https://changelly.com/blog/milady-crypto/
- https://coindesk.com/business/2022/08/11/pudgy-penguins-announce-physical-toys-sending-nft-prices-surging/
- https://coingecko.com/learn/what-are-pudgy-penguins-nfts
- https://coinmarketcap.com/currencies/dickbutt/
- https://corporatetrash.beehiiv.com/p/five-things-know-chromie-squiggles
- https://crypto.news/pudgy-penguins-gets-support-as-billionaire-buys-117-nfts/
- https://cryptobriefing.com/moonbirds-birb-token-launch/
- https://cryptobriefing.com/pengu-token-jumps-62-percent-ipo-speculation/
- https://cryptonews.com/news/blur-nft-volume-collapse-shut-down/
- https://cryptopotato.com/co-founders-of-remilia-file-lawsuit-in-new-milady-vs-milady-case-against-charlotte-fang/
- https://cryptopunks.networked.art/
- https://cryptoticker.io/en/nft-prices-october-2026-bored-ape-cryptopunks-floor
- https://curio.cards/
- https://dappradar.com/blog/azuki-nfts
- https://dickbutt.site/
- https://docs.curio.cards/
- https://en.wikipedia.org/wiki/Curio_Cards
- https://en.wikipedia.org/wiki/Pudgy_Penguins
- https://finance.yahoo.com/news/moonbirds-nfts-soaring-again-whats-160103496.html
- https://forbesjapan.com/articles/detail/45891
- https://forkast.news/pudgy-penguins-licensing-nft-revenue-airdrops/
- https://fortune.com/2022/04/18/moonbird-nft-collection-surge/
- https://games.gg/news/orange-cap-games-raises-millions/
- https://github.com/cryptopunksnotdead/awesome-cryptopunks-bubble/blob/master/PUNKS_V1_NOTES.md
- https://gooch.finance/
- https://grailcap.substack.com/p/digital-art-market-on-blockchains-2e3
- https://icv2.com/articles/news/view/63522/azuki-labs-announces-second-azuki-tcg-set
- https://ilikecalculus.substack.com/p/an-ode-to-terraforms
- https://info.arkm.com/research/gcr-wakes-up-to-claim-cult-airdrop-53iul
- https://insidebitcoins.com/news/moonbirds-unveils-birb-tokenomics-allocates-just-25-to-nfts
- https://insidebitcoins.com/news/nft-firm-azuki-unveils-its-2026-roadmap-including-a-manga
- https://iq.wiki/wiki/cryptodickbutts
- https://iq.wiki/wiki/milady-maker/events
- https://iq.wiki/wiki/terraforms
- https://koinly.io/blog/milady-meme-coin/
- https://kucoin.com/announcement/en-milady-cult-coin-miladycult-gets-listed-on-kucoin
- https://medium.com/@first.vip/first-vip-project-analysis-terraforms-by-mathcastles-c401dd15a1a6
- https://metaversal.banklesshq.com/p/art-blocks-20
- https://mintorskip.beehiiv.com/p/im-smooth-brain
- https://mintorskip.beehiiv.com/p/will-never-buy
- https://news.bitcoin.com/nft-based-firm-remilia-corporation-sues-independent-contractors-accused-of-siphoning-1-million/
- https://nftduck.com/collection/cryptodickbutts-s3
- https://nftevening.com/snowfro-speaks-the-art-blocks-founder-on-his-journey-as-a-web3-artist/
- https://niftynoon.substack.com/p/niftynoon-azukis-anime-coin-is-finally
- https://nodefoundation.com/cryptopunks
- https://nowmedia.co/posts/art-blocks-500-snowfro-generative-art-interview
- https://phemex.com/news/article/pudgy-penguins-targets-50-million-revenue-eyes-ipo-by-2027-16063
- https://seanbonner.com/2022/02/13/explaining-cryptopunks-versions/
- https://thedigitalarttimes.substack.com/p/cryptopunks-after-the-20-million
- https://thousandant.itch.io/hypercastle-explorer
- https://threadreaderapp.com/thread/1439332605263032327.html
- https://toledomuseum.org/about/leadership/snowfro
- https://unframed.lacma.org/node/3729
- https://venusovermanhattan.com/news/ocula
- https://verse.works/series/terraforms-by-mathcastles
- https://whale-alert.io/stories/ea98012535090c/OpenSea-delays-SEA-token-launch-indefinitely-last-Treasure-rewards-wave-refunds-offered-forfeiting-Treasure-and-0-OS2-trading-fees-for-60-days
- https://www.anitrendz.com/news/2024/04/11/enter-the-garden-anime-anthology-series-launches-1st-part-the-waiting-man-on-april-30
- https://www.anitrendz.com/news/2025/07/02/web3-company-azuki-sets-up-us-anime-studio-with-comisma-and-xenotoon
- https://www.axios.com/2023/05/09/pudgy-penguins-nft-ip-brand
- https://www.bitget.com/news/detail/12560603924492
- https://www.bitget.com/news/detail/12560605079403
- https://www.bitrue.com/blog/what-is-cryptodickbutts-nft
- https://www.blockchaingamer.biz/news/40300/faraway-sells-hv-mtl-adam-weitsman/
- https://www.blockchaingamer.biz/news/43020/abstract-shutting-down/
- https://www.blockhead.co/2022/08/08/meme-culture-strengthens-as-cryptodickbutts-nft-volume-surges-935/
- https://www.blockmedia.co.kr/archives/707573
- https://www.cartoonbrew.com/anime/will-smith-jada-pinkett-smith-westbrook-inc-studio-azuki-248220.html
- https://www.centrepompidou.fr/en/ressources/oeuvre/WX3xkvI
- https://www.coinbase.com/price/moonbirds
- https://www.coingecko.com/en/coins/moonbirds
- https://www.coingecko.com/learn/october-10-crypto-crash-explained
- https://www.courtlistener.com/docket/72364956/pei-licensing-llc-v-pudgy-penguins-inc/
- https://www.cryptopolitan.com/milady-cult-token-500m-market-cap-whitepaper/
- https://www.cryptotimes.io/2023/07/18/milady-maker-wins-nft-project-of-the-year-at-binance-awards/
- https://www.cryptotimes.io/2026/01/02/milady-nft-floor-price-rises-50-after-vitaliks-profile-update/
- https://www.datawallet.com/crypto/what-is-milady-nft
- https://www.dentsu.com/news-releases/dentsu-partners-with-azuki-to-create-three-part-anime-series
- https://www.dwf-labs.com/news/427-dwf-labs-invests-5m-in-milady-memecoin
- https://www.gate.com/learn/articles/first-class-research-report-terraforms-by-mathcastles/1820
- https://www.gfinityesports.com/article/moonbirds-nft-mint-price-where-to-buy
- https://www.glitchmarfa.com/e30dgallery/terraforms/
- https://www.globenewswire.com/news-release/2025/08/28/3140968/0/en/Lady-Rocket-Foundation-and-Unstoppable-Domains-Announce-Launch-of-MOONCAT-to-Support-Cat-Rescue-and-Onchain-Identity.html
- https://www.kucoin.com/news/flash/moonbirds-announces-birb-token-tge-on-january-28
- https://www.lerandom.art/artists/mathcastles
- https://www.newartdealers.org/fairs/nada-miami-2022/artworks/8141
- https://www.retailitinsights.com/doc/pudgy-penguins-expands-pudgy-toys-to-second-major-nationwide-retailer-0001
- https://www.terraformsantenna.info/
- https://www.theboredapegazette.com/post/are-punks-the-next-punks-jalil-eth-found-a-fix-for-the-original-cryptopunks-v1-contract-sparking
- https://www.theboredapegazette.com/post/v2-punks-are-not-alone-a-v1-alien-cryptopunk-sells-for-180-eth-or-312k-months-after-jalil-patched
- https://www.zagabond.com/

## E. API/RPC URLs referenced in text

- `https://api.pudgypenguins.io/lil/1`
- `https://apis.io/providers/reservoir/`
- `https://decrypt.co/96786/pudgy-penguins-ethereum-nft-collection-sold-to-netz-capital-for-2-5-million`
- `https://gateway.tenderly.co/public/mainnet`
- `https://www.federalregister.gov/api/v1/documents.json?conditions[term]=%22PENGU%22`
- `https://www.theblock.co/post/336746/azukis-anime-token-surpasses-350-million-market-capitalization-one-day-after-launch`
- `https://www.theblock.co/research/institutional/rapid-insights-the-pudgy-penguin-airdrop-331611`
