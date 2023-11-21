import asyncio
import time


async def call():

    print('начался звонок')
    await asyncio.sleep(5)
    print('звонок закончился')

async def prin_pos():
    print('посетитель пришел')
    await asyncio.sleep(2)
    print('посетитель ушел')

async def grafiks():
    print('начало бронирования')
    await asyncio.sleep(2)
    print('')

async def aeroticket():
    print('выбор авиабилетов')
    await asyncio.sleep(2)
    print('покупка авиабилетов')

async def documents():
    print('начало заполнения')
    await asyncio.sleep(5)
    print('документы заполнены')

async def main():
    task_call = asyncio.create_task(call())
    task_prin_pos = asyncio.create_task(prin_pos())

    print('9:00')
    await prin_pos()
    print('10:00')
    work = asyncio.gather(task_call, task_prin_pos)
    print('11:00')
    await call()
    print('12:00')
    await grafiks()
    print('13:00')
    await asyncio.gather(task_call, task_prin_pos)

asyncio.run(main())
