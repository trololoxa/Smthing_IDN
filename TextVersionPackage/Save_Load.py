from Player import Player
import os
import json
# import hashlib

save_folder = os.getenv('APPDATA') + "\\..\\Kinda Hacker Game\\Saves\\"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
save_files = os.listdir(save_folder)


# TODO: Test Json save & load
def save(inp):
    money = inp[1]
    pc_tier = inp[2]
    # TODO: encrypt/decrypt save
    with open(save_folder + inp[0], 'w') as json_file:
        data = {'save': [{'savelen': 2, 'money': inp[1], 'pc_tier': inp[2]}]}
        json.dump(data, json_file)


def load(is_new=True):
    # TODO: cls
    # os.system("cls")
    if is_new:
        Sanya = Player()
        save(Sanya.play_game())
    else:
        print("Plz choose save file")
        for i in range(len(save_files)):
            print(str(i + 1) + ") " + save_files[i])
        while True:
            # TODO: Lowercase
            print("print:", end=" ")
            command = input()
            try:
                if command in save_files:
                    loadfile = command
                    break
                elif len(save_files) >= int(command) > 0:
                    loadfile = save_files[int(command) - 1]
                    break
                else:
                    print("Wrong input")
            except ValueError:
                print("plz input number or name of savefile u want load")
        load_file(save_folder + loadfile, loadfile)


# TODO: name save files
def load_file(file_loc, file_name):
    try:
        with open(file_loc, 'r') as file:
            ld = json.load(file)
            savedata = ld['save'][0]
            if savedata['savelen'] != 2:
                print('Old save file format')
                exit(-1)
            money = savedata['money']
            pc_tier = savedata['pc_tier']
    except KeyError:
        print('Incorrect save file format1')
        raise exit(-1)
    except json.decoder.JSONDecodeError:
        print('Incorrect save file format2')
        raise exit(-1)
    # TODO: Send save file name
    Sanya = Player(money=money, pc_tier=pc_tier)
    save(Sanya.play_game())
