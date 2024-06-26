#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Prince Mendiratta
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import (
    Client,
    __version__,
    enums
)
from . import (
    API_HASH,
    API_ID,
    LOGGER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS
)
import threading
from bot.__banner.banner import bannerTop
import sys


class Bot(Client):
    """ modded client for NU-Alert-Bot """

    def __init__(self):
        super().__init__(
            "NU-Alert-Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=TG_BOT_TOKEN,
            plugins={
                "root": "bot/plugins"
            },
            workers=TG_BOT_WORKERS
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        banner = bannerTop()
        self.LOGGER(__name__).info("\n{}".format(banner))
        self.LOGGER(__name__).info(
            f"\n\n[*] @{usr_bot_me.username} based on Pyrogram v{__version__}\n"
            "[*] Send /init in chat to start scraping.\n\n"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("[*] NU-Alert-Bot stopped. Bye.")
        sys.exit()
