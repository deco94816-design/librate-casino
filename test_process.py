import asyncio
from auto_deposit import get_ton_price_usd, process_deposit
from storage import db

class MockBot:
    async def send_message(self, chat_id, text, parse_mode):
        print(f"Sent message to {chat_id}: {text}")

async def test():
    print("Testing process_deposit")
    try:
        await process_deposit(MockBot(), "128948409", "paid", 0.10)
        print("Success")
    except Exception as e:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())
