import console_gfx

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

def main():
    print("Welcome to the RLE image encoder!")
    print("\nDisplaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    print()
    file_data = []
    while True:
        print("\nRLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image")
        print("3. Read RLE String\n4. Read RLE Hex String\n5. Read Data Hex String")
        print("6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data")
        option = int(input("\nSelect a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            fileName = str(input("Enter name of file to load: "))
            file_data = console_gfx.load_file(fileName)
        elif option == 2:
            file_data = console_gfx.test_image
            print("Test image data loaded.")
        elif option == 3:
            rle_string = str(input("Enter an RLE string to be decoded: "))
            file_data = decode_rle(string_to_rle(rle_string))
        elif option == 4:
            hex_rle_string = str(input("Enter the hex string holding RLE data: "))
            file_data = decode_rle(string_to_data(hex_rle_string))
        elif option == 5:
            hex_string = str(input("Enter the hex string holding flat data: "))
            file_data = string_to_data(hex_string)
        elif option == 6:
            print("Displaying image...")
            print("(no data)") if len(file_data) == 0 else console_gfx.display_image(file_data)
        elif option == 7:
            if len(file_data) == 0:
                print(f"RLE representation: (no data)")
            else:
                print(f"RLE representation: {to_rle_string(encode_rle(file_data))}")
        elif option == 8:
            if len(file_data) == 0:
                print(f"RLE hex values: (no data)")
            else:
                print(f"RLE hex values: {to_hex_string(encode_rle(file_data))}")
        elif option == 9:
            if len(file_data) == 0:
                print(f"Flat hex values: (no data)")
            else:
                print(f"Flat hex values: {to_hex_string(file_data)}")
        else:
            print("Error! Invalid input.")
