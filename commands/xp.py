from math import log
from concurrent.futures import process
import random
import nextcord
from nextcord.ext import commands
import asyncio
import mysql.connector
xp = {}

class xp(commands.Cog):
    def __init__(self, bot: commands.Bot, db) -> None:
        self.bot = bot
        self.messageCounts = {}
        self.db:mysql.connector.MySQLConnection = db

    @commands.Cog.listener()
    async def on_ready(self):
        await self.processXP()

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        # print(self.messageCounts)
        if message.author.bot or message.guild is None:
            return
        if not message.guild.id in self.messageCounts:
            self.messageCounts[message.guild.id] = {}

        if not message.author.id in self.messageCounts[message.guild.id]:
            self.messageCounts[message.guild.id][message.author.id] = 1
            return
        self.messageCounts[message.guild.id][message.author.id] += 1


    async def processXP(self):
        while True:
            await self.calcXP()
            await asyncio.sleep(15)

    async def calcXP(self):
        xpStores = []
        for s in self.messageCounts.keys():
            for u in self.messageCounts[s].keys():
                uX = round(log(self.messageCounts[s][u])+5,0)
                xpStores.append({"server":s,"user":u,"xp":uX})
        await self.storeXP(xpStores)
        self.messageCounts = {}

    async def storeXP(self, xpStore):
        if self.db is None:
            print(xpStore)
            return
        cursor:mysql.connector.connection.MySQLCursor = self.db.cursor()
        cursor.execute("SELECT * FROM xp")
        results = cursor.fetchall()
        members = {}
        for result in results:
            if result[0] not in members:
                members[result[0]] = {}
            members[result[0]][result[1]] = result[2]
            # members = {
            #       guildId: {
            #           memberId: xp        
            #       }
            #   }
        changedData = []
        newData = []
        for user in xpStore:
            if str(user["server"]) in members.keys():
                if str(user["user"]) in members[str(user["server"])].keys():
                    changedData.append((user["server"], user["user"], user["xp"]+members[user["server"]][user["user"]]))
                    continue
            newData.append((user["server"], user["user"], user["xp"]))
        print(newData)