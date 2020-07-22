import asyncio

from discord.ext.commands import bot

from display import *
from logs import log_account_sent


username = ['username_1', 'username_2', 'username_3', 'username_4',
            'username_5', 'username_6', 'username_7', 'username_8',
            'username_9', 'username_10', 'username_11', 'username_12',
            'username_13', 'username_14', 'username_15', 'username_16',
            'username_17', 'username_18', 'username_19', 'username_20',
            'username_21', 'username_22', 'username_23', 'username_24']

password = ['password_1', 'password_2', 'password_3', 'password_4',
            'password_5', 'password_6', 'password_7', 'password_8',
            'password_9', 'password_10', 'password_11', 'password_12',
            'password_13', 'password_14', 'password_15', 'password_16',
            'password_17', 'password_18', 'password_19', 'password_20',
            'password_21', 'password_22', 'password_23', 'password_24']


account_position = 0

async def get_next_username_password(requester, client):
    global account_position
    account_position += 1
    if account_position >= len(username):
        account_position = 0
    await log_account_sent(requester, username[account_position], account_position, client)
    return username[account_position], password[account_position]


async def during_match_provided_acc(target_user):
    embed = display_during_match_provided_acc()
    msg = await target_user.send(embed=embed)
    await msg.add_reaction('📢')
    await asyncio.sleep(1)
    await msg.add_reaction('🚫')


async def account_request(account_need):
    account_need: discord.Member
    embed = display_account_rules()
    msg = await account_need.send(embed=embed)
    await msg.add_reaction('✅')
    await asyncio.sleep(1)

# reaction, user = await ctx.bot.wait_for("reaction_add", timeout=45.0, check=predicate)
