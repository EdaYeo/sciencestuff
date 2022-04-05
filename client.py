# client
import socket
s = socket.socket()
s.connect(("127.0.0.1", 12345))
def menu():
    print("Menu: \n1) Guess a letter \n2) Guess a word\n3) Quit")
game_over = False
msg = s.recv(1024).decode()
current_word_guessed = int(msg[6:8])*"?"
print("Current word guessed: " + current_word_guessed)
while not game_over:
    menu()
    choice = int(input("What do you want to do?: "))
    if choice == 1:
        letter = input("Guess a letter: ")
        msg = "GUESS," + letter + "\n"
        s.sendall(msg.encode())
    elif choice == 2:
        msg = "HWORD," + input("Guess a word: ") + "\n"
        s.sendall(msg.encode())
    elif choice == 3:
        msg = "QUIT\n"
        s.sendall(msg.encode())
    else:
        print("Please key in a valid option from 1-3")

    recv_msg = s.recv(1024).decode()
    if recv_msg == "WIN\n":
        print("Player wins!")
        game_over = True
        break
    if recv_msg == "QUIT\n":
        print("Player quits.")
        game_over = True
        break
    else:
        for i in range(len(current_word_guessed)):
            if i in list(int(recv_msg[6:-2].strip(","))):
                current_word_guessed[i] = letter
        print(current_word_guessed)
    
    
    
        
    

s.close()
