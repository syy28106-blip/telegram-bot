from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.constants import ChatAction

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes
)

import random

# ================= TOKEN =================
TOKEN = "8617243274:AAES1fjK92CaQLvCg-CfI8mtqMJVabiG_e8"

# ================= OWNER ID =================
OWNER_ID = 123456789

# ================= QR IMAGE =================
QR_IMAGE = "https://i.postimg.cc/j2HcFQqj/hariscanner.jpg"


# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["ai_mode"] = False

    keyboard = [
        [
            InlineKeyboardButton("🎨 AI Image", callback_data="image"),
            InlineKeyboardButton("📈 Followers", callback_data="followers")
        ],
        [
            InlineKeyboardButton("💰 Earning", callback_data="earning"),
            InlineKeyboardButton("👑 Premium", callback_data="premium")
        ],
        [
            InlineKeyboardButton("🎮 Game", callback_data="game"),
            InlineKeyboardButton("🎁 Reward", callback_data="daily")
        ],
        [
            InlineKeyboardButton("ℹ️ Help", callback_data="help")
        ]
    ]

    text = """
🔥 WELCOME TO HARI BHAI SERVICES 🔥

━━━━━━━━━━━━━━━━━━
🤖 PREMIUM MULTI FEATURE BOT
━━━━━━━━━━━━━━━━━━

🎨 AI Image Generator
📈 Followers Services
💰 Earning System
🎮 Games
🎁 Daily Rewards
👑 VIP Premium

━━━━━━━━━━━━━━━━━━
⚡ FAST • SAFE • NON DROP
━━━━━━━━━━━━━━━━━━

👇 CHOOSE OPTION BELOW
"""

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ================= BUTTON HANDLER =================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data


    # ================= AI IMAGE =================
    if data == "image":

        context.user_data["ai_mode"] = True

        await query.message.reply_text(
            "🎨 SEND YOUR IMAGE PROMPT\n\n"
            "Example:\n"
            "cyberpunk city neon lights"
        )


    # ================= FOLLOWERS =================
    elif data == "followers":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📢 Telegram Services",
                    callback_data="telegram_service"
                ),

                InlineKeyboardButton(
                    "📸 Instagram Services",
                    callback_data="insta_service"
                )
            ]
        ]

        text = """
📈 FOLLOWERS PANEL

━━━━━━━━━━━━━━━━━━
🔥 CHOOSE YOUR SERVICE
━━━━━━━━━━━━━━━━━━

📢 Telegram Subscribers
📸 Instagram Followers

⚡ Fast Delivery
🛡️ Non Drop
"""

        await query.message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ================= TELEGRAM SERVICE =================
    elif data == "telegram_service":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔥 1000 Subs ₹30",
                    callback_data="tg_1000"
                ),

                InlineKeyboardButton(
                    "⚡ 2000 Subs ₹60",
                    callback_data="tg_2000"
                )
            ]
        ]

        text = """
📢 TELEGRAM SUBSCRIBERS

━━━━━━━━━━━━━━━━━━
✅ NON DROP SERVICE
⚡ FAST DELIVERY
🚀 REAL LOOKING MEMBERS
━━━━━━━━━━━━━━━━━━

👇 SELECT PACKAGE
"""

        await query.message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ================= PACKAGE SELECT =================
    elif data == "tg_1000" or data == "tg_2000":

        if data == "tg_1000":
            quantity = "1000"
            price = 30

        else:
            quantity = "2000"
            price = 60

        context.user_data["service"] = "Telegram Subscribers"
        context.user_data["quantity"] = quantity
        context.user_data["price"] = price

        keyboard = [
            [
                InlineKeyboardButton(
                    "🛒 ORDER NOW",
                    callback_data="order_now"
                ),

                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="telegram_service"
                )
            ]
        ]

        text = f"""
🔥 SERVICE SELECTED

━━━━━━━━━━━━━━━━━━
📢 Telegram Subscribers
👥 Quantity : {quantity}
💰 Price : ₹{price}
━━━━━━━━━━━━━━━━━━

🛡️ NON DROP
⚡ FAST DELIVERY

👇 CLICK ORDER NOW
"""

        await query.message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ================= ORDER NOW =================
    elif data == "order_now":

        context.user_data["waiting_link"] = True

        await query.message.reply_text(
            "🛒 SEND YOUR TELEGRAM CHANNEL LINK\n\n"
            "Example:\n"
            "https://t.me/yourchannel"
        )


    # ================= EARNING =================
    elif data == "earning":

        await query.message.reply_text(
            "💰 EARNING SYSTEM COMING SOON 🚀"
        )


    # ================= PREMIUM =================
    elif data == "premium":

        await query.message.reply_text(
            "👑 PREMIUM FEATURES COMING SOON 🚀"
        )


    # ================= HELP =================
    elif data == "help":

        await query.message.reply_text(
            "ℹ️ HELP SECTION\n\n"
            "👉 Use buttons for services\n"
            "👉 AI image works only after clicking AI Image button"
        )


    # ================= DAILY REWARD =================
    elif data == "daily":

        coins = context.user_data.get("coins", 0)

        reward = random.randint(10, 50)

        coins += reward

        context.user_data["coins"] = coins

        await query.message.reply_text(
            f"🎁 DAILY REWARD CLAIMED\n\n"
            f"💰 +{reward} Coins\n"
            f"🪙 Total : {coins}"
        )


    # ================= GAME =================
    elif data == "game":

        number = random.randint(1, 5)

        context.user_data["game"] = number

        keyboard = [
            [
                InlineKeyboardButton("1", callback_data="g_1"),
                InlineKeyboardButton("2", callback_data="g_2"),
                InlineKeyboardButton("3", callback_data="g_3")
            ],
            [
                InlineKeyboardButton("4", callback_data="g_4"),
                InlineKeyboardButton("5", callback_data="g_5")
            ]
        ]

        await query.message.reply_text(
            "🎮 GUESS NUMBER (1-5)",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ================= GAME RESULT =================
    elif data.startswith("g_"):

        guess = int(data.split("_")[1])

        correct = context.user_data.get("game")

        if guess == correct:
            msg = "🎉 CORRECT! YOU WIN 🔥"

        else:
            msg = f"❌ WRONG! CORRECT WAS {correct}"

        await query.message.reply_text(msg)


# ================= MESSAGE HANDLER =================
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text


    # ================= CHANNEL LINK =================
    if context.user_data.get("waiting_link"):

        context.user_data["channel_link"] = text

        context.user_data["waiting_link"] = False

        context.user_data["waiting_payment"] = True

        service = context.user_data.get("service")
        quantity = context.user_data.get("quantity")
        price = context.user_data.get("price")

        caption = f"""
💳 PAYMENT REQUIRED

━━━━━━━━━━━━━━━━━━
📢 SERVICE : {service}
👥 QUANTITY : {quantity}
💰 PRICE : ₹{price}
━━━━━━━━━━━━━━━━━━

✅ SCAN QR & PAY
📸 SEND PAYMENT SCREENSHOT

⚠️ AFTER PAYMENT SEND SS HERE
"""

        await update.message.reply_photo(
            photo=QR_IMAGE,
            caption=caption
        )

        return


    # ================= WAITING PAYMENT =================
    if context.user_data.get("waiting_payment"):

        await update.message.reply_text(
            "⚠️ PLEASE SEND PAYMENT SCREENSHOT IMAGE"
        )

        return


    # ================= AI IMAGE MODE =================
    if context.user_data.get("ai_mode"):

        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action=ChatAction.TYPING
        )

        await update.message.reply_text(
            "🧠 PROCESSING PROMPT..."
        )

        image_url = f"https://image.pollinations.ai/prompt/{text}"

        await update.message.reply_photo(photo=image_url)

        context.user_data["ai_mode"] = False

        return


    # ================= DEFAULT =================
    await update.message.reply_text(
        "⚠️ PLEASE SELECT OPTION FROM MENU"
    )


# ================= PHOTO HANDLER =================
async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.user_data.get("waiting_payment"):
        return

    user = update.effective_user

    service = context.user_data.get("service")
    quantity = context.user_data.get("quantity")
    price = context.user_data.get("price")
    link = context.user_data.get("channel_link")

    photo = update.message.photo[-1].file_id

    # ================= USER SUCCESS =================
    await update.message.reply_text(
        "✅ PAYMENT SCREENSHOT RECEIVED\n\n"
        "🚀 ORDER SUBMITTED SUCCESSFULLY\n"
        "⏳ DELIVERY START SOON"
    )

    # ================= SEND TO OWNER =================
    caption = f"""
🔥 NEW ORDER RECEIVED

━━━━━━━━━━━━━━━━━━
👤 USER : @{user.username}
🆔 ID : {user.id}

📢 SERVICE : {service}
👥 QUANTITY : {quantity}
💰 PRICE : ₹{price}

🔗 CHANNEL :
{link}
━━━━━━━━━━━━━━━━━━
"""

    await context.bot.send_photo(
        chat_id=OWNER_ID,
        photo=photo,
        caption=caption
    )

    context.user_data["waiting_payment"] = False


# ================= MAIN =================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(button))

app.add_handler(
    MessageHandler(
        filters.PHOTO,
        photo_handler
    )
)

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        reply
    )
)

print("🔥 BOT RUNNING SUCCESSFULLY...")

app.run_polling()
