from aiogram import executor

from handlers import register_handlers
from initialization import dp


def main():
    register_handlers(dp)
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
