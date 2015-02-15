import glob

def training_data():
    file_list = glob.glob("games/*.*")
    game_list = []
    input_value = { ".": 0, "o": 1, "x": 2 }
    output_value_x = { 'x': 1, '.': 0, 'o': 0 }
    output_value_o = { 'o': 1, '.': 0, 'x': 0 }

    for file_name in file_list:
        file = open(file_name, "r")
        data = file.read().split("\n")
        game_list += data[1:-1]

    inputs = []
    outputs = []
    for index, game in enumerate(game_list):
        if index % 2 == 0:
            inputs.append([input_value[cell] for cell in list(game)])
        else:
            outputs.append([output_value_x[cell] for cell in list(game)] + [output_value_o[cell] for cell in list(game)])
            
    return (inputs, outputs)

print training_data()
