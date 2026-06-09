import asyncio, os
from dotenv import load_dotenv
load_dotenv()
from oxapay import OxaPay

async def main():
    ox = OxaPay(os.getenv('OXAPAY_KEY'))
    print(await ox.inquiry_deposit('128948409'))

if __name__ == "__main__":
    asyncio.run(main())
