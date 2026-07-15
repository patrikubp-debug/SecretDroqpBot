import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

ADMIN_ID = 5257042796

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        "سلام 👋\nبه ربات چت ناشناس خوش آمدید."
    )

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text(
            "پنل مدیریت فعال است ✅"
        )
    else:
        await update.message.reply_text(
            "دسترسی ندارید."
        )

def main():
    TOKEN = os.getenv("BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))

    app.run_polling()

if __name__ == "__main__":
    main()
