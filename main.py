import os
from discord.ext import commands
from discord.ext.commands import bot

from display import *
from accounts import *

client = commands.Bot(command_prefix='=')
client.remove_command('help')


# TODO: Add a =notify feature
# TODO: Add a lobby auto-kick feature
# TODO: Add a match auto-purge feature


@client.command()
@commands.guild_only()
async def help(ctx):
    await ctx.channel.send(f'{ctx.author.mention} Here is a list of the commands you have access to: ')
    embed = help_list(ctx)
    await ctx.channel.send(embed=embed)


@client.event
async def on_reaction_add(reaction, user):
    if not user.bot:
        # in a dm, on a message by the bot
        if reaction.message.channel.type == discord.ChannelType.private and reaction.message.author.id == client.user.id:
            # if the bot sent the same (correct) reaction as the user just responded with
            if reaction.me == True and reaction.count == 2 and reaction.emoji == '✅':
                # unreact (can't be triggered again)
                await reaction.remove(client.user)
                pointer = await increment_return_account_position()
                # send account details (user just confirmed to have read the rules);
                embed = account_info(username[pointer], password[pointer])
                msg = await reaction.message.edit(embed=embed)

@client.command(pass_content=True)
async def test(ctx):
    msg = await account_request(ctx.author)


@client.event
async def on_command_error(message, error):
    if isinstance(error, commands.CommandNotFound):
        await message.send(f'{message.author.mention} Invalid command, please try again.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await message.send(f'{message.author.mention} You must specify a specific person, try again.')
    elif isinstance(error, commands.NoPrivateMessage):
        await message.send(f'{message.author.mention} You can\'t use that command in DMs, sorry.')
    else:
        raise error


@client.event
async def on_member_update(before, after):
    if str(after.status) == "offline":
        if after.mention in lobby:
            after: discord.Member
            remove_lobby(after.mention)
            await after.send(f'You were removed from the PIL Pugs lobby because you went offline. Please rejoin the lobby when you are back online and ready to play!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('')
