import os
from aiogram import Bot, types


async def get_photo(msg: types.Message, bot: Bot, image_dir: str) -> str:
    photo = msg.photo[-1]  # берем последнее изображение, т.к. оно имеет наибольшее разрешение
    file_info = await bot.get_file(photo.file_id)

    # определяем название файла и путь сохранения
    image_filename = f"{msg.from_user.id}_{msg.date}.jpg"  # создаем уникальное название файла
    image_path = os.path.join(image_dir, image_filename)

    # скачиваем и сохраняем изображение
    await bot.download_file(file_info.file_path, image_path)

    return image_filename