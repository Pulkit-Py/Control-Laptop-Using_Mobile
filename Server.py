import time, socket, sys
from chatbot import chatty
import os
import random
import datetime
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 
port = 8080
 
new_socket.bind((host_name, port))
print( "Binding successful!")
print("This is your IP: ", s_ip)
 
name = 'chatty'
 
new_socket.listen(5) 
 
 
conn, add = new_socket.accept()
 
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
 
conn.send(name.encode())
while True:
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
    value = chatty(message)
    if value is not None:
        print("Me : "+ value)
        conn.send(value.encode())
    else:
        query = message.lower()
        if "calculate" in query:
            res = query.split()
            temp = []
            for i in res:
                if i.isdigit() or '+'in i or "*" in i or '-' in i or '/' in i:
                    temp.append(i)
            answer = ''.join(temp) 
            ans = eval(answer)
            print('Me : ', str(ans))
            conn.send(str(ans).encode())
        elif "play music" in query:
            print("Me : Playing songs")
            conn.send("Playing songs...".encode())
            music_dir = "F:\\Playlist"
            songs = os.listdir(music_dir)
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir,song))
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%m:%S")
            print('Me :', str(time))
            conn.send(str(time).encode())
        elif 'stop' in query:
            print("Me : By take care")
            conn.send("By take care".encode())
            break
        elif "say something" in query:
            print("Me: please like the video subsribe Pulkit py.")
            conn.send("please like the video and subsribe Pulkit py".encode())
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1") 
        elif 'restart' in query:
            os.system("shutdown /r /t 1") 
        else:
            print("Me :Sorry i didnt understand :(")
            conn.send("Sorry i didnt understand :(".encode())


       	
