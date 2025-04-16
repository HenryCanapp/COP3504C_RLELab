

#translates data to hexadecimal string
def to_hex_string(data):
    output = ''
    for i in data:
        output += '%x' % i
    return output

#counts the number of runs in raw data
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

#turns raw data into RLE data
def encode_rle(flat_data):
    output = [1, flat_data[0]]
    run_index = 0
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i-1] and output[run_index * 2] < 15:
            output[run_index * 2] += 1
        else:
            run_index += 1
            output.append(1)
            output.append(flat_data[i])
    return output

#returns the decompressed size of RLE data
def get_decoded_length(rle_data):
    output = 0
    for i in range(0,len(rle_data)//2):
        output += rle_data[i * 2]
    return output

#turns RLE data into raw data
def decode_rle(rle_data):
    output = []
    for i in range(0, len(rle_data)//2):
        for j in range(0, rle_data[i * 2]):
            output.append(rle_data[i * 2 + 1])
    return output

#turns a hex string into data (array)
def string_to_data(data_string):
    output = []
    for char in data_string:
        output.append(int(char, 16))
    return output

#Turns RLE data into a human-readable string
def to_rle_string(rle_data):
    output = ''
    for i in range(len(rle_data)//2):
        if i != 0: output += ':'
        output += str(rle_data[i * 2])
        output += '%x' % rle_data[i * 2 + 1]
    return output

#turns a human-readable string into RLE data (array)
def string_to_rle(rle_string : str):
    hex_string = ""
    for i in rle_string.split(":"):
        if len(i) > 2:
            hex_string += '%x' % int(i[:2])
            hex_string += i[-1]
        else:
            hex_string += '%x' % int(i[0])
            hex_string += '%x' % int(i[1])
    return string_to_data(hex_string)
