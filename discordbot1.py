import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '>')
client.remove_command("help")

def simpleEmbed(s):
    embed = discord.Embed(
        color=discord.Colour.green(),
        description=s,
    )
    return embed


duck_gif = ['https://media.tenor.com/images/2d6c4778a4311a035152427163dc8443/tenor.gif',
            'https://media.tenor.com/images/33cbb479e4bceeef31e669d4698a8b93/tenor.gif',
            'https://media.tenor.com/images/18134e7c0ebc66cdc700a184cf1c9988/tenor.gif',
            'https://media.tenor.com/images/dab11270bc31f1b32b9e2abd67a360a0/tenor.gif',
            'https://media.tenor.com/images/a64c3d32f1b93bde5d7a63fb4fc3a976/tenor.gif',
            'https://media.tenor.com/images/34875eed9f61677cecc5fbe53b3318b4/tenor.gif',
            'https://media.tenor.com/images/de0431a10c7fde3bb1011855355d42e9/tenor.gif',
            'https://media.tenor.com/images/cb80fbf63ea961a50c1981d338df241d/tenor.gif',
            'https://media.tenor.com/images/ef725ec7349e13cd19a0614a3498b17e/tenor.gif',
            'https://media.tenor.com/images/e218e358dca7638e8ab2d99f12b7efec/tenor.gif',
            'https://media.tenor.com/images/3eef0a2f2e7539c98dac494e494181e9/tenor.gif',
            'https://media.tenor.com/images/a3fee76f2ffe4c0932e24bbe1a502675/tenor.gif']


anime_sad=["https://media.tenor.com/images/7e623e17dd8c776aee5e0c3e0e9534c9/tenor.gif",
           "https://media.tenor.com/images/eda88aaad47aaab5d861c19a03d73e27/tenor.gif",
           "https://media.tenor.com/images/b261321eff758fb664ea6ff110fec20a/tenor.gif",
           "https://media.tenor.com/images/f8aa8ffe34d6211894d1a8edc229401e/tenor.gif",
           "https://media.tenor.com/images/d0d3978f45b380bfd2abbaf21543125f/tenor.gif",
           "https://media.tenor.com/images/535d5fef2e2db033b143a4e0b7a9f5a5/tenor.gif",
           "https://media.tenor.com/images/6f1b243c5d1dca606a2e79d00c62cfce/tenor.gif"]


anime_slap=["https://media.tenor.com/images/c519bdd8fd4dd9163150ab1237226c2b/tenor.gif",
            "https://media.tenor.com/images/ad7d5ee89e99fc54fef26282c87c7c2c/tenor.gif",
            "https://media.tenor.com/images/783aabd96e94319bd963958a59efbd4b/tenor.gif",
            "https://media.tenor.com/images/f4b4d26df00e1d57006bffb256a848b0/tenor.gif",
            "https://media.tenor.com/images/d4d417d59d14d249f22285405ecec71f/tenor.gif"]


anime_wave=["https://media.tenor.com/images/824a5c6fb0eff4de202d0cd4da1e6692/tenor.gif",
            "https://media.tenor.com/images/3fbae3954123a7815bd235f87eeb2ad3/tenor.gif",
            "https://media.tenor.com/images/fe3e2d08c49445ca807935eba60e5627/tenor.gif"]


@client.event
async def on_ready():
    print("bot is ready!")

@client.event
async def on_member_join(member):
    channel = client.get_channel()

    embed = discord.Embed(title= f"WELCOME TO **{member.guild.name}**", description= f"WELCOME TO OUR SERVER {member.mention}! HOPE YOU ENJOY HERE!", colour = discord.Colour.blue())
    embed.add_field(name = f"READ ALL THE RULES FROM :", value = f"<#772741949789569034>", inline = False)
    embed.add_field(name = f"ASK FOR A ROLE IN THE SERVER :", value = f"<#771694681394249748>", inline = False)
    embed.set_footer(text = "Ducky's club OFFICIAL BOT")
    embed.set_thumbnail(url = member.avatar_url)

    await channel.send(embed = embed)


@client.event
async def on_member_remove(member):
    channel = client.get_channel()
    await channel.send(f"=================================\n{member.display_name} just left the server <:byebye:> \nWe will miss you! \nHope to see you again soon \n=================================")


@client.event
async def on_message(msg):
    guild1=client.get_guild()
    
    if "count member" in  msg.content:
        await msg.channel.send(f"```the number of member in the server {guild1.member_count}```")
    elif "member report" in msg.content:
        x=0
        y=0
        z=0

        for m in guild1.members:
            if m.status == "ONLINE":
                x=x+1
            if m.status == "OFFLINE":
                y=y+1
            else:
                z=z+1
        await msg.channel.send(f"``` Online:{x}.\nIdle/Busy/dnd:{z}.\nOffline:{y}.```")
   
    elif "noice" in msg.content:
        await msg.channel.send("https://media.tenor.com/images/005fab01cec29e687a227fef15057a2d/tenor.gif")
    elif "yeah" in msg.content:
        await msg.channel.send("https://media.tenor.com/images/21010460ecdb9bfd0a495a4bf9929a4f/tenor.gif")
    elif "wtf" in msg.content:
        await msg.channel.send("https://media.tenor.com/images/98e10746fd32c1c7bec76cfc77415f6d/tenor.gif")
    elif "among us" in msg.content:
        await msg.channel.send("https://media.tenor.com/images/b83e9877c1337880961541d3533e12b0/tenor.gif")
    elif "boii" in msg.content:
        await msg.channel.send("sujay sooooo hooooot still a virgin")
    await client.process_commands(msg)
   


@client.command(aliases = ["hello","hi","sup"])
async def hlo(ctx):
    await ctx.send("hi")
    await ctx.send(ctx.author.mention)



@client.command(aliases = ["user","info",])
async def fuckyou(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name ,description= member.mention , color= discord.Colour.red())
    embed.add_field(name="bhosdiwaala" , value = member.id ,inline=False )
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def rainbow(ctx):
    image= 'https://emoji.gg/assets/emoji/1853_Rainbow_Cat.gif'
    embed=discord.Embed()
    embed.set_image(url= image)
    await ctx.send(embed=embed)

@client.command()
async def rainbowcat(ctx):
    await ctx.send("https://emoji.gg/assets/emoji/1853_Rainbow_Cat.gif")

@client.command()
async def boo(ctx):
    await ctx.send("https://emoji.gg/assets/emoji/9892_ghostboo.gif")

@client.command()
async def triggered(ctx):
    await ctx.send("https://c.tenor.com/KXE2S4-PlnUAAAAj/anime-baka.gif")

@client.command()
async def wee(ctx):
    await ctx.send("https://emoji.gg/assets/emoji/2917_baby_dance.gif")

@client.command()
async def blob(ctx):
    await ctx.send("https://emoji.gg/assets/emoji/8608_apartyblob.gif")


@client.command(aliases = ["ducky","duck",])
async def fucky(ctx):
    random_link=random.choice(duck_gif)
   
    await ctx.send(random_link)

@client.command(aliases = ["sad","uww"])
async def anisad(ctx):
    random_link=random.choice(anime_sad)
   
    await ctx.send(random_link)

@client.command()
async def slap(ctx):
    random_link=random.choice(anime_slap)
   
    await ctx.send(random_link)

@client.command()
async def henlo(ctx, member : discord.Member):
    embed = discord.Embed( color= discord.Colour.red())
    embed.add_field(name="Hello " , value = " " , inline=False)
    embed.add_field(name=str(member.display_name) , value=" " , inline=False)
    random_link=random.choice(anime_wave)
    embed.set_image(url = random_link )
    await ctx.send(embed=embed)


@client.command()
async def troll(ctx, member : discord.Member):
    embed = discord.Embed( color= discord.Colour.red())
    embed.add_field(name="Hehehe " ,value=member.name,inline=True )
    embed.set_image(url ="https://emoji.gg/assets/emoji/4887_trollparrot.gif" )
    await ctx.send(embed=embed)


@client.command()
async def slapped(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    random_link=random.choice(anime_slap)       
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))
    await ctx.send(random_link)

@client.command(aliases = ["Helpme"])
async def help(ctx):
    embed = discord.Embed(title = "What can I do?", description = "Use The Prefix -> >", color = discord.Colour.green())
    embed.add_field(name = ">hlo", value = "Say hi to the bot!")
    embed.add_field(name = ">fuckyou", value = "Gives user info!")
    embed.add_field(name='>slapped @mem1 @mem2', value="mem1 slapped mem2",inline=True)
    embed.add_field(name="troll @mem", value='troll gif')

    await ctx.send(embed = embed)

client.run("")
