import asyncio
import time

def sync_function(test_parm: str) -> str:
    print("This is sync func")

    time.sleep(0.1)

    return f"sync result: {test_parm}"

#co-routine function

async def async_function(test_parm: str) -> str:
    print("This is async coroutine func")

    await asyncio.sleep(0.1)

    return f"sync result: {test_parm}"


async def main():
    # sync_result = sync_function("Test")
    # print(sync_result)
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    print(f"Empty Future: {future}")
   
    future.set_result("Future Result: Test")
    future_result = await future
    print(future_result)


if __name__ == "__main__":
    asyncio.run(main())