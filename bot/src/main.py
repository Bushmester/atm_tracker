from aiogram import executor

from dialogs import register_dialogs
from handlers import register_handlers
from initialization import dp, registry


def main():
    register_dialogs(registry)
    register_handlers(dp)
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
