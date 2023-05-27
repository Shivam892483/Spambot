from DEADLYSPAM import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from DEADLYSPAM import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/86f7674656cd38321316d.jpg"

DEAD_Help = "🔥 Sʜɪᴠᴀᴍ Sᴘᴀᴍ Bᴏᴛ 🔥\n\n"
 
DEAD_Help += f"__ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ Sʜɪᴠᴀᴍ Sᴘᴀᴍ ʙᴏᴛ__\n\n"

DEAD_Help += f" ↧ sᴘᴀᴍʙᴏᴛ 𝙲𝙼𝙳𝚂 ↧\n\n"

DEAD_Help += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n\n"
 
DEAD_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

DEAD_Help += f" `!leave` - to leave public/private channel/groups\n\n"
 
DEAD_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

DEAD_Help += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!bspam` - this cmd use for spamming on someone birthday!!\n `!delayspam` - this cmd use for delay spam\n\n"

DEAD_Help += f" !pornspam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"

DEAD_Help += f"© @Earn_without_investment01\n"


@BOT0.on(events.NewMessage(incoming=True, pattern='!help'))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DEAD_Help,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Earning_with_shivam_official"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Earn_without_investment01")
        ] 
        ]
        )
