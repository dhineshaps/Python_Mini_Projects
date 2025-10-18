import asyncio

#to run multiple co-routine concunrrently
# one of the problem is if 1 fails other won't stop

async def fetch_data(id, sleep_time):
    print("fetching data....id", id)
    await asyncio.sleep(sleep_time)
    print(f"completed {id}")
    return {"id":id, "data":f"sample data from coroutine {id}"}

async def main():
     results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))

     for result in results:
          print(f"Received result: {result}")

asyncio.run(main())