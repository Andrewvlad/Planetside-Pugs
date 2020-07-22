import discord
from discord.utils import get

from lobby import *
from match import *
from captains import get_captain
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
                         value=f"Captain: \n {get_captain(0)} ({factions_team[0]})\n Players:" + "\n".join(
                             team_2),
                         inline=True)
    team_embed.add_field(name="Team 2",
                         value=f"Captain: \n {get_captain(1)} ({factions_team[1]})\n Players:" + "\n".join(
                             team_1),
                         inline=True)
    team_embed.add_field(name="Remaining", value="Players:" + "\n".join(roster), inline=True)
    return team_embed


def display_account_rules():
    # dm to be read and accepted before details given out to players that need to be provided accounts
    embed = discord.Embed(
        colour=discord.Color.red(),
        title='Jaeger Account Info:',
        description=f'**MUST READ: [Rules](https://planetsideguide.com/other/jaeger/)**\n',
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/703912354269888572/727931056476389396/PIL_Logo11_Zoomed.png")
    embed.set_footer(
        text=f'Failure to follow these rules can result in your suspension from   ALL   Jaeger events.\n'
            f'By reacting with a checkmark below, you confirm you understand these rules.')
    return embed


def display_account_info(username_password):
    # dm with account details for players that need them
    embed = discord.Embed(
        colour=discord.Color.green(),
        title='Jaeger Account Info:',
        description=f'**MUST READ: [Rules](https://planetsideguide.com/other/jaeger/)**\n'
                    f'Username: `{username_password[0]}`\n '
                    f'Password: `{username_password[1]}`',
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/703912354269888572/727931056476389396/PIL_Logo11_Zoomed.png")
    embed.set_footer(
        text=f'Failure to follow these rules can result in your suspension from   ALL   Jaeger events.\n'
            'By reacting with a checkmark below, you confirm you understand these rules.')
    return embed


def display_during_match_provided_acc():
    embed = discord.Embed(
        colour = discord.Color.orange(),
        title = f'Match in Progress:\n'
                f'{get_captain(0)} vs {get_captain(1)}',
        description = f'Game in progress! If you have issues with your account, or with players in your game, use the buttons below to report issues.\n'
                    f'Use the  📢  reaction to report an issue with the account; password not working, fewer than 100,000 certs on a character.\n'
                    f'Use the  🚫  reaction to report an issue with a player ingame; Toxicity/Harassment, repeated rules violations, etc.',
    )
    # logo uses up too much space in the embed box
    #embed.set_thumbnail(
        #url="https://cdn.discordapp.com/attachments/703912354269888572/727931056476389396/PIL_Logo11_Zoomed.png")
    return embed


def display_during_match_own_acc():
    return

def display_log_account_sent(requester_member, username, pointer):
    pointer += 1 #1-based
    embed = discord.Embed(
        colour = discord.Color.blurple(),
        title = f'Account {pointer}\'s Details Sent:',
        description = f'{requester_member.display_name} ({requester_member.name}#{requester_member.discriminator})\n'
                    f'has been given the account details for {username}, account #{pointer}.'
    )
    embed.set_thumbnail(
        url=f"{requester_member.avatar_url}")
    embed.set_footer(
        text=f'user id: {requester_member.id}')
    return embed
