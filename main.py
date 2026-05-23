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

import os

TOKEN = os.getenv("TOKEN")


# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

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
            InlineKeyboardButton("🎁 Daily Reward", callback_data="daily")
        ],
        [
            InlineKeyboardButton("ℹ️ Help", callback_data="help")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🔥 Welcome To Hari Bhai Services 🔥

━━━━━━━━━━━━━━━━━━
🤖 MULTI FEATURE BOT
━━━━━━━━━━━━━━━━━━

🎨 AI Image Generator
📈 Social Tools
💰 Earning System
🎮 Mini Game
🎁 Daily Rewards
👑 Premium Access

━━━━━━━━━━━━━━━━━━
🚀 Fast • Smart • Powerful
━━━━━━━━━━━━━━━━━━

Choose option below 👇
"""

    await update.message.reply_text(text, reply_markup=reply_markup)


# ---------------- BUTTON HANDLER ----------------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data


    # ---------------- IMAGE ----------------
    if data == "image":
        await query.message.reply_text(
            "🎨 Send any prompt\n\nExample:\ncyberpunk city, neon lights"
        )


    # ---------------- FOLLOWERS ----------------
    elif data == "followers":
        await query.message.reply_text(
            "📈 Followers Service\n\n🔥 Instagram\n🔥 YouTube\n🔥 Telegram\n\n⚡ Coming Soon"
        )


    # ---------------- EARNING ----------------
    elif data == "earning":
        await query.message.reply_text(
            "💰 Earning System\n\n"
            "🎯 Refer & Earn\n"
            "📌 Daily Tasks\n"
            "🎁 Rewards\n\n"
            "🚀 Coming Soon"
        )


    # ---------------- PREMIUM ----------------
    elif data == "premium":
        await query.message.reply_text(
            "👑 Premium Features\n\n"
            "⚡ Unlimited Images\n"
            "⚡ Faster Speed\n"
            "⚡ VIP Support\n\n"
            "🔥 Coming Soon"
        )


    # ---------------- HELP ----------------
    elif data == "help":
        await query.message.reply_text(
            "ℹ️ Help\n\n"
            "👉 Send text for AI image\n"
            "👉 Use buttons for features\n\n"
            "Example: sunset on mountains"
        )


    # ---------------- DAILY REWARD ----------------
    elif data == "daily":

        coins = context.user_data.get("coins", 0)
        reward = random.randint(10, 50)

        coins += reward
        context.user_data["coins"] = coins

        await query.message.reply_text(
            f"🎁 Daily Reward Claimed!\n\n💰 +{reward} coins\n🪙 Total: {coins}"
        )


    # ---------------- GAME ----------------
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
            "🎮 Guess Number (1-5)",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ---------------- GAME GUESS ----------------
    elif data.startswith("g_"):

        guess = int(data.split("_")[1])
        correct = context.user_data.get("game")

        if correct is None:
            await query.message.reply_text("⚠️ Game restart karo /start se")
            return

        if guess == correct:
            msg = "🎉 Correct! You Win 🔥"
        else:
            msg = f"❌ Wrong! Correct was {correct}"

        await query.message.reply_text(msg)


# ---------------- IMAGE GENERATOR ----------------
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )

    await update.message.reply_text("🧠 Processing prompt...")

    image_url = f"https://image.pollinations.ai/prompt/{text}"

    await update.message.reply_photo(photo=image_url)


# ---------------- MAIN APP ----------------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("🔥 Bot Running Successfully...")

app.run_polling()
