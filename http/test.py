import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://www.example.com")
        print(response.text[:200])
        
    

asyncio.run(main())