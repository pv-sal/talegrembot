from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Replace with your real bot token
BOT_TOKEN = "8494274304:AAF72-4J7pQX4qFNu-azUsOlqezMK22mQFQ"

# Function to handle new members
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        user_id = member.id
        await update.message.reply_text(
            f"🙏🏻 សូមស្វាគមន៍ {member.first_name}! អរគុណសម្រាប់ការចូលរួមក្នុង buildflow group 🎉\n🆔 Your ID: `{user_id}`",
            parse_mode="Markdown"
        )

# Main function to start the bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Add a handler for new chat members
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
