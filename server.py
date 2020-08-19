import socket
from _thread import *
import pickle
import random
from settings import *




def generate_food(amount: int):
    food_positions = []
    for _ in range(0, amount):
        temp = (random.choice(range(-WIDTH, WIDTH*2)),random.choice(range(-HEIGHT, HEIGHT*2)))
        food_positions.append(temp)
    return food_positions


server = "192.168.0.194"
port = 5555
players = {}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
food_positions = generate_food(AMOUNT_OF_FOOD)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(NUMBER_OF_PLAYERS)
print("Waiting for a connection, Server Started")




def threaded_client(conn, game_id):
    global food_positions, players
    conn.send(pickle.dumps(game_id))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048*4))
            if not data:
                break
            else:
                if data["action"] == "get":
                    print("get")
                    reply = food_positions
                if data["action"] == "append":
                    players[game_id] = data["data"]
                    reply =  [players[i] for i in range(len(players))]
                if data["action"] == "update":
                    print("update")
                    food_positions = data["data"]
                    reply = food_positions

                conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    del players[game_id]
    conn.close()

currentGame = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentGame))
    currentGame += 1