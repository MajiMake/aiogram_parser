from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_parser.telegram.lexicons import LEXICON_RU

router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU.start)

@router.message(F.text.lower().in_(LEXICON_RU.include_lexicon))
async def tests_ability(message: Message):
    await message.answer(text="фыв")
