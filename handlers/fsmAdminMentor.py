from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINS
from . import keyboards


class FSMAdmin(StatesGroup):
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMAdmin.name.set()
        await message.answer("Имя ментора?", reply_markup=keyboards.cancel_markup)
    else:
        await message.answer("Пишите пожалуйста в личку")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Какое направление?', reply_markup=keyboards.direction_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Возраст ментора?')


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Укажите возраст в числах!")
    elif not 15 < int(message.text) < 65:
        await message.answer("Значения не подпадают в возрастную группу")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer('Ментор какой группы?')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(data['group'])
        await message.answer(f"{data['name']} {data['direction']} {data['age']} {data['group']}")

    await FSMAdmin.next()
    await message.answer('Данные верны?', reply_markup=keyboards.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        # TODO: Запись в БД
        await state.finish()
        await message.answer("Данные записаны!")
    elif message.text.lower() == ("редактировать"):
        await FSMAdmin.name.set()
        await message.answer("Имя ментора?")
    else:
        await message.answer("OK")


async def cancel_form(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Выход")


def register_handlers_fsmAdminMentor(dp: Dispatcher):
    dp.register_message_handler(cancel_form, state='*', commands=['cancel'])
    dp.register_message_handler(
        cancel_form,
        Text(equals='отмена', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, Text(equals='Регистрация', ignore_case=True))
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
