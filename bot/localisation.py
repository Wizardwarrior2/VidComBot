#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
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

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "𝗛𝗲𝗹𝗹𝗼, \n\n𝗜 𝗮𝗺 𝘃𝗶𝗱𝗲𝗼 𝗰𝗼𝗺𝗽𝗿𝗲𝘀𝘀 𝗯𝗼𝘁  \n\n<b>𝗽𝗹𝗲𝗮𝘀𝗲 𝗦𝗲𝗻𝘁 𝗠𝗲 𝗔𝗻𝘆 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗕𝗶𝗴 𝗙𝗶𝗹𝗲/𝗩𝗶𝗱𝗲𝗼 𝗜 𝗪𝗶𝗹𝗹 𝗖𝗼𝗻𝗽𝗿𝗲𝘀𝘀 𝗔 𝗦𝗺𝗮𝗹𝗹 𝗙𝗶𝗹𝗲/𝗩𝗶𝗱𝗲𝗼</b> \n\n/help 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗗𝗲𝘁𝗮𝗶𝗹𝘀... \n\n𝗕𝘂𝘁 𝗬𝗼𝘂 𝗠𝘂𝘀 𝗝𝗼𝗶𝗻 𝗠𝘆 𝗨𝗽𝗱𝗮𝘁𝗶𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲 :@Mega_Bots_Updates"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 📥 \n"
    
    UPLOAD_START = "📤 𝗨𝗽𝗹𝗼𝗱𝗶𝗻𝗴 📤 \n"
    
    COMPRESS_START = "📀 𝗧𝗿𝘆𝗶𝗻𝗴 𝗧𝗼 𝗖𝗼𝗺𝗽𝗿𝗲𝘀𝘀... 📀"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already One Process going on. \n or \n A media already exists. \n  Please send /cancel to delete existing media. ⚠️"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi am Video Compressor Bot \n\n1. Sent your telegram big video file \n2. Reply the file - /compress And Persentage \nEg:- <code>/compress 50</code> \n\nSupport Group :@Mega_Bots_Updates"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
