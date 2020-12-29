# Copyright (C) 2020 FireganqQ
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#
# FireqanQUserBot - FireganqQ

""" UserBot yardım komutu """

from userbot.cmdhelp import CmdHelp
from userbot import cmdhelp
from userbot import CMD_HELP
from userbot.events import register

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("__fireqanq")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.fg(?: |$)(.*)")
async def _(event):
    """ .fg komutu için """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(LANG["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [sorted(list(CMD_HELP))[i:i + 5] for i in range(0, len(sorted(list(CMD_HELP))), 5)]

        for i in sayfa:
            string += f'`⏩ `'
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n\n"
        await event.edit(LANG["NEED_MODULE"] + '\n\n' + string)
