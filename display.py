import discord
from discord.utils import get

from lobby import *
from match import *
from captains import *
from factions import *
from teams import *


def help_list(ctx):
    embed = discord.Embed(
        colour=discord.Color.orange()
    )
    embed.add_field(name='Lobby Commands',
                    value='`=j` - Join the lobby for a match\n'
                          '`=l` - Leave the lobby for a match\n'
                          '`=q` - See the current lobby for a match'
                    , inline=False)
    embed.add_field(name='Team Captain Commands',
                    value='`=faction` `VS`/`NC`/`TR` - Picks a faction\n'
                          '`=pick` `@player` - Picks a player'
                    , inline=False)
    embed.add_field(name='Other Commands',
                    value='`=help` - Brings up this prompt\n'
                    , inline=False)
    user = ctx.author
    role = get(user.roles, name="PIL Pugs Staff")
    if role:
        embed.add_field(name='Admin Match Commands',
                        value='`=clear_queue` - Clears the lobby queue\n'
                              '`=clear_match` - Clears the match roster\n'
                        , inline=False)
    embed.set_footer(text='Made by Rapid',
                     icon_url='https://cdn.discordapp.com/attachments/702303117450018896/717756306190237696/PIL_Logo_toby_dog_prison.png')
    return embed


def lobby_list():
    embed = discord.Embed(
        description="\n".join(lobby),
        colour=discord.Color.orange()
    )
    embed.set_author(name=f'Lobby: {len(lobby)} / 12')
    return embed


def lobby_announcement():
    embed = (f', '.join(lobby) + ', please join the General VC to pick teams.')
    return embed


def match_list():
    team_embed = discord.Embed(
        colour=discord.Color.orange()
    )
    team_embed.add_field(name="Team 1",
                         value=f"Captain: \n {captains[0]} ({factions_team[0]})\n Players:" + "\n".join(
                             team_2),
                         inline=True)
    team_embed.add_field(name="Team 2",
                         value=f"Captain: \n {captains[1]} ({factions_team[1]})\n Players:" + "\n".join(
                             team_1),
                         inline=True)
    team_embed.add_field(name="Remaining", value="Players:" + "\n".join(roster), inline=True)
    return team_embed


def account_rules():
    embed = discord.Embed(
        colour=discord.Color.red(),
        title='Jaeger Account Info:',
        description=f'**MUST READ: [Rules](https://planetsideguide.com/other/jaeger/)**\n',
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/703912354269888572/727931056476389396/PIL_Logo11_Zoomed.png")
    embed.set_footer(
        text='Failure to follow these rules can result in your suspension from   ALL   Jaeger events.\nBy reacting with a checkmark below, you confirm you understand these rules.')
    return embed


def account_info(username, password):
    embed = discord.Embed(
        colour=discord.Color.green(),
        title='Jaeger Account Info:',
        description=f'**MUST READ: [Rules](https://planetsideguide.com/other/jaeger/)**\n'
                    f'Username: `{username}`\n '
                    f'Password: `{password}`',
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/703912354269888572/727931056476389396/PIL_Logo11_Zoomed.png")
    embed.set_footer(
        text='Failure to follow these rules can result in your suspension from   ALL   Jaeger events.\nBy reacting with a checkmark below, you confirm you understand these rules.')
    return embed
