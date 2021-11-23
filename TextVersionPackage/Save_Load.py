from Player import Player
import os
#import hashlib

save_folder = os.getcwd() + "\\..\\UrsinaEngine\\Saves\\"
save_files = os.listdir(save_folder)


def save(inp):
    money = inp[1]
    pc_tier = inp[2]
    #TODO: encrypt/decrypt save
    with open(save_folder+inp[0], 'w') as sv:
        sv.write(str(inp[1]))
        sv.write("\n")
        sv.write(str(inp[2]))


def load(is_new=True):
    #TODO: cls
    #os.system("cls")
    if is_new:
        Sanya = Player()
        save(Sanya.play_game())
    else:
        print("Plz choose save file")
        for i in range(len(save_files)):
            print(str(i+1)+") "+save_files[i])
        while True:
            #TODO: Lowercase
            print("print:", end=" ")
            command = input()
            try:
                if command in save_files:
                    loadfile = command
                    break
                elif len(save_files) >= int(command) > 0:
                    loadfile = save_files[int(command)-1]
                    break
                else:
                    print("Wrong input")
            except ValueError:
                print("plz input number or name of savefile u want load")
        load_file(save_folder+loadfile, loadfile)

#TODO: name save files
def load_file(file_loc, file_name):
    with open(file_loc, 'r') as file:
        money = int(file.readline())
        pc_tier = int(file.readline())
    #TODO: Send save file name
    Sanya = Player(money=money, pc_tier=pc_tier)
    save(Sanya.play_game())
