import asyncio

#to run multiple co-routine concunrrently
# has error handling , if one failes others will be cancelled

async def fetch_data(id, sleep_time):
    print("fetching data....id", id)
    await asyncio.sleep(sleep_time)
    print(f"completed {id}")
    return {"id":id, "data":f"sample data from coroutine {id}"}

async def main():
    tasks = []
    
    async with asyncio.TaskGroup() as tg:   #asyncorous contex manager
        for i, sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            print("completed the task ",i)
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())