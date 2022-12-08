import asyncio

async def fetch():
  print('start fetching')
  await asyncio.sleep(2)
  print('done fetching')
  return {'data': 1}

async def print_numbers():
  for i in range(10):
    print(i)
    await asyncio.sleep(0.25)

async def main():
  # task1 = asyncio.create_task(fetch())
  await fetch()
  task2 = asyncio.create_task(print_numbers())

  # value =  await task1
  # print(value)
  await task2

asyncio.run(main())

"""
start fetching
done fetching
0
1
2
3
4
5
6
7
8
9
"""
