from justgoodapi.coro import imjustgood
import asyncio

api = imjustgood('YOUR_APIKEY_HERE')

async def main():
    # return await api.apikeyStatus("CHECK_ANOTHER_APIKEY") -> You can check another apikey here
    return await api.apikeyStatus() # -> Check your apikey status

print(asyncio.run(main())) # Get the result