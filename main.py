from telegram import (
    }
}

# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🛍 Shop", callback_data="shop")],
        [InlineKeyboardButton("💰 Add Money", callback_data="money")],
        [InlineKeyboardButton("📦 My Orders", callback_data="orders")],
        [InlineKeyboardButton("📞 Support", callback_data="support")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "🔥 Welcome to Flassy Mods Store 🔥\n\n"
        "✅ Manual Delivery\n"
        "✅ 24/7 Support\n"
        "✅ bKash / Nagad / Rocket Payment"
    )

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

# ---------------- BUTTONS ----------------
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # ---------------- SHOP ----------------
    if data == "shop":

        keyboard = []

        for product in products:
            keyboard.append([
                InlineKeyboardButton(
                    product,
                    callback_data=f"product_{product}"
                )
            ])

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text(
            "🛒 Select a product:",
            reply_markup=reply_markup
        )

    # ---------------- PRODUCT ----------------
    elif data.startswith("product_"):

        product_name = data.replace("product_", "")

        plans = products[product_name]

        text = f"🔥 {product_name}\n\n"

        for plan, price in plans.items():
            text += f"✅ {plan} = ৳{price}\n"

        text += (
            "\n💳 Payment Methods:\n"
            "• bKash\n"
            "• Nagad\n"
            "• Rocket\n\n"
            "📩 Contact Admin After Payment"
        )

        await query.message.reply_text(text)

    # ---------------- MONEY ----------------
    elif data == "money":

        text = (
            "💰 Add Balance\n\n"
            "Send payment screenshot to admin.\n\n"
            "💳 Payment Methods:\n"
            "• bKash\n"
            "• Nagad\n"
            "• Rocket"
        )

        await query.message.reply_text(text)

    # ---------------- ORDERS ----------------
    elif data == "orders":

        await query.message.reply_text(
            "📦 No orders found."
        )

    # ---------------- SUPPORT ----------------
    elif data == "support":

        await query.message.reply_text(
            "📞 Contact Admin: @yourusername"
        )

# ---------------- RUN BOT ----------------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("Bot Running...")
app.run_polling()
