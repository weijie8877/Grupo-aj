import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("TOKEN not found in Railway Variables")

CHANNEL_URL = "https://t.me/lily_grupo_aj"
INSTAGRAM_URL = "https://www.instagram.com/lily__gerente"
SUPPORT_URL = "https://vue.livehelp100service.com/03ddbf9d379cab2jkfle-kelid2bd983091ae237dc6ecf19c4463c6b4b98ff9f1fda5365b7b73424b20baef28"
WEBSITE_URL = "https://www.ajgrupo.com"


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🤝 CANAL Cooperar", url=CHANNEL_URL)],
        [InlineKeyboardButton("📷 INSTAGRAM", url=INSTAGRAM_URL)],
        [InlineKeyboardButton("💬 SUPPORT", url=SUPPORT_URL)],
        [InlineKeyboardButton("🌐 WEBSITE", url=WEBSITE_URL)],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 *Bem-vindo ao Bot Oficial Lily Gerente!*\n\n"
        "Escolha uma opção abaixo:",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


async def canal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🤝 ABRIR CANAL", url=CHANNEL_URL)]]

    await update.message.reply_text(
        "📢 *Canal Oficial Lily Gerente*\n\n"
        "Clique no botão abaixo para acessar:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📷 ABRIR INSTAGRAM", url=INSTAGRAM_URL)]]

    await update.message.reply_text(
        "📷 *Instagram Lily Gerente*\n\n"
        "Clique no botão abaixo para acessar:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💬 FALAR COM SUPORTE", url=SUPPORT_URL)]]

    await update.message.reply_text(
        "💬 *Suporte Lily Gerente*\n\n"
        "Clique abaixo para falar com nosso suporte:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🌐 ABRIR WEBSITE", url=WEBSITE_URL)]]

    await update.message.reply_text(
        "🌐 *Website*\n\n"
        "Clique no botão abaixo para acessar:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("canal", canal))
    app.add_handler(CommandHandler("instagram", instagram))
    app.add_handler(CommandHandler("support", support))
    app.add_handler(CommandHandler("website", website))

    print("✅ Lily Gerente Bot Online")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
