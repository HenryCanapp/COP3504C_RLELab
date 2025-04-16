import Week12Lab_C
import console_gfx

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
        file_data = Week12Lab_C.decode_rle(Week12Lab_C.string_to_rle(rle_string))
    elif option == 4:
        hex_rle_string = str(input("Enter the hex string holding RLE data: "))
        file_data = Week12Lab_C.decode_rle(Week12Lab_C.string_to_data(hex_rle_string))
    elif option == 5:
        hex_string = str(input("Enter the hex string holding flat data: "))
        file_data = Week12Lab_C.string_to_data(hex_string)
    elif option == 6:
        print("Displaying image...")
        print("(no data)") if len(file_data) == 0 else console_gfx.display_image(file_data)
    elif option == 7:
        if len(file_data) == 0:
            print(f"RLE representation: (no data)")
        else:
            print(f"RLE representation: {Week12Lab_C.to_rle_string(Week12Lab_C.encode_rle(file_data))}")
    elif option == 8:
        if len(file_data) == 0:
            print(f"RLE hex values: (no data)")
        else:
            print(f"RLE hex values: {Week12Lab_C.to_hex_string(Week12Lab_C.encode_rle(file_data))}")
    elif option == 9:
        if len(file_data) == 0:
            print(f"Flat hex values: (no data)")
        else:
            print(f"Flat hex values: {Week12Lab_C.to_hex_string(file_data)}")
    else:
        print("Error! Invalid input.")
