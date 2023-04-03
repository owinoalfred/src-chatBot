import discord
import responses 
import main


async def send_message(message, user_message, is_private): 
    try:
        responses = responses.handle_responses(user_message)
        await message.author.send(responses) if is_private else await message.channel.send(responses)
    except Exception as e:
        print(e)


def run_disord_bot():
    TOKEN: ' MTA5MjM5ODI3OTM1MTg2OTUyMA.G7-aJP.k9nZB3t86ZYVZrKU2C_2EGnLv4nv1GMJahn2Pc'
    client: discord.Client()

    @client.event

    async def on_ready():
        print(f'{client.user} is now running')

        client.run('https://discord.com/api/oauth2/authorize?client_id=1092398279351869520&permissions=534723950656&scope=bot')
