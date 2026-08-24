import asyncio

async def main():
    await asyncio.sleep(3.5)
    print("Hello")
    
asyncio.run(main() , debug=True)