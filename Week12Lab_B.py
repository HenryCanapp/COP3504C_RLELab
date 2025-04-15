def to_hex_string(data):
    output = ''
    for i in data:
        output += '%x' % i
    return output

def count_runs(flat_data):
    output = 1
    current_run = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] != flat_data[i-1] or current_run >= 16:
            output += 1
            current_run = 1
        else:
            current_run += 1
    return output

def encode_rle(flat_data):
    output = [1, flat_data[0]]
    run_index = 0
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i-1] and output[run_index * 2] < 16:
            output[run_index * 2] += 1
        else:
            run_index += 1
            output.append(1)
            output.append(flat_data[i])
    return output

def get_decoded_length(rle_data):
    output = 0
    for i in range(0,len(rle_data)//2):
        output += rle_data[i * 2]
    return output

def decode_rle(rle_data):
    output = []
    for i in range(0, len(rle_data)//2):
        for j in range(0, rle_data[i * 2]):
            output.append(rle_data[i * 2 + 1])
    return output

def string_to_data(data_string):
    output = []
    for char in data_string:
        output.append(int(char, 16))
    return output