import socket
from _thread import *
import pickle
import random
from settings import *

server = "192.168.0.194"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
food_positions = generate_food(AMOUNT_OF_FOOD)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(NUMBER_OF_PLAYERS)
print("Waiting for a connection, Server Started")


def generate_food(amount: int):
    food_positions = []
    for _ in range(0, amount):
        temp = (random.choice(range(-WIDTH, WIDTH*2)),random.choice(range(-HEIGHT, HEIGHT*2)))
        food_positions.append(temp)
    return food_positions

def threaded_client(conn):
    global food_positions
    conn.send(str.encode(str(conn)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if not data:
                break
            else:
                if data == "get":
                    reply = food_positions

                conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))