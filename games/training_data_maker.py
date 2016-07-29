import glob

input_representation = { 'o': 1, 'x': 2, '.': 0 }
output_representation_for_o = { 'o': 1, 'x': 0, '.': 0 }
output_representation_for_x = { 'o': 0, 'x': 1, '.': 0 }

file_list = glob.glob('game*')

inputs = open('inputs', 'w+')
outputs = open('outputs', 'w+')

for file_name in file_list:
    print 'file: ', file_name

    game = open(file_name).read()

    # Removes the first move as we want to reverse 'x' and 'o'
    # 'o' learns from 'x' movements against 'o' movements

    moves = game.strip().split('\n')[1:]
    if len(moves) % 2 == 1:
        moves = moves[:-1]

    for player_move, opponent_move in zip(moves[0::2], moves[1::2]):
        input_data = [input_representation[x] for x in player_move]
        inputs.write(','.join(str(x) for x in input_data) + '\n')

        output_data = [output_representation_for_o[x] for x in opponent_move] + [output_representation_for_x[x] for x in opponent_move]
        outputs.write(','.join(str(x) for x in output_data) + '\n')

inputs.close()
outputs.close()

print "Wrote input data to: inputs"
print "Wrote output data to: outputs"
