import asyncio 
import discord
import random

client = discord.Client()

token = "NzMyMjIyMzI0NjM1MzM2NzE0.XwxdLg.y7pO7V2T9Vtg786FNyUxE0AK8uk"

@client.event
async def on_ready():

    print("=========================")
    print("다음으로 로그인 합니다 : komabot")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("코마야 도움")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "코마봇 입력 테스트":
        await message.channel.send("출력")
    if message.content == "코마야 도움":
        embed = discord.Embed(title="코마봇 도움말", description="이것은 도움말입니다", color=0x00ff00)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/697279994707181588/733099712764444822/unknown.png")
        embed.add_field(name="코마야 도움 링크", value="링크를 보여준다", inline=True) 
        embed.add_field(name="코마야 도움 게임", value="내장게임이 있다", inline=True) 
        embed.add_field(name="코마야 도움 전적", value="전적을 보여준다", inline=True) 
        await message.channel.send(embed=embed)
    if message.content == "코마야 도움 링크":
        embed = discord.Embed(title="코마봇 도움말 링크", description="이것은 링크입네다", color=0x00ff00)
        embed.add_field(name="1", value="[코마 유튜브](https://www.youtube.com/channel/UCIigIgtZ65TiGQSmnVJaUCQ)", inline=False)
        embed.add_field(name="2", value="[코마 트위치](https://www.twitch.tv/twitchkoma)", inline=False)
        embed.add_field(name="3", value="[코마 트윕](https://twip.kr/twitchkoma)", inline=False)
        embed.add_field(name="4", value="[코마 투네이션](https://toon.at/donate/637149279939478102)", inline=False)
        embed.set_footer(text="이정도면 도와줬지?")
        await message.channel.send(embed=embed)
    if message.content == "코마야 도움 게임":
        await message.channel.send("구란뎅 \n그걸 믿네")
    if message.content == "코마야 sake L" or message.content == "코마야 신":
        bot_response = random.randint(1,9)
        if bot_response == 1:
            await message.channel.send("sakeL은 불을 안 꺼도 램을 볼 수 있다")
        if bot_response == 2:
            await message.channel.send("sake L은 동원참치의 레시피를 1개로 줄일 수 있다")
        if bot_response == 3:
            await message.channel.send("sake L은 땅바닥에 떨어진 음식을 10초 뒤에 먹을수 있다")
        if bot_response == 4:
            await message.channel.send("귀신은 매일 잠자리에 들기전 침대 밑에 sake L이 있는지 확인한다")
        if bot_response == 5:
            await message.channel.send("sake L은 정신한테 물려가도 호랑이를 차릴수 있다")
        if bot_response == 6:
            await message.channel.send("sake L은 주호민이 머리에 빗질하는 모습을 보았다")
        if bot_response == 7:
            await message.channel.send("sake L은 진용진을 클릭해주셔서 미안하게만들수있다")
        if bot_response == 8:
            await message.channel.send("sake L은 로봇이 아닙니다를 한번에 할 수 있다")
        if bot_response == 9:
            await message.channel.send("sake L은 오목을 바둑돌 1개로 이길수 있다")
    
client.run(token)
