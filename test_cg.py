import asyncio, aiohttp
from storage import db
async def test_cg():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text())
            
    # Check deposit
    print("Is 128948409 credited?", db.deposit_already_credited("128948409"))
    
if __name__ == "__main__":
    asyncio.run(test_cg())
