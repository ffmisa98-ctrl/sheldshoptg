from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8568437699:AAG6P6sJKmXiFddbeznOFcv0uekYLJn_K2A"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

PRODUCTS = {
    "📦 Товар 1": "Цена: 500₽\nОписание товара 1",
    "📦 Товар 2": "Цена: 1000₽\nОписание товара 2"
}

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for p in PRODUCTS:
        kb.add(p)
    await message.answer(
        "👋 Добро пожаловать в магазин!\nВыбери товар:",
        reply_markup=kb
    )

@dp.message_handler(lambda m: m.text in PRODUCTS)
async def product(message: types.Message):
    await message.answer(
        PRODUCTS[message.text] +
        "\n\n💳 Оплата: перевод на Сбер\n📞 После оплаты напиши 'Оплатил'"
    )

@dp.message_handler(lambda m: "оплатил" in m.text.lower())
async def paid(message: types.Message):
    await message.answer(
        "✅ Оплата принята!\nСкоро с тобой свяжутся."
    )

if __name__ == "__main__":
    executor.start_polling(dp)