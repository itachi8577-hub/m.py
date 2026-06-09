# ============================================================
# itachi_ultimate_bot.py - ULTIMATE PRO MAX BOT 🔥🔥🔥
# pip install telethon
# ============================================================

import asyncio
import json
import os
import random
import time
import math
from datetime import datetime
from telethon import TelegramClient, events, Button
from telethon.tl.types import MessageEntityTextUrl, MessageEntityMentionName

# =====================================================================
# ⚙️ CONFIG - APNA YAHI DAALO
# =====================================================================
API_ID = 24923714
API_HASH = '040929ee690bdb53b36484e017310358'
BOT_TOKEN = '8740442137:AAF2WAdztdbg37LRMiwWjX3DkPCJ3icIz74'  # @BotFather se lo
OWNER_ID = 7862394625  # Teri ID

SUDO_USERS = [OWNER_ID]
bot_status = "online"
raid_active = {}
raid_speed = 1.5
GROUPS_CACHE = []
muted_users = {}
USER_STATES = {}
BOT_USERNAME = ""

# =====================================================================
# 📁 AUTO FILE SYSTEM
# =====================================================================
DEFAULT_RAID_LINES = [
    "TERI MAKI CHUT MADARCHODO HIZDA HAI HAI TUM MADARCHODO BOL DE YUTA TERA BAAP HAI WARNA TERI KI CHUT KOI RAMDI KI AULAD NHI BACHA PAYEGA AAJ SAMJH LE MADRCHOD",
    "AIR JORDEN KE JUTE SE TERI KI CHUT PR MAAR MAAR KE LAAL KR DUNGA KALI SE LAAL 😋🥵 RANDI MADARCHODO",
    "MADARCHODO BAAP SE LADEGA APNE TERI MA KI CHUT KHA JAUNGA RAMDI",
    "TERI MAA KI CHHUT KA KHAA JAUNGAA MADARCHODO RANDI KI AULAD SPAM KARTA HAI MADARCOD KE CHAKKE KI AULAD TERE BAAP KO GADHE KE LAND SEE CHODUNGA",
    "TERI MAKI CHUT MADARCHOD SUR KE LAND SE MA CHODUNGA GANDI CHUT KI KALI AULAD FATI KALI CHUT KI AULD CHAMR TERI MAIYA KI CHUT KO CHOR BAZR ME BECHUNGA MADRACHOD",
    "TERI MAIYA KE KI CHUT ME APNE LAND KA PYTHON BOT BANA KR RUN KRUNGA TERI SASTI SPAM USER BOT KA BHOSDA MADARCHODO",
    "TERI MAIYA KA BHOSDA MADARCHODO SASTI GB RAOD KI RANDI KI AULAD",
    "FATI KALI CHUT KI AULD CHAMR TERI MAIYA KI CHUT KO CHOR BAZR ME BECHUNGA MADRACHOD",
    "TERI MAKICHUT KO KUTTO KO KHILA DUNGA RANDI KI SASTSTI AULAD MADARCHODO",
    "TERI MUMMY KI CHUT BSDK 🖕",
    "SUN BHSDIKE, TU APNI MA KI CHUT ME PANI BHAR KE AA RHA HAI KYA? TERI MAKI CHUT KA ANGUTHI KE BARABAR BHI KOI VALUE NAHI HAI, MADARCHOD KAHIN KA. TERI BEHEN KI CHUT KA CHAKKAR MEIN TERA BAAP BHI KUCH NAHI KAR PAYEGA. TERI GAAND ME 4 GOLIYAN MAR KE TUMHE BHAGWA CHOLA PEHNA DUNGA.",
    "MADARCHOD! TERI MAIYA NE TO MUJHE BATAYA KI TU ABHI TAK BACHON WALI NIKKAR PEHENTA HAI. TERI BEHEN TO MERI RANDI HAI AUR TERI MAA MERI RAKHAIL.",
    "BAHEN KE LODE! TUJHE LAGTA HAI TU BOHOT BADA AAYA HAI? TERI MAIYA TO MERI CHODI HUI MALKIN HAI.",
    "TERI MAIYA KI CHUT ME MERA LUND ITNA ZOR SE GHOOSTA HAI JAISE STADIUM KE FLOOD LIGHTS CHAL RAHI HO.",
    "RANDI KI AULAD! TERI MAIYA TO MERI AAFAT HAI AUR TU MERA FAN. TERI MAA KI CHUT ME TO BOHOT ZYADA TRAFFIC HAI.",
    "CHUTIYA TU MAA CHUDANE AAYA HAI? TERI MAIYA TO MERI RANDI LIST ME HIGHEST RATED HAI.",
    "TERI MAA KI CHUT ME MERA LUND BSDK 🍆💦",
    "TERI GAAND PHAT GAYI KYA BHAG KYA RHA HAI 🏃💨",
    "TERI MAA NE MUJHE BOLYA KO GHAS MAT KHILA 💀",
    "TERI MAA KI CHUT KA KERA HAI TU 🤡",
    "TERI BEHEN KO DEKH KE MERA LUND KHARA HO GYA 😏",
    "TU APNI MAA KA DUDH PEENA BAND KAR DE 🍼",
    "TERI BEHEN KI CHUT ME 5 BIHARI EK SAATH 🥵",
    "TERI SHAKAL DEKH KE MERA LUND MURJHA GYA 🥀",
    "TERI BEHEN TO MERI EX HAI AB TERI MAA MERI CURRENT HAI 😎",
    "TERA BAAP BHI RANDI KI AULAD HAI SALE 🚮",
    "TERI MAA KI CHUT ME PARKING LOT 🅿️",
    "TERI BEHEN KI CHUT ME WIFI CHALTA HAI 📶",
    "TERI BEHEN TO MERI FAVORITE RANDI HAI 💋",
    "TERI MAA KI CHUT ME CLOUD STORAGE ☁️",
    "TERI BEHEN KI CHUT ME BLUETOOTH CONNECT 📱",
    "TERI MAA KI CHUT KA SUBSCRIBER HU MAI 🔔",
    "TERI MAA KO CHOD KE THAK GYA HU 💦",
    "TERI BEHEN KA ONLYFANS TOP DONATION MAI HU 👑",
    "TERI BEHEN KO CHODTA HU TO AWAZ AATI HAI OYE HAYE 🎵",
    "TERI BEHEN KI CHUT KA RENT 500 HAI 💵",
    "TERI BEHEN KO DEKH KE MERA LUND BOLTA HAI AAJA 🗣️",
    "TERI BEHEN KA VIRGINITY MAINE LI THI 🏆",
    "TERI BEHEN KE MUH ME MERA LUND 💯",
    "TERI BEHEN KO RANDI BANA KE CHODTA HU 🎯",
    "TERI BEHEN TO MERI SUGARMAMMY HAI 🍭",
    "TERI BEHEN KE MUH KA SWAD CHANG HAI 👅",
    "TERI BEHEN KO RANDI BANANE KA MASTER HU MAI 🧠",
    "TERI BEHEN KI CHUT KA TOLL FREE NUMBER 📞",
    "TERI BEHEN KI CHUT KA PIN 7860 📌",
    "TERI BEHEN KI CHUT KA RATE LIST 💲",
    "TERI BEHEN KI CHUT KA CATALOG 📚",
    "TERI BEHEN KI CHUT KA LOCATION 📍",
    "TERI BEHEN KI CHUT KA COLOR BLACK 🖤",
    "TERI BEHEN KI CHUT KA STOCK AVAILABLE 📦",
    "TERI BEHEN KI CHUT KA OFFER ZONE 🏷️",
    "TERI BEHEN KI CHUT KI QUALITY AAA ✅",
    "TERI BEHEN KI CHUT KA TRACK RECORD 🏅",
    "Teri maa ki chut teri behen ka bhosda 🖕",
    "Madarchod teri aukaat nahi hai bhaag yahan se 🤬",
    "Bhadwe teri maa ki chut itna attitude kahan se laata hai 🖕",
    "Itni shakal buri ki aaina bhi tod de 🔥",
    "Teri photo dekh ke darwaza chod de itna ugly hai tu 🤣",
    "Main aag hoon jo jalati hai aur raakh mein bhi chamakti hai 🔥",
    "Meri aukaat nahi meri shaan hai 👑",
    "Teri shaadi kab hai? Maa ne kaha ghar par rakh legi 😂",
    "Tu itna smart hai ki duniya ko laga tera baap ka paisa hai 🤣",
]

DEFAULT_SHAYARI = {
    "love": ["Tumse milna ek khwab tha jo ab hakikat ban gaya 💕", "Teri aankhon mein kho jaaun chaand bhi sharmaa jaaye 🌙"],
    "sad": ["Tanhaiyon mein aansu bahate hain aur yaad tumhari aati hai 😔", "Har jagah teri kami hai dil toot gaya 💔"],
    "roast": ["Itni shakal buri ki aaina bhi tod de 🔥", "Teri photo dekh ke darwaza chod de 🤣"],
    "romantic": ["Teri aankhon mein kho jaaun itna pyaar karta hoon 💘", "Raat ko teri yaad aati hai neend nahi aati 🌙"],
    "attitude": ["Main aag hoon jo jalati hai aur raakh mein bhi chamakti hai 🔥", "Meri aukaat nahi meri shaan hai 👑"],
    "abuse": ["Madarchod teri aukaat nahi hai bhaag yahan se 🤬", "Bhadwe teri maa ki chut itna attitude kahan se laata hai 🖕"],
    "funny": ["Teri shaadi kab hai? Maa ne kaha ghar par rakh legi 😂", "Tu itna smart hai ki duniya ko laga tera baap ka paisa hai 🤣"],
}

# Auto create files
for fname, fdata in [("raid_lines.json", DEFAULT_RAID_LINES), ("shayari.json", DEFAULT_SHAYARI)]:
    if not os.path.exists(fname):
        with open(fname, "w") as f: json.dump(fdata, f, indent=4)

if not os.path.exists("stickers.json"):
    with open("stickers.json", "w") as f: json.dump({"saved": []}, f, indent=4)
if not os.path.exists("muted_users.json"):
    with open("muted_users.json", "w") as f: json.dump({}, f, indent=4)
if not os.path.exists("settings.json"):
    with open("settings.json", "w") as f: json.dump({"photo_url": "https://picsum.photos/400/400"}, f, indent=4)
if not os.path.exists("groups.json"):
    with open("groups.json", "w") as f: json.dump([], f, indent=4)

def read_json(path):
    try:
        with open(path) as f: return json.load(f)
    except: return {}

def write_json(path, data):
    with open(path, "w") as f: json.dump(data, f, indent=4)

raid_lines = read_json("raid_lines.json")
shayari_data = read_json("shayari.json")
sticker_data = read_json("stickers.json")
settings = read_json("settings.json")
muted_users = read_json("muted_users.json")
GROUPS_CACHE = read_json("groups.json")

# =====================================================================
# 🤖 BOT INIT
# =====================================================================
bot = TelegramClient('itachi_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# =====================================================================
# 🔐 HELPERS
# =====================================================================
async def is_auth(user_id):
    return user_id == OWNER_ID or user_id in SUDO_USERS

def get_mention(user):
    """REAL TAG/MENTION - bina username ke bhi!"""
    return f"[{user.first_name}](tg://user?id={user.id})"

async def resolve_target(event, args):
    if event.is_reply:
        rep = await event.get_reply_message()
        return rep.sender_id, rep.sender
    if args:
        try:
            target = args[0]
            if target.startswith("@"):
                u = await bot.get_entity(target)
                return u.id, u
            return int(target), await bot.get_entity(int(target))
        except:
            return None, None
    return None, None

def update_groups_sync():
    """Load groups from file"""
    global GROUPS_CACHE
    try:
        GROUPS_CACHE = read_json("groups.json")
    except:
        GROUPS_CACHE = []
    return GROUPS_CACHE

def save_groups():
    write_json("groups.json", GROUPS_CACHE)

# =====================================================================
# 🚫 MUTE CHECK
# =====================================================================
@bot.on(events.NewMessage(incoming=True))
async def mute_checker(event):
    if not event.sender_id: return
    if event.sender_id == OWNER_ID or event.sender_id in SUDO_USERS: return
    cid = str(event.chat_id)
    uid = event.sender_id
    if cid in muted_users and uid in muted_users[cid]:
        try:
            await asyncio.sleep(0.05)
            await event.delete()
        except: pass

# =====================================================================
# 📋 MAIN COMMAND HANDLER
# =====================================================================
@bot.on(events.NewMessage(pattern=r'^[\.\/\!]'))
async def command_handler(event):
    global bot_status, raid_active, raid_speed, SUDO_USERS, muted_users, BOT_USERNAME, GROUPS_CACHE
    
    text = event.text.strip()
    user = await event.get_sender()
    user_id = user.id
    chat_id = event.chat_id
    
    cmd_full = text[1:].strip()
    parts = cmd_full.split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    
    if not BOT_USERNAME:
        me = await bot.get_me()
        BOT_USERNAME = me.username
    
    known = ['alive', 'start', 'menu', 'off', 'ping', 'speed', 'id', 'info', 'sudo', 'sudolist',
             'r', 'rr', 'rrr', 's', 'addline', 'lines', 'mute', 'unmute', 'shayari', 'addsticker',
             'sticker', 'broadcast', 'tagbroadcast', 'chatbox', 'hack', 'spam', 'quote', 'calc',
             'joke', 'gc', 'restart', 'truth', 'dare', 'setphoto', 'addsudo', 'remsudo', 'botstats',
             'forward', 'mutedlist', 'delallraid', 'shayaritypes']
    
    if cmd not in known:
        await event.reply(f"╔══════════════════════╗\n"
                          f"   ❌ **GALT COMMAND** ❌\n"
                          f"╚══════════════════════╝\n\n"
                          f"😤 `{text}` ye command exist nahi karti!\n"
                          f"📋 /menu se saari commands dekho!")
        return
    
    # ===== .alive =====
    if cmd == "alive":
        if not await is_auth(user_id):
            return await punish_unauthorized(event)
        bot_status = "online"
        me = await bot.get_me()
        update_groups_sync()
        
        await event.reply(
            f"╔══════════════════════════════════╗\n"
            f"   🔥 **BOT IS NOW ONLINE** 🔥\n"
            f"╚══════════════════════════════════╝\n\n"
            f"🤖 **Bot:** @{me.username}\n"
            f"👑 **Owner:** {get_mention(await bot.get_entity(OWNER_ID))}\n"
            f"🆔 **Owner ID:** `{OWNER_ID}`\n"
            f"⚡ **Mode:** `ACTIVE & LETHAL`\n"
            f"🔑 **Sudo Users:** `{len(SUDO_USERS)}`\n"
            f"📦 **Groups:** `{len(GROUPS_CACHE)}`\n"
            f"📜 **Raid Lines:** `{len(raid_lines)}`\n"
            f"🔇 **Muted Users:** `{sum(len(v) for v in muted_users.values())}`\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"❤️ **TELEPHON + PYTHON**\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"✅ **BOT ONLINE! SAB COMMANDS READY!**"
        )
        return
    
    # ===== Bot offline check =====
    if bot_status == "offline" and cmd not in ["alive", "start", "menu"]:
        await event.reply(f"╔══════════════════════╗\n"
                          f"   ❌ **BOT OFFLINE** ❌\n"
                          f"╚══════════════════════╝\n\n"
                          f"😴 Bot so raha hai!\n🚀 Pehle `.alive` karein!")
        return
    
    # ===== Auth check =====
    if not await is_auth(user_id):
        return await punish_unauthorized(event)
    
    # ===== /menu =====
    if cmd in ["start", "menu"]:
        me = await bot.get_me()
        btns = [
            [Button.inline("👤 MY OWNER", data="owner")],
            [Button.inline("📋 FULL COMMAND LIST", data="cmd_list")],
            [Button.url("➕ ADD ME YOUR GROUP", f"https://t.me/{me.username}?startgroup=true")],
            [Button.inline("💬 CHAT BOX", data="chatbox_menu"), Button.inline("📢 BROADCAST", data="bc_menu")],
        ]
        await event.reply(
            f"╔══════════════════════════════╗\n"
            f"   🔥 **ULTIMATE PRO MAX BOT** 🔥\n"
            f"╚══════════════════════════════╝\n\n"
            f"👋 {get_mention(user)}!\n\n"
            f"⚡ **Status:** `{'🟢 ONLINE' if bot_status == 'online' else '🔴 OFFLINE'}`\n"
            f"👑 **Owner:** `{OWNER_ID}`\n"
            f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            buttons=btns
        )
        return
    
    # ===== .off =====
    if cmd == "off":
        bot_status = "offline"
        raid_active = {}
        await event.reply(f"╔══════════════════════╗\n"
                          f"   ❌ **BOT OFFLINE** ❌\n"
                          f"╚══════════════════════╝\n\n"
                          f"🔴 Bot so gaya!\n🟢 .alive se uthao!")
        return
    
    # ===== .ping =====
    if cmd == "ping":
        start = time.time()
        m = await event.reply("📡 Pinging...")
        end = time.time()
        ping = round((end-start)*1000, 2)
        await m.edit(f"⚡ **PONG!** `{ping}ms`\n🚀 **Bot:** FAST MODE")
        return
    
    # ===== .speed =====
    if cmd == "speed":
        await event.reply(f"🚀 **Raid Speed:** `{raid_speed}s`\n⚡ **Mode:** FAST 🔥")
        return
    
    # ===== .id =====
    if cmd == "id":
        await event.reply(
            f"👤 **Name:** {get_mention(user)}\n"
            f"🆔 **ID:** `{user_id}`\n"
            f"📛 **Username:** @{user.username if user.username else 'N/A'}\n"
            f"👑 **Owner:** {'✅' if user_id==OWNER_ID else '❌'}\n"
            f"🔑 **Sudo:** {'✅' if user_id in SUDO_USERS else '❌'}"
        )
        return
    
    # ===== .info =====
    if cmd == "info":
        target_id, target_user = await resolve_target(event, args)
        if not target_id:
            await event.reply("❌ Usage: `.info @username`")
            return
        try:
            u = target_user or await bot.get_entity(target_id)
            await event.reply(f"👤 {get_mention(u)}\n🆔 `{u.id}`\n📛 @{u.username if u.username else 'N/A'}")
        except Exception as e:
            await event.reply(f"❌ Error: {e}")
        return
    
    # ===== .sudo =====
    if cmd in ["sudo", "addsudo"]:
        if user_id != OWNER_ID:
            await event.reply("❌ Sirf owner!")
            return
        target_id, target_user = await resolve_target(event, args)
        if not target_id:
            await event.reply("❌ Usage: `.sudo @username`")
            return
        if target_id == OWNER_ID:
            await event.reply("❌ Owner khud sudo nahi!")
            return
        if target_id in SUDO_USERS:
            await event.reply("❌ Pehle se sudo hai!")
            return
        SUDO_USERS.append(target_id)
        u = target_user or await bot.get_entity(target_id)
        await event.reply(
            f"╔══════════════════════╗\n"
            f"   🔑 **SUDO ADDED** 🔑\n"
            f"╚══════════════════════╝\n\n"
            f"👤 {get_mention(u)}\n🆔 `{target_id}`\n\n"
            f"🎉 **Aapko sudo mil gaya!**\n✅ Aap ab bot use kar sakte hain!"
        )
        return
    
    if cmd == "remsudo":
        if user_id != OWNER_ID:
            await event.reply("❌ Sirf owner!")
            return
        target_id, _ = await resolve_target(event, args)
        if not target_id:
            await event.reply("❌ Usage: `.remsudo @username`")
            return
        if target_id in SUDO_USERS:
            SUDO_USERS.remove(target_id)
            await event.reply(f"✅ Sudo hata diya!")
        else:
            await event.reply("❌ Yeh sudo nahi hai!")
        return
    
    if cmd == "sudolist":
        text = "🔐 **SUDO USERS LIST**\n\n"
        for sid in SUDO_USERS:
            try:
                u = await bot.get_entity(sid)
                text += f"• {get_mention(u)} - `{sid}`\n"
            except:
                text += f"• `{sid}`\n"
        await event.reply(text)
        return
    
    # ===== .r / .rr / .rrr - RAID =====
    if cmd in ["r", "rr", "rrr"]:
        if raid_active.get(chat_id, False):
            await event.reply("❌ Raid already active! Pehle `.s` se stop karein!")
            return
        
        target_id, target_user = await resolve_target(event, args)
        if not target_id:
            await event.reply("❌ Usage: `.r @username`")
            return
        if target_id == OWNER_ID or target_id in SUDO_USERS:
            await event.reply("🛡️ Cannot raid owner/sudo!")
            return
        
        speed = 1.5 if cmd == "r" else (0.6 if cmd == "rr" else 0.25)
        raid_speed = speed
        mention = get_mention(target_user or await bot.get_entity(target_id))
        
        await event.reply(f"╔══════════════════════╗\n  ⚔️ **RAID STARTED** ⚔️\n╚══════════════════════╝\n\n🎯 {mention}\n⚡ `{speed}s`\n📜 `{len(raid_lines)}`\n\n🔥 Raid chal raha hai...")
        
        raid_active[chat_id] = True
        try:
            while raid_active.get(chat_id, False):
                for line in raid_lines:
                    if not raid_active.get(chat_id, False): break
                    final = line.replace("${USER}", mention) if "${USER}" in line else f"{mention} {line}"
                    try: await bot.send_message(chat_id, final)
                    except: pass
                    await asyncio.sleep(speed)
        except: pass
        raid_active[chat_id] = False
        return
    
    # ===== .s - RAID STOP =====
    if cmd == "s":
        if not raid_active.get(chat_id, False):
            await event.reply("❌ Koi raid active nahi hai!")
            return
        raid_active[chat_id] = False
        await event.reply(f"╔══════════════════════╗\n  🛑 **RAID STOPPED** 🛑\n╚══════════════════════╝\n\n✅ Raid stop ho gayi!")
        return
    
    # ===== .addline =====
    if cmd == "addline":
        if not args:
            await event.reply("❌ Usage: `.addline Teri maa ki chut`")
            return
        line = " ".join(args)
        raid_lines.append(line)
        write_json("raid_lines.json", raid_lines)
        await event.reply(f"✅ **Raid Line Added!**\n📊 Total: `{len(raid_lines)}`")
        return
    
    # ===== .lines =====
    if cmd == "lines":
        text = ""
        for i, line in enumerate(raid_lines[:15], 1):
            display = line[:60] + "..." if len(line) > 60 else line
            text += f"`{i}.` {display}\n"
        if len(raid_lines) > 15: text += f"\n...aur `{len(raid_lines)-15}` lines"
        await event.reply(f"📜 **RAID LINES ({len(raid_lines)})**\n\n{text}")
        return
    
    # ===== .mute =====
    if cmd == "mute":
        target_id, target_user = await resolve_target(event, args)
        if not target_id:
            await event.reply("❌ Usage: `.mute @username`")
            return
        if target_id == OWNER_ID or target_id in SUDO_USERS:
            await event.reply("🛡️ Cannot mute owner/sudo!")
            return
        cid = str(chat_id)
        if cid not in muted_users: muted_users[cid] = []
        if target_id not in muted_users[cid]:
            muted_users[cid].append(target_id)
            write_json("muted_users.json", muted_users)
            mention = get_mention(target_user or await bot.get_entity(target_id))
            await event.reply(f"╔══════════════════════╗\n  🔇 **USER MUTED** 🔇\n╚══════════════════════╝\n\n👤 {mention}\n🆔 `{target_id}`\n\n🔇 Ab ye msg nahi kar payega!")
        else:
            await event.reply("❌ Pehle se muted hai!")
        return
    
    # ===== .unmute =====
    if cmd == "unmute":
        target_id, _ = await resolve_target(event, args)
        if not target_id:
            await event.reply("❌ Usage: `.unmute @username`")
            return
        cid = str(chat_id)
        if cid in muted_users and target_id in muted_users[cid]:
            muted_users[cid].remove(target_id)
            if not muted_users[cid]: del muted_users[cid]
            write_json("muted_users.json", muted_users)
            await event.reply(f"✅ **User UNMUTED!**")
        else:
            await event.reply("❌ Yeh user muted nahi hai!")
        return
    
    # ===== .mutedlist =====
    if cmd == "mutedlist":
        cid = str(chat_id)
        if cid in muted_users and muted_users[cid]:
            text = "🔇 **MUTED USERS**\n\n"
            for uid in muted_users[cid]:
                try:
                    u = await bot.get_entity(uid)
                    text += f"• {get_mention(u)} - `{uid}`\n"
                except: text += f"• `{uid}`\n"
            await event.reply(text)
        else:
            await event.reply("✅ Koi muted user nahi!")
        return
    
    # ===== .shayari =====
    if cmd == "shayari":
        if not args:
            types_text = "\n".join([f"• `{t}` — {len(v)} lines" for t,v in shayari_data.items()])
            await event.reply(f"📖 **SHAYARI HUB**\n\n{types_text}\n\nAdd: `.shayari [type] [line]`\nSend: `.shayari [type] @user [count]`\nTypes: love, sad, roast, romantic, attitude, abuse, funny")
            return
        stype = args[0].lower()
        if stype not in shayari_data: shayari_data[stype] = []
        if len(args) >= 2:
            if args[1].startswith("@"):
                try:
                    _, target_user = await resolve_target(event, [args[1]])
                    u = target_user or await bot.get_entity(args[1])
                    mention = get_mention(u)
                    count = 1
                    if len(args) >= 3 and args[2].isdigit():
                        count = min(int(args[2]), 20)
                    if not shayari_data[stype]:
                        await event.reply(f"❌ `{stype}` mein koi shayari nahi!")
                        return
                    await event.reply(f"⏳ {mention} ko `{count}` shayari...")
                    for _ in range(count):
                        line = random.choice(shayari_data[stype])
                        final = line.replace("${USER}", mention) if "${USER}" in line else f"{mention} {line}"
                        try: await bot.send_message(chat_id, final)
                        except: pass
                        await asyncio.sleep(0.5)
                    await event.reply(f"✅ Done!")
                except Exception as e:
                    await event.reply(f"❌ Error: {e}")
            else:
                line = " ".join(args[1:])
                if "${USER}" not in line: line = "${USER} " + line
                shayari_data[stype].append(line)
                write_json("shayari.json", shayari_data)
                await event.reply(f"✅ Added to `{stype}`! Total: `{len(shayari_data[stype])}`")
        else:
            await event.reply(f"❌ Usage: `.shayari {stype} @user [count]` ya `.shayari {stype} [line]`")
        return
    
    if cmd == "shayaritypes":
        types_text = "\n".join([f"• `{t}` — {len(v)} lines" for t,v in shayari_data.items()])
        await event.reply(f"📖 **SHAYARI TYPES**\n\n{types_text}")
        return
    
    # ===== .addsticker =====
    if cmd == "addsticker":
        if not event.is_reply:
            await event.reply("❌ Kisi sticker pe reply karo!")
            return
        reply = await event.get_reply_message()
        if not reply.sticker:
            await event.reply("❌ Reply sticker pe karo!")
            return
        sid = reply.sticker.id
        if sid not in sticker_data["saved"]:
            sticker_data["saved"].append(sid)
            write_json("stickers.json", sticker_data)
        await event.reply(f"✅ Sticker added! Total: `{len(sticker_data['saved'])}`")
        return
    
    # ===== .sticker =====
    if cmd == "sticker":
        if not args:
            await event.reply("❌ Usage: `.sticker @user [count]`")
            return
        if not sticker_data["saved"]:
            await event.reply("❌ Koi sticker nahi!")
            return
        try:
            _, target_user = await resolve_target(event, [args[0]])
            u = target_user or await bot.get_entity(args[0])
            mention = get_mention(u)
            count = 1
            if len(args) >= 2 and args[1].isdigit():
                count = min(int(args[1]), 10)
            await event.reply(f"⏳ {count} sticker...")
            for _ in range(count):
                sid = random.choice(sticker_data["saved"])
                try: await bot.send_message(chat_id, f"{mention} 🖼️", file=sid)
                except: pass
                await asyncio.sleep(0.3)
            await event.reply(f"✅ Done!")
        except Exception as e:
            await event.reply(f"❌ Error: {e}")
        return
    
    # ===== .broadcast =====
    if cmd == "broadcast":
        if not args:
            await event.reply("❌ Usage: `.broadcast [msg]`")
            return
        bmsg = " ".join(args)
        update_groups_sync()
        status = await event.reply("📢 Broadcasting...")
        count = 0
        for gid in GROUPS_CACHE:
            try:
                await bot.send_message(gid, f"📢 **BROADCAST**\n\n{bmsg}")
                count += 1
                await asyncio.sleep(0.3)
            except: pass
        await status.edit(f"✅ `{count}/{len(GROUPS_CACHE)}` groups mein bhej diya!")
        return
    
    # ===== .tagbroadcast =====
    if cmd == "tagbroadcast":
        if len(args) < 2:
            await event.reply("❌ Usage: `.tagbroadcast @user [msg]`")
            return
        try:
            _, target_user = await resolve_target(event, [args[0]])
            u = target_user or await bot.get_entity(args[0])
            mention = get_mention(u)
            bmsg = " ".join(args[1:])
            update_groups_sync()
            status = await event.reply("📢 Broadcasting...")
            count = 0
            for gid in GROUPS_CACHE:
                try:
                    await bot.send_message(gid, f"{mention}\n\n📢 {bmsg}")
                    count += 1
                except: pass
            await status.edit(f"✅ `{count}/{len(GROUPS_CACHE)}` groups!")
        except Exception as e:
            await event.reply(f"❌ Error: {e}")
        return
    
    # ===== .chatbox =====
    if cmd == "chatbox":
        if not args:
            await event.reply("❌ Usage: `.chatbox [msg]` ya `.chatbox @user [msg]`")
            return
        if args[0].startswith("@"):
            try:
                _, target_user = await resolve_target(event, [args[0]])
                u = target_user or await bot.get_entity(args[0])
                mention = get_mention(u)
                bmsg = " ".join(args[1:]) if len(args) >= 2 else ""
                if not bmsg:
                    await event.reply("❌ Kuch likho!")
                    return
                update_groups_sync()
                count = 0
                for gid in GROUPS_CACHE:
                    try:
                        await bot.send_message(gid, f"{mention}\n\n📢 {bmsg}")
                        count += 1
                    except: pass
                await event.reply(f"✅ `{count}` groups!")
            except Exception as e:
                await event.reply(f"❌ Error: {e}")
        else:
            bmsg = " ".join(args)
            update_groups_sync()
            count = 0
            for gid in GROUPS_CACHE:
                try:
                    await bot.send_message(gid, f"📢 {bmsg}")
                    count += 1
                except: pass
            await event.reply(f"✅ `{count}` groups!")
        return
    
    # ===== .hack =====
    if cmd == "hack":
        if not args:
            await event.reply("❌ Usage: `.hack @username`")
            return
        try:
            _, target_user = await resolve_target(event, [args[0]])
            u = target_user or await bot.get_entity(args[0])
            mention = get_mention(u)
            m = await event.reply(f"🖥️ **HACKING {mention}**")
            await asyncio.sleep(1.5); await m.edit("📡 Connecting...")
            await asyncio.sleep(1.5); await m.edit("🔓 Bypassing encryption...")
            await asyncio.sleep(1.5); await m.edit("📊 Extracting data...")
            await asyncio.sleep(1)
            await m.edit(f"✅ **HACKED!**\n👤 {mention}\n🆔 `{u.id}`\n\n😈 **Just kidding! Safe hai!** 🛡️")
        except Exception as e:
            await event.reply(f"❌ Error: {e}")
        return
    
    # ===== .spam =====
    if cmd == "spam":
        if len(args) < 2:
            await event.reply("❌ Usage: `.spam [count] [msg]`")
            return
        count = int(args[0]) if args[0].isdigit() else 1
        smsg = " ".join(args[1:])
        if count > 50: count = 50
        await event.reply(f"⏳ Spamming `{count}` times...")
        for _ in range(count):
            try: await bot.send_message(chat_id, smsg)
            except: pass
            await asyncio.sleep(0.2)
        await event.reply(f"✅ Done!")
        return
    
    # ===== .quote =====
    if cmd == "quote":
        quotes = [
            "Zindagi mein do cheezein kabhi mat bhoolna: Apni family aur apne enemies. 😎",
            "Insaan woh nahi hota jo sochta hai, insaan woh hota hai jo karta hai. 🔥",
            "Girna allowed hai, bas uthna zaroori hai. ⚡",
            "Kamyabi ka raasta asaan nahi hota. 🏆",
        ]
        await event.reply(f"💬 **QUOTE**\n\n{random.choice(quotes)}")
        return
    
    # ===== .calc =====
    if cmd == "calc":
        if not args:
            await event.reply("❌ Usage: `.calc 2+2`")
            return
        expr = "".join(args)
        allowed = set("0123456789+-*/.()%")
        if any(c not in allowed for c in expr):
            await event.reply("❌ Sirf numbers aur operators!")
            return
        try:
            result = eval(expr)
            await event.reply(f"🧮 `{expr}` = `{result}`")
        except Exception as e:
            await event.reply(f"❌ {e}")
        return
    
    # ===== .joke =====
    if cmd == "joke":
        jokes = [
            "Teacher: Beta tumhari shaadi ho gayi? Student: Nahi sir! 😂",
            "Papa: Beta exam mein kitne number aaye? Beta: 100 mein se 100 GALAT! 🤣",
        ]
        await event.reply(f"😂 {random.choice(jokes)}")
        return
    
    # ===== .gc =====
    if cmd == "gc":
        update_groups_sync()
        text = f"📦 **TOTAL GROUPS:** `{len(GROUPS_CACHE)}`\n\n"
        for i, gid in enumerate(GROUPS_CACHE[:20], 1):
            try:
                chat = await bot.get_entity(gid)
                text += f"`{i}.` {chat.title[:30]}\n"
            except: text += f"`{i}.` `{gid}`\n"
        if len(GROUPS_CACHE) > 20: text += f"\n...aur `{len(GROUPS_CACHE)-20}` groups"
        await event.reply(text)
        return
    
    # ===== .restart =====
    if cmd == "restart":
        if user_id != OWNER_ID:
            await event.reply("❌ Sirf owner!")
            return
        await event.reply("🔄 **BOT RESTARTING...**")
        os._exit(0)
    
    # ===== .truth =====
    if cmd == "truth":
        truths = ["Apni crush ka naam batao? 💕", "Kabhi jhooth bola? 🤥", "Sabse embarrassing moment? 😅"]
        await event.reply(f"🎯 **TRUTH**\n\n{random.choice(truths)}")
        return
    
    # ===== .dare =====
    if cmd == "dare":
        dares = ["Apni DP 5 min ke liye badlo 😂", "Kisi random number pe call karo 📞", "1 min breath rok ke rakho 🫁"]
        await event.reply(f"🔥 **DARE**\n\n{random.choice(dares)}")
        return
    
    # ===== .botstats =====
    if cmd == "botstats":
        update_groups_sync()
        total_muted = sum(len(v) for v in muted_users.values())
        raid_status = "🟢 Active" if any(raid_active.values()) else "🔴 Inactive"
        await event.reply(
            f"📊 **BOT STATISTICS**\n\n"
            f"🤖 **Status:** {'🟢 ONLINE' if bot_status == 'online' else '🔴 OFFLINE'}\n"
            f"👑 **Owner:** `{OWNER_ID}`\n"
            f"🔑 **Sudo:** `{len(SUDO_USERS)}`\n"
            f"📦 **Groups:** `{len(GROUPS_CACHE)}`\n"
            f"📜 **Lines:** `{len(raid_lines)}`\n"
            f"⚔️ **Raid:** {raid_status}\n"
            f"🔇 **Muted:** `{total_muted}`\n"
            f"🖼️ **Stickers:** `{len(sticker_data.get('saved', []))}`\n"
            f"📖 **Shayari:** `{len(shayari_data)}` types\n"
            f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        return
    
    # ===== .forward =====
    if cmd == "forward":
        if not event.is_reply:
            await event.reply("❌ Kisi msg pe reply karo!")
            return
        if not args:
            await event.reply("❌ Usage: `.forward @username`")
            return
        try:
            reply = await event.get_reply_message()
            target = args[0]
            if target.startswith("@"): dest = await bot.get_entity(target)
            else: dest = await bot.get_entity(int(target))
            await bot.forward_messages(dest.id, reply.id, chat_id)
            await event.reply(f"✅ Forwarded!")
        except Exception as e:
            await event.reply(f"❌ Error: {e}")
        return
    
    # ===== .setphoto =====
    if cmd == "setphoto":
        if user_id != OWNER_ID:
            await event.reply("❌ Sirf owner!")
            return
        if not args:
            await event.reply("❌ Usage: `.setphoto [url]`")
            return
        settings["photo_url"] = args[0]
        write_json("settings.json", settings)
        await event.reply(f"✅ Photo updated!")
        return
    
    if cmd == "delallraid":
        if user_id != OWNER_ID:
            await event.reply("❌ Sirf owner!")
            return
        raid_lines.clear()
        write_json("raid_lines.json", raid_lines)
        await event.reply("🗑️ **All lines deleted!**")
        return

# =====================================================================
# 💀 UNAUTHORIZED PUNISHMENT
# =====================================================================
async def punish_unauthorized(event):
    user = await event.get_sender()
    mention = get_mention(user)
    lines = [
        f"TERI MAKI CHUT {mention} RANDI ITACHI PAPA BOL KE THODI AUKAT BANA LE 😋🥵",
        f"MADARCHOD {mention} TERI AUKAAT NAHI HAI BOT USE KARNE KI 🍆💦",
        f"{mention} RANDI KI AULAD BOT KA USE KARE GA TERI MAKI CHUT ME TALWAR GHUSAAUNGA 🔥",
        f"BHOSDIKE {mention} TERI BEHEN KI CHUT ME BOT DAAL DUNGA 🖕",
        f"{mention} CHUTIYE TERA BAAP BHI NAHI HAI TERA 🤡",
        f"TERI MAKI CHUT {mention} MADARCHOD PEHLE SUDO LE PHIR AA 💀",
    ]
    for i in range(random.randint(4, 6)):
        try:
            await event.reply(random.choice(lines))
            await asyncio.sleep(0.8)
        except: pass

# =====================================================================
# 🔄 CALLBACK HANDLER
# =====================================================================
@bot.on(events.CallbackQuery)
async def callback_handler(event):
    data = event.data.decode()
    
    if data == "owner":
        try:
            owner = await bot.get_entity(OWNER_ID)
            mention = get_mention(owner)
        except: mention = f"`{OWNER_ID}`"
        await event.edit(f"👑 **BOT OWNER**\n\n🆔 `{OWNER_ID}`\n👤 {mention}\n🔑 Sudo: `{len(SUDO_USERS)}`\n📡 {'🟢 ONLINE' if bot_status == 'online' else '🔴 OFFLINE'}", buttons=[[Button.inline("⬅️ Back", data="main")]])
    
    elif data == "cmd_list":
        await event.edit(
            "📋 **FULL COMMAND LIST**\n\n"
            "🔰 **BASIC**\n`.alive` | `.off` | `.ping` | `.speed` | `.id` | `.info`\n\n"
            "⚔️ **RAID**\n`.r @user` (1.5s) | `.rr @user` (0.6s) | `.rrr @user` (0.25s)\n`.s` stop | `.addline` | `.lines`\n\n"
            "🔇 **MUTE**\n`.mute @user` | `.unmute @user` | `.mutedlist`\n\n"
            "📖 **SHAYARI**\n`.shayari` | `.shayari [type] @user [count]`\n\n"
            "🖼️ **STICKERS**\n`.addsticker` (reply) | `.sticker @user [count]`\n\n"
            "📢 **BROADCAST**\n`.broadcast [msg]` | `.tagbroadcast @user [msg]` | `.chatbox [msg]`\n\n"
            "🔐 **SUDO**\n`.sudo @user` | `.remsudo @user` | `.sudolist`\n\n"
            "🎮 **EXTRA**\n`.hack` | `.spam` | `.quote` | `.calc` | `.joke` | `.truth` | `.dare`\n`.botstats` | `.gc` | `.forward` | `.setphoto` | `.restart`",
            buttons=[[Button.inline("⬅️ Back", data="main")]])
    
    elif data == "main":
        me = await bot.get_me()
        btns = [
            [Button.inline("👤 MY OWNER", data="owner")],
            [Button.inline("📋 FULL COMMAND LIST", data="cmd_list")],
            [Button.url("➕ ADD ME YOUR GROUP", f"https://t.me/{me.username}?startgroup=true")],
            [Button.inline("💬 CHAT BOX", data="chatbox_menu"), Button.inline("📢 BROADCAST", data="bc_menu")],
        ]
        await event.edit(f"🔥 **ULTIMATE PRO MAX BOT**\n\n⚡ {'🟢 ONLINE' if bot_status == 'online' else '🔴 OFFLINE'}\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", buttons=btns)
    
    elif data == "chatbox_menu":
        await event.edit("💬 **CHAT BOX**\n`.chatbox [msg]` - Sab groups mein\n`.chatbox @user [msg]` - Tag + all", buttons=[[Button.inline("⬅️ Back", data="main")]])
    
    elif data == "bc_menu":
        await event.edit("📢 **BROADCAST**\n`.broadcast [msg]` - Sab groups\n`.tagbroadcast @user [msg]` - Tag + all", buttons=[[Button.inline("⬅️ Back", data="main")]])

# =====================================================================
# 📦 AUTO GROUP TRACK WHEN ADDED
# =====================================================================
@bot.on(events.ChatAction)
async def chat_action(event):
    if event.user_added:
        me = await bot.get_me()
        for u in event.users:
            if u.id == me.id:
                cid = event.chat_id
                if cid not in GROUPS_CACHE:
                    GROUPS_CACHE.append(cid)
                    save_groups()
                await event.reply(f"╔══════════════════════╗\n  🔥 **BOT ADDED** 🔥\n╚══════════════════════╝\n\n✅ Thanks!\n👑 Owner: `{OWNER_ID}`\n📋 /menu | 🚀 `.alive`")

# =====================================================================
# 🚀 START
# =====================================================================
async def main():
    me = await bot.get_me()
    print(f"""
╔══════════════════════════════╗
   🔥 BOT STARTED 🔥
╚══════════════════════════════╝
  🤖 Bot: @{me.username}
  👑 Owner: {OWNER_ID}
  📦 Groups: {len(GROUPS_CACHE)}
  ✅ BOT IS ONLINE!
""")

if __name__ == "__main__":
    bot.loop.run_until_complete(main())
    bot.run_until_disconnected()
