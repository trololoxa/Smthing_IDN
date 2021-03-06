from MainVersion.Player import Player
import os
import json
# import hashlib

player = Player()
save_folder = os.getenv('APPDATA') + "\\Kinda Hacker Game\\Saves\\"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
save_files = os.listdir(save_folder)


# TODO: Gimme name
def save(inp):
    # TODO: encrypt/decrypt save
    with open(save_folder + inp[0], 'w') as json_file:
        data = {'save': [{'money': inp[1], 'pc_tier': inp[2], 'hunger': inp[3], 'game_time': inp[4], 'cheerfulness': inp[5]}]}
        json.dump(data, json_file)


def load(is_new=True, choose_file=''):
    if not is_new:
        load_file(save_folder, choose_file)


# TODO: name save files
def load_file(file_loc, file_name):
    try:
        with open(file_loc + file_name, 'r') as file:
            ld = json.load(file)
            savedata = ld['save'][0]
            if len(savedata) != 5:
                print('Old save file format')
                exit(-1)
            money = savedata['money']
            pc_tier = savedata['pc_tier']
            hunger = savedata['hunger']
            game_time = savedata['game_time']
            cheerfulness = savedata['cheerfulness']
    except KeyError:
        print('Incorrect save file format')
        raise exit(-1)
    except json.decoder.JSONDecodeError:
        print('Incorrect save file format')
        raise exit(-1)
    # TODO: Send save file name
    player.__init__(file_name=file_name, money=money, pc_tier=pc_tier, hunger=hunger, game_time=game_time, cheerfulness=cheerfulness)