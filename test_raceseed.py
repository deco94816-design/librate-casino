import asyncio
from unittest.mock import AsyncMock, MagicMock
from race_admin import cmd_race_seed

async def main():
    update = MagicMock()
    # A dummy user ID that is definitively NOT an admin
    update.effective_user.id = 999999999
    update.message.reply_text = AsyncMock()
    
    context = MagicMock()
    context.args = []

    # Call the command, which immediately invokes _is_admin
    await cmd_race_seed(update, context)

    # _is_admin will hit the "Admin only" path because 999999999 is not an admin
    update.message.reply_text.assert_called_once()
    debug_msg = update.message.reply_text.call_args[0][0]
    print(f"EXACT_DEBUG_MSG: {debug_msg}")

if __name__ == "__main__":
    asyncio.run(main())
