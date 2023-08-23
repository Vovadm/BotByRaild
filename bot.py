import disnake
from disnake.ext import commands
import random


bot = commands.Bot(command_prefix=".", intents= disnake.Intents.all(), help_command= None, test_guilds=[server id])

# /sex
@bot.slash_command()
async def sex(string, nick: disnake.Member):
    rn1 = random.randint(0, 3)
    if rn1 == 0:
        await string.send(f"Вы успешно занялись секcом с {nick}")
    elif rn1 == 1:
        await string.send(f"О ноу, вы заразили себя и {nick} спидом ((((")
    elif rn1 == 2:
        await string.send(f"О ноу, произошел пролив спермы, и теперь у {nick} появился ребенок")
    elif rn1 == 3:
        await string.send(f"Бро, ты же сигма. Тебя не должен интересовать {nick}")





# private voice
@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel.id == voice id:
        category = after.channel.category
        guild = member.guild
        channel = await guild.create_voice_channel(name=f'Private of {member.display_name}', category = category)
        await member.move_to(channel)
        def check(x, y, z):
            return len(channel.members) == 0
        await bot.wait_for('voice_state_update', check = check)
        await channel.delete()


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

bot.run("token")
