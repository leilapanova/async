# import asyncio
# import time
#
#
# async def async_func(num):
#     print(f'...start {num}')
#     await asyncio.sleep(3)
#     print(f'..end {num}')
#
#
# async def main():
#     taskA = asyncio.create_task(async_func('A'))
#     taskB = asyncio.create_task(async_func('B'))
#     taskC = asyncio.create_task(async_func('C'))
#     await asyncio.wait([taskA, taskB, taskC])
#
# if __name__ == '__main__':
#     asyncio.run(main())

# def mulply(a, b):
#     return a * b

import asyncio
import time


async def count(counter):
    print(f'колво записей в списке{len(counter)}')
    while True:
        await asyncio.sleep(1/1000)
        counter.append(1)

async def print_every_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'прошла 1с. Элементов в списке {len(counter)}')

async def print_every_5sec():
    while True:
        await asyncio.sleep(5)
        print(f'прошлo 5сек')

async def print_every_10sec():
    while True:
        await asyncio.sleep(10)
        print(f'прошлo 10сек')

#
# async def main():
#     counter = list()
#     count(counter)
# async def main():
#     counter = []
#
#     task1 = asyncio.create_task(count(counter))
#     task2 = asyncio.create_task(print_every_sec(counter))
#     task3 = asyncio.create_task(print_every_5sec())
#     task4 = asyncio.create_task(print_every_10sec())
#
#     await task1
#     await task2
#     await task3
#     await task4
#
# asyncio.run(main())

# import time
#
#
# async def makeCofee():
#     print('start makeCofee')
#     await asyncio.sleep(3)
#     print('end makeCofee')
#
#
# async def toastBrew():
#     print('start toastBrew')
#     await asyncio.sleep(2)
#     print('end toastBrew')
#     return  'toast is ready'
#
# async def main():
#     start = time.time()
#     await asyncio.gather(makeCofee(), toastBrew())
#     res_cofee, res_toast = await work
#     end = time.time()
#     print(res_cofee)
#     print(res_toast)
#     print(f'времени прошло {end-start:.2f} минут')
#
# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
#
# async
#     print('sleep start')
#
#
# async def my_work():
#     print('work stsrt')
#     await asyncio.sleep(5)
#     print('work end')
#
# async  def main():
#     task1 = asyncio.create_task(my_sleep())
#     task2 = asyncio.create_task(my_work())
#     print('rest end')

# import asyncio
# import httpx
# async def dowload(current):
#     url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail"
#
#     async with httpx.AsyncClient() as client:
#         result = await client.get(url)
#         if result.status_code == 200:
#             my_res = result.json()
#             print(my_res['drinks'], current)
#
#         else:
#             print(result.status_code)
#         print(f'результат {current}')
#
# def print_info(info, current):
#     # print(f' имя {info["first_name"]}, фамилия {info["last_name"]}, Email: {info["email"]}')
#     print(info[current]['strDrink'])
#
# async def main():
#     users_count = int(input('сколько? '))
#
#     current = 0
#     task_list = []
#     while current < users_count:
#
#         current += 1
#         task = asyncio.create_task(dowload(current))
#         task_list.append(task)
#         await task
#     await asyncio.gather(*task_list)
#
#     print('Done')
#
# asyncio.run(main())

