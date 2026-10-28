
import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salam, brat! 🚆 ADY bilet bildiriş botu işləyir."
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot aktivdir. Bilet izləmə funksiyasını növbəti mərhələdə qoşacağıq."
    )

def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN təyin edilməyib")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.run_polling()
  async def izle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚆 Tbilisi → Bakı bilet izləmə siyahısı\n\n"
        "📅 1 noyabr 2026\n"
        "📅 2 noyabr 2026\n"
        "📅 3 noyabr 2026\n\n"
        "⏱️ Planlaşdırılan yoxlama: 15 dəqiqədən bir\n"
        "⚠️ Avtomatik bilet yoxlaması hələ qoşulmayıb."
    )      
if __name__ == "__main__":
    main()
