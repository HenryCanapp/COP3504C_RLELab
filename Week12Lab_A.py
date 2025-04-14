import console_gfx

print("Welcome to the RLE image encoder!")
print("\nDisplaying Spectrum Image:")
console_gfx.display_image(console_gfx.test_rainbow)
file_data = []
while True:
    print("\n\nRLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image")
    print("3. Read RLE String\n4. Read RLE Hex String\n5. Read Data Hex String")
    print("6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data")
    option = int(input("\nSelect a Menu Option:"))
    if option == 0:
        break
    elif option == 1:
        fileName = str(input("Enter name of file to load: "))
        file_data = console_gfx.load_file(fileName)
    elif option == 2:
        file_data = console_gfx.test_image
    elif option == 6:
        console_gfx.display_image(file_data)