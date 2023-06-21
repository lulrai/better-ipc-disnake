import asyncio
import disnake
from typing import Dict
from disnake.ext import commands
from disnake.ext.ipc.server import Server
from disnake.ext.ipc.objects import ClientPayload

class MyBot(commands.Bot):
    def __init__(self) -> None:
        intents = disnake.Intents.all()

        super().__init__(
            command_prefix="$.",
            intents=intents,
        )

        self.ipc = Server(self, secret_key="🐼")

    async def setup_hook(self) -> None:
        await self.ipc.start()

    @Server.route()
    async def get_user_data(self, data: ClientPayload) -> Dict:
        return user._to_minimal_user_json() # type: ignore

if __name__ == "__main__":
    bot = MyBot()
    asyncio.run(bot.start("TOKEN"))