import discord,asyncio
from enum import Enum
from discord import app_commands, Interaction, ui, SelectOption, Embed
from mbti import *

class ArgumentMbti(Enum):
    ISTJ="ISTJ"
    ISFJ="ISFJ"
    INFJ="INFJ"
    INTJ="INTJ"
    ISTP="ISTP"
    ISFP="ISFP"
    INFP="INFP"
    INTP="INTP"
    ESTP="ESTP"
    ESFP="ESFP"
    ENFP="ENFP"
    ENTP="ENTP"
    ESTJ="ESTJ"
    ESFJ="ESFJ"
    ENFJ="ENFJ"
    ENTJ="ENTJ"

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.futures = {}

    async def on_ready(self):
        await self.wait_until_ready()
        await tree.sync()
        print(f"{self.user} 에 로그인하였습니다!")

    async def on_interaction(self, interaction: Interaction):
        if interaction.user.id in self.futures:
            self.futures[interaction.user.id].set_result(interaction)
            del self.futures[interaction.user.id]
            await interaction.response.defer()  # 상호작용에 대한 응답 추가

intents = discord.Intents.default()
client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="검사", description="MBTI 검사를 시작합니다.")
async def start_test(interaction: Interaction):
    thread = await interaction.channel.create_thread(name=f"{interaction.user.display_name}님의 MBTI 검사", type=discord.ChannelType.private_thread)
    await thread.add_user(interaction.user)
    await interaction.response.send_message("MBTI 검사를 시작합니다. 스레드에서 진행됩니다.", ephemeral=True)
    async def run_test(thread, interaction, respond):
        for i in range(61):
            try:
                async for message in thread.history(limit=100):
                    if message.author == client.user:
                        await message.delete()
            except:
                pass
            if i < 60:
                question = get_test(i)
                select = ui.Select(placeholder="선택하세요", min_values=1, max_values=1)
                select.add_option(label="매우 그렇다",description="당신의 행동이나 태도에 매우 부합합니다.",emoji="🟥", value="-3")
                select.add_option(label="대체로 그렇다",description="당신이 해당 특징을 대부분 나타냅니다.", emoji="🟧", value="-2")
                select.add_option(label="약간 그렇다",description="당신이 해당 특징의 일부 가지고 있습니다.",emoji="🟨", value="-1")
                select.add_option(label="잘 모르겠다",description="당신이 해당 특징에 대해 확신을 갖고 있지 않습니다.",emoji="⬛", value="0")
                select.add_option(label="약간 그렇지 않다",description="당신이 해당 특징의 매우 일부분만을 나타냅니다.",emoji="🟩", value="1")
                select.add_option(label="대체로 그렇지 않다",description="당신이 해당 특징을 대부분 나타내지 않습니다.",emoji="🟦", value="2")
                select.add_option(label="매우 그렇지 않다",description="당신의 행동이나 태도에 매우 부합하지 않습니다.",emoji="🟪", value="3")
                view=ui.View()
                view.add_item(select)
                embed = discord.Embed(title=f"{i+1}번째 질문",description=question,color=discord.Color.blurple())
                await thread.send(embed=embed,view=view)

                future = client.loop.create_future()
                client.futures[interaction.user.id] = future
                interaction = await future
                respond.append(int(interaction.data['values'][0]))
            else:
                mbti_result = get_result(*respond)
                embed = Embed(title=f"당신의 유형은 {mbti_result['nickname']}({mbti_result['mbti']})입니다.", description=f"{mbti_result['description']}\n\n[[자세한 정보]]({mbti_result['url']})는 해당 URL확인해주세요.").set_image(url=mbti_result['avatar'],color=discord.Color.blurple())
                await thread.send(embed=embed)
                break
    respond = []
    try:
        await asyncio.wait_for(run_test(thread, interaction, respond), timeout=3600)
    except asyncio.TimeoutError:
        await thread.delete()
        embed = discord.Embed(title="시간 초과 🕘",description="시간 초과로 인해 쓰레드를 삭제하였습니다.",color=discord.Color.red())
        await interaction.user.send(embed=embed)

@tree.command(name="궁합", description="MBTI 유형간의 궁합을 확인합니다.")
async def mkembed(interaction:Interaction,유형1:ArgumentMbti,유형2:ArgumentMbti):
    embed = discord.Embed(title=f"{유형1.value}와 {유형2.value}의 궁합",description=get_relationship(유형1.value,유형2.value),color=discord.Color.blurple()) #name:오른쪽, value:왼쪽 빨간색을 골랐다면 name은 빨강 value는 discord.Color.red()
    await interaction.response.send_message(embed=embed)

@tree.command(name="정보", description="MBTI 유형의 정보를 불러옵니다.")
async def mkembed(interaction:Interaction,유형:ArgumentMbti):
    mbti_result = get_info(유형.value)
    embed = Embed(title=f"{mbti_result['nickname']}({mbti_result['mbti']})의 정보.", description=f"{mbti_result['description']}",color=discord.Color.blurple()).set_image(url=mbti_result['avatar'])
    await interaction.response.send_message(embed=embed)

client.run("Insert your token")