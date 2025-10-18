import asyncio

#here scheduling multiple task to run at the same time if the current task is waiting on the something
async def fetch_data(id, sleep_time):
    print("fetching data....id", id)
    await asyncio.sleep(sleep_time)
    print(f"completed {id}")
    return {"id":id, "data":f"sample data from coroutine {id}"}

async def main():
    task1 = asyncio.create_task(fetch_data(1,15)) #task will goes to next if current task wait on something, program will be efficient
    task2 = asyncio.create_task(fetch_data(2,3))
    task3 = asyncio.create_task(fetch_data(3,1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1,result2,result3)

asyncio.run(main())