# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2017 SML

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import discord
from discord.ext import commands
from discord.ext.commands import Context
from .utils import checks
from random import choice
from __main__ import send_cmd_help
import colorsys
import asyncio
import os
import datetime
import aiohttp
import hsluv
# from .economy import Economy


class Magic:
    """Magic username"""
    def __init__(self, bot):
        self.bot = bot
        self.magic_is_running = False

        self.role_color = discord.Color(value=int("242424", 16))

        self.hue = 0

        # # construct magic color table
        # self.magic_colors = []
        # self.magic_color_id = 0
        # for x in range(0, 360):
        #     color = colorsys.hsv_to_rgb(x, 0.5, 1)
        #     self.magic_colors.append(
        #         tuple(int(i * 255) for i in color))


    @commands.group(pass_context=True)
    @checks.mod_or_permissions()
    async def magic(self, ctx:Context):
        """Magic role with ever changing username color"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @magic.command(name="start", pass_context=True)
    @checks.mod_or_permissions()
    async def magic_start(self, ctx:Context):
        """Starts the magic role."""
        server = ctx.message.server
        magic_role_name = "Magic"
        magic_role = [
            r for r in server.roles
            if r.name == magic_role_name].pop()

        self.magic_is_running = True



        while self.magic_is_running:
            self.hue = self.hue + 10
            self.hue = self.hue % 360
            # await self.bot.say("hue: {}".format(self.hue))
            # await self.bot.say("rgb: {}".format(hsluv.hsluv_to_rgb((self.hue, 50, 50))))
            hex = hsluv.hsluv_to_hex((self.hue, 90, 60))
            # await self.bot.say("hex: {}".format(hex))
            hex = hex[1:] # remove '#'
            color_int = int(hex, 16)
            new_color = discord.Color(value=int(hex, 16))

            await self.bot.edit_role(
                server,
                magic_role,
                color=new_color)

            # await self.bot.say(self.role_color)
            # self.role_color = self.get_next_color(self.role_color)

            # await self.bot.say(self.get_next_color(magic_role.color))
                # color=self.get_random_color())
            await asyncio.sleep(0.5)


    @magic.command(name="stop", pass_context=True)
    @checks.mod_or_permissions()
    async def magic_stop(self, ctx):
        """Stops magic role"""
        self.magic_is_running = False


    def get_random_color(self):
        """Return a discord.Color instance of a random color."""
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        return discord.Color(value=color)

def setup(bot):
    r = Magic(bot)
    # bot.add_listener(r.member_join, "on_member_join")
    bot.add_cog(r)



"""
Sample code for timer events

https://github.com/Rapptz/discord.py/blob/master/examples/background_task.py

import discord
import asyncio

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='channel_id_here')
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, counter)
        await asyncio.sleep(60) # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(my_background_task())
client.run('token')

"""
"""

https://github.com/tekulvw/Squid-Plugins/blob/master/scheduler/scheduler.py

loop = asyncio.get_event_loop()
loop.create_task(self.check())

async def check(self):
    while True:
        # do some stuff
        await asyncio.sleep(3600)

"""