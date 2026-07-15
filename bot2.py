import os
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


ADMIN_ID = 5257042796


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")


def run_server():
    server = HTTPServer(("0.0.0.0", 10000), Handler)
    server.serve_forever()


def main():
    TOKEN = os.getenv("BOT_TOKEN")

    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    Thread(target=run_server, daemon=True).start()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))

    app.run_polling()


if __name__ == "__main__":
    main()
