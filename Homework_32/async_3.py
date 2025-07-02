import asyncio


async def sender(future):
    print("Sender: doing work...")
    future.set_result("message from sender!")


async def receiver(future):
    print("Receiver: waiting for message...")
    message = await future
    print("Receiver got:", message)


async def main():
    future = asyncio.Future()
    await asyncio.gather(
        receiver(future),
        sender(future),
    )


asyncio.run(main())
