import asyncio


async def fetch_data(delay, id):
    print("fetching data....id", id)
    await asyncio.sleep(delay)
    print("Data Fetched, id", id)
    return {"data":"Some data", "id":id}


async def main():  #co-routine function
    print("start of main coroutine")
    task1 = fetch_data(2,1) #this just build the co routine , won't execute unless await
    task2 = fetch_data(2,2)
    result1 = await task1   # here the execution goes to the function  - only used under async func
    print(f"Received result1: {result1}")
    result2 = await task2
    print(f"Received result2: {result2}")
    print("End of main coroutine")

#main() #when executed like this, it will just build co-routine so it returns the object with warning

asyncio.run(main()) #here it will satrt the event loop