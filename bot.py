import discord
import responses 
import main


async def send_message(message, user_message, is_private): 
    try:
        responses = responses.handle_responses(user_message)
        await message.author.send(responses) if is_private else await message.channel.send(responses)