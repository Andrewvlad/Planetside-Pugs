import asyncio
import discord

from display import display_log_account_sent

async def log_account_sent(requester, username, pointer, client):
    logging_channel_id = '734807076672372760' # (734807076672372760 = Planetside Pugs Test #bot-test)
    public_guild_id = '734509290609442836' # (734509290609442836 = Planetside Pugs Test)

    # turns the requester (a discord User) into a guild Member from the public server (much more info)
    requester_member = client.get_guild(int(public_guild_id)).get_member(requester.id)
    logging_channel = client.get_channel(int(logging_channel_id))
    
    embed = display_log_account_sent(requester_member, username, pointer)
    await logging_channel.send(embed=embed)
