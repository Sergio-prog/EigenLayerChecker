from pathlib import Path

ETHERFI_API = "https://claim.ether.fi/api/eigenlayer-allocations/{address}"
RENZO_API = "https://airdrop-data-ezeigen.s3.us-west-2.amazonaws.com/{address}/0x6910c6df496dcb1fb2e2983ca69bb6fe62a7ade8d6289d9ad91d493d05a40aea-{address}.json"
PUFFER_API = "https://api.hedgey.finance/token-claims/{address}"
KELP_API = "https://common.kelpdao.xyz/el-merkle/proofs/{address}"
SWELL_API = "https://v3-lrt.svc.swellnetwork.io/swell.v3.WalletService/EigenlayerAirdrop?connect=v1&encoding=json&message=%7B%22walletAddress%22%3A%22{address}%22%7D"
EL_API = "https://claims.eigenfoundation.org/clique-eigenlayer-api-v2/campaign/eigenlayer/credentials?walletAddress={address}"
MAGPIE_API = "https://api.magpiexyz.io/eigenpie/stakingPointsSeason?account={address}"
STAKESTONE_API = "https://claims.stakestone.io/clique-stakestone-api/airdrop/credentials?walletAddress={address}"

FAKE_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
FAKE_POSTMAN_USER_AGENT = "PostmanRuntime/7.42.0"

WRITE_TO_HTML = True
WRITE_TO_CSV = True
SAVE_FILE_NAME = "result"
ROOT_DIR = Path(__file__).parent
