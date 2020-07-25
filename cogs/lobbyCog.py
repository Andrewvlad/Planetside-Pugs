import random

from discord.ext import commands
from display import *
from lobby import *
from teams import *
from other import *


class LobbyCog(commands.Cog):
    """
    A class used to contain all of the general lobby commands

    Methods
    -------
    on_ready(self)
        Prints that the cog is running on startup
    """

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Lobby Cog is online')

    """
    Registered Commands:

    !join
    !leave
    !queue
    """

    @commands.command()
    @commands.guild_only()
    async def j(self, ctx):
        if ctx.author.mention in lobby:
            await ctx.channel.send("You're already queued for a match!")
        elif ctx.author.mention in get_match() or ctx.author.mention in get_roster()[0] or ctx.author.mention in get_roster()[1]:
            await ctx.channel.send("You're already in a match!")
        elif str(ctx.author.status) == "offline":
            await ctx.channel.send("You can't join a queue if your Discord status is offline/invisible!")
        elif len(lobby) < 12:
            add_lobby(ctx.author.mention)
            await ctx.channel.send("You've been added to the queue!")
        else:
            await ctx.channel.send(
                "It seems like the lobby is full! Please wait just one moment for a staff member to fix the issue :)")
        await ctx.channel.send(embed=lobby_list())
        if len(lobby) == 12:
            if get_match():
                await ctx.channel.send(
                    "There is currently a match being picked right now, please try again after picking is finished")
            else:
                set_match()
                set_captain(get_match()[random.randint(0, 11)])
                set_captain(get_match()[random.randint(0, 10)])
                pick_force()
                await ctx.channel.send(embed=match_list())

    @commands.command()
    @commands.guild_only()
    async def l(self, ctx):
        if ctx.author.mention in lobby:
            remove_lobby(ctx.author.mention)
            await ctx.channel.send("You've been removed from the queue.")
        else:
            await ctx.channel.send("You're not queued for a match!")
        await ctx.channel.send(embed=lobby_list())

    @commands.command()
    @commands.guild_only()
    async def q(self, ctx):
        await ctx.channel.send(embed=lobby_list())


def setup(client):
    client.add_cog(LobbyCog(client))
