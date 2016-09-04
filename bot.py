import discord
import random

client = discord.Client()

@client.async_event
def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('#test'):
		yield from client.send_message(message.channel, "This is a fucking test")

	if message.content.startswith('#frank'):
		yield from client.send_message(message.channel, "Hey I'm Frank. Would you like to know my opinion?")
		opinions = ["Hey, I agree with your opinion.", "I'm fucking triggered!", "Hey, your opinion's stupid"]
		msg = yield from client.wait_for_message(timeout = 10, author = message.author)
		if msg is None:
			yield from client.send_message(message.channel, "Wow... I really wanted to share my opinion")
			return
		if msg.content == "yes":
			num = random.randint(0,2)
			yield from client.send_message(message.channel, opinions[num])
		elif msg.content == "no":
			yield from client.send_message(message.channel, "Umm...Wu")
		elif msg.content == "wu":
			while True:
				yield from client.send_message(message.channel, "Yo...Wu")
				msg = yield from client.wait_for_message(timeout = 10, author = message.author,content = "wu") 
				if msg is None:
					yield from client.send_message(message.channel, "Wu!")
					return

	if message.content.startswith('#choose '):
		msg = message.content[len('#choose'):].strip()
		if msg == "":
			yield from client.send_message(message.channel, "Give me some choices man!")
			return
		choices = msg.split(",")
		xs = len(choices)
		if xs == 1:
			yield from client.send_message(message.channel, "You only gave me one choice, cunt.")
			return
		num = random.randint(0,xs)
		yield from client.send_message(message.channel, choices[num])

	if message.content.startswith('#kierannudes'):
		yield from client.send_file(message.channel, "C://bananabot//kieran.jpg", filename = "kieran.jpg", content = "I don't have nudes but I have...")

	if message.content.startswith('#shutdown'):
		yield from client.send_message(message.channel, "Shutting down...")
		yield from client.logout()

	if message.content.startswith("#psr "):
		msg = message.content[len('#psr '):].strip()
		psr = [":fist:", ":v:", ":raised_hand:"]
		num = random.randint(0,2)
		if num - 1 == -1:
			win = 2
		else:
			win = num - 1
		if num + 1 == 3:
			lose = 0
		else:
			lose = num +1
		yield from client.send_message(message.channel, psr[num])
		if msg == psr[num]:
			yield from client.send_message(message.channel, "It's a draw!")
			return
		elif msg == psr[win]:
			yield from client.send_message(message.channel, "You win!")
			return
		elif msg == psr[lose]:
			yield from client.send_message(message.channel, "You lose!")
			return


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run("MjIwNDk4NDgwMDk3OTE4OTg2.Cql3kw.aTquvKfAbubAnz97Dc8rfukqO68")