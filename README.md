# Better IPC Disnake

Forked from Better IPC: https://github.com/MiroslavRosenov/better-ipc

Support discord for original repository: <a href="https://discord.gg/Rpg7zjFYsh" target="_blank"><img src="https://img.shields.io/discord/875005644594372638?label=discord"></a>

## High-performance inter-process communication library designed to work with the latest version of disnake.

<img src="https://raw.githubusercontent.com/MiroslavRosenov/better-ipc/main/banner.png">

This library is *based* on [discord-ext-ipc](https://github.com/Ext-Creators/discord-ext-ipc), which is no longer maintained.

> ### Development version
#### For Linux
```shell
python3 -m pip install -U git+https://github.com/lulrai/better-ipc-disnake
```
#### For Windows
```shell
py -m pip install -U git+https://github.com/lulrai/better-ipc-disnake
```

# Examples

### Client example
```python
import disnake
from typing import Dict
from disnake.ext import commands, ipc
from disnake.ext.ipc.server import Server
from disnake.ext.ipc.objects import ClientPayload

class MyBot(commands.Bot):
    def __init__(self) -> None:
        intents = disnake.Intents.all()

        super().__init__(
            command_prefix="$.",
            intents=intents,
        )

        self.ipc = ipc.Server(self, secret_key="🐼")

    async def setup_hook(self) -> None:
        await self.ipc.start()

    @Server.route()
    async def get_user_data(self, data: ClientPayload) -> Dict:
        user = self.get_user(data.user_id)
        return user._to_minimal_user_json()
```


### Cog example
```python
from typing import Dict
from disnake.ext import commands, ipc
from disnake.ext.ipc.server import Server
from disnake.ext.ipc.errors import IPCError
from disnake.ext.ipc.objects import ClientPayload

class Routes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        if not hasattr(bot, "ipc"):
            bot.ipc = ipc.Server(self.bot, secret_key="🐼")
    
    async def cog_load(self) -> None:
        await self.bot.ipc.start()

    async def cog_unload(self) -> None:
        await self.bot.ipc.stop()
        self.bot.ipc = None

    @Server.route()
    async def get_user_data(self, data: ClientPayload) -> Dict:
        user = self.bot.get_user(data.user_id)
        return user._to_minimal_user_json()

async def setup(bot):
    await bot.add_cog(Routes(bot))
```


### Inside your web application
```python
from quart import Quart
from disnake.ext.ipc import Client

app = Quart(__name__)
ipc = Client(secret_key="🐼")

@app.route('/')
async def main():
    resp = await ipc.request("get_user_data", user_id=383946213629624322)
    return str(resp.response)

if __name__ == '__main__':
    app.run()
```
