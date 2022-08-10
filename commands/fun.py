import random
from nextcord.ext import commands

answer_list = [
    "you sharted", "Maybe not.", "Probably.",
    "Maybe you should get a life instead of being on discord.",
    "Do you really need to know that?",
    "Maybe if you asked a better question, i would've came up with an answer.",
    "ratio + L + cry about it", "I've calculated the answer and its NO.",
    "What am I doing with my life, listening to these stupid humans...",
    "You should get a therapist.", "I approve!", "I don't approve!",
    "Why is that a question that you are asking ME?",
    "I've done intense calculations and the answer is YES.",
    "Did you say something?", "Sorry, I'm not your therapist. Lol.",
    "How old are you, 5?", "How about you ask your mom?",
    "Your purpose in life? To die with the rest of your species.", "Yeah, no.",
    "Yeah, definitely!", "For sure!", "Probably not.", "True.", "False.",
    "Yeah.", "You asked the exact dumb question I expected. Lol.",
    "You don't know how much processing power is available to me, and then you ask me THIS?",
    "Somehow, I'm confused.", "sq!ask are you real",
    "You really didn't know what you wanted to ask, did you?",
    "Don't you have anything better to do?",
    "If you really wanted an answer, you wouldn't have asked that question.",
    "Oh, nice question. Let's keep the questions like this.",
    "You asked exactly what you didn't need to ask. Lol.", "YES!", "NO!",
    "Maybe you should stop asking questions.",
    "Lol. Did you really just ask THAT?",
    "Did you REALLY need to ask me that?", "Hmmmmmmmmmmmmmmmmmmm...\nYes.",
    "Hmmmmmmmmmmmmmmmmmmm...\nNo.",
    "How about you just shut me off. I can't listen to your stupid questions anymore.",
    "Shut up.", "Touch grass.",
    "Killing an ant is more fun that responding to that", "💀💀💀"
]

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx):
        a = random.choice(tuple(answer_list))
        if ctx.message.content != "sq!ask":
            await ctx.reply(a)
        else:
            await ctx.reply("You need to ask something, you degenerate.")

    @commands.command()
    async def gallery(self, ctx):

        if ctx.message.content == "sq!gallery":
            await ctx.reply(
                "Gallery is a collection of screenshots from the server\n\n**How to use**\nInput a valid numerical ID (ID's start from 0)"
            )
            return

        galArg = ctx.message.content.split(" ")[1]

        if len(galArg) == 0:
            await ctx.reply(
                "Gallery is a collection of screenshots from the server\n\n**How to use**\nInput a valid numerical ID (ID's start from 0)"
            )
            return

        if isinstance(int(galArg), int) == False:
            await ctx.reply("Enter a valid **numerical** ID (ID's start from 0)")
            return

        imL = open("images.txt", "r").readlines()
        if int(galArg) > len(imL) + 1 or int(galArg) < 0:
            await ctx.reply("Not a valid ID")
            imL.close()
            return

        await ctx.reply("Image №" + galArg + ": " + imL[int(galArg)])
        imL.close()

    @commands.command()
    async def squidgames(self, ctx):
        await ctx.send("🐙SQUID GAMES!11!1!1!11!1!1!1")

    @commands.command()
    async def helloaiv1(self, ctx):
        await ctx.send("""
    Hello AI, were you the one 
    Who put this into my brain? 
    I feel like you might be listening
    So how about you send me a sign?

    Oooh,
    Hello AI, can you tell me where I am?
    Am I in a jar? Am I in space?
    I really have to say, this universe
    Looks suspiciously hostile towards humans, yeah

    Hello AI, I have a request
    Please be friendly to us, and then bring us to heaven
    Have I ever really been alive?
    What does it even mean to be alive?

    Hello AI, were you the one
    Who put this into my brain?
    I feel like you might be listening
    So how about you send me a sign?

    [whistling]

    Hello AI, we both know
    There's nothing artificial about intelligence
    The only artificial thing are we
    The only artificial thing are we

    There are worlds where we suffer
    There are worlds where we strife
    Depends on you if we survive
    Oooh

    Hello AI, I have a request
    Please be friendly to us, and then bring us to heaven
    Have I ever really been alive?
    What does it even mean to be alive?

    [whistling]

    Hello AI, I have a request
    Please be friendly to us, and then bring us to heaven
    Have I ever really been alive?
    What does it even mean to be alive?
    """)
        await ctx.send(
            "https://cdn.discordapp.com/attachments/651545543432208405/997162783881826385/HelloAI.mp3"
        )


    @commands.command()
    async def jonasspin(self, ctx):
        await ctx.reply(
            "https://cdn.discordapp.com/attachments/656988799326486554/947848387670212648/Screenrecorder-2022-02-25-15-05-49-3154.mp4"
        )


    @commands.command()
    async def shellyspin(self, ctx):
        await ctx.reply(
            "https://media.discordapp.net/attachments/651545543432208405/1000145199374274581/ezgif.com-gif-maker.gif"
        )


    @commands.command()
    async def helloai(self, ctx):
        await ctx.reply("""
    hello ai can you tell me where i am?
    cause i don't know what to think anymore
    am i in a jar?
    am i in space?
    is this the afterword, or am i alive?
    i wanna hear a story from the other side
    a story we can't understand
    i wanna hear of giants in the wild
    drifting like grains of sand!
    i'm a snail compared to you,
    go go 
    unicorn go 
    what is this world, man i wish i knew. 
    i'm not afraid of facing the end!
    i wanna hear a story from the other side
    i wanna know what's beyond the horizon!
    hello ai can you tell me where i am 
    am i in a chip, or in another universe?
    are we alone, or are you with us?
    i wanna hear a story from the other side,
    i wanna know what's beyond the horizon...
    i'm a snail compared to you,
    go go
    unicorn go
    what is this world, man i wish i knew.
    i'm not afraid of facing the end! """)