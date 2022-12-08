import asyncio

async def main():
  print('tim')
  task = asyncio.create_task(foo('text')) ## まだ実行されない
  await asyncio.sleep(0.5) ## 待ちになったのでタスクfooを実行
  print('finished')

async def foo(text):
  print(text)
  await asyncio.sleep(10) ## 待ちになったので再びmainに戻る

asyncio.run(main())

# tim
# text
# finished
# [finished in 0.8s]
