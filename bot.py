import discord
import random
import Tictactoe
from cleverbot import Cleverbot

cleverbot_client = Cleverbot()
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
			yield from client.send_message(message.channel, "Um. Wu")
		elif msg.content == "wu":
			while True:
				yield from client.send_message(message.channel, "Yo. Wu")
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
		yield from client.send_message(message.channel, "I choose {0}".format(choices[num]))

	if message.content.startswith('#kierannudes'):
		yield from client.send_file(message.channel, "C://bananabot//kieran.jpg", filename = "kieran.jpg", content = "I don't have nudes but I have...")

	if message.content.startswith('#shutdown'):
		yield from client.send_message(message.channel, "Shutting down...")
		yield from client.logout()

	if message.content.startswith('#tictactoe'):
		t = Tictactoe.Tictactoe()
		yield from client.send_message(message.channel, t)
		while True:
			message = yield from client.wait_for_message()
			if message.content.startswith('#killttc'):
				yield from client.send_message(message.channel, "Tictactoe game is dead.")
				return
			if message.content.startswith('#naught'):
				coord = message.content.strip("#naught ")
				row = int(coord[2])
				column = int(coord[0])
				yield from client.send_message(message.channel, t.naught(column,row))
				yield from client.send_message(message.channel, t.check())
			elif message.content.startswith('#cross'):
				coord = message.content[len('#cross'):].strip()
				row = int(coord[2])
				column = int(coord[0])
				yield from client.send_message(message.channel, t.cross(column,row))
				yield from client.send_message(message.channel, t.check())
			if t.win != 0:
				return

	if message.content.startswith('#bb'):
		question = message.content.strip('#bb ')
		answer = cleverbot_client.ask(question)
		yield from client.send_message(message.channel, answer)

	if "harambe" in message.content.lower():
		yield from client.send_message(message.channel, "RIP")

	if "banana" in message.content.lower():
		yield from client.send_message(message.channel, ":Banana:")

	if message.content.startswith("#psr"):
		msg = message.content.strip("psr# ")
		psr = [":fist:", ":v:", ":raised_hand:"]
		num = random.randint(0,2)
		ans = psr[num]
		if num - 1 == -1:
			win = psr[2]
		else:
			win = psr[num - 1]
		if num + 1 == 3:
			lose = psr[0]
		else:
			lose = psr[num + 1]
		yield from client.send_message(message.channel, ans)
		if ans in msg:
			yield from client.send_message(message.channel, "It's a draw!")
			return
		elif win in msg:
			yield from client.send_message(message.channel, "You win!")
			return
		elif lose in msg:
			yield from client.send_message(message.channel, "You lose!")
			return


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run("MjIwNDk4NDgwMDk3OTE4OTg2.Cql3kw.aTquvKfAbubAnz97Dc8rfukqO68")