# طلب اختيار المستخدم
print("Hello! Choose what you want to do:")
print("1- Convert from binary text to plain text")
print("2 - Convert from plain text to binary text")

choice = input("Enter the number (1 or 2):")

if choice == '1':
    # تحويل من ثنائي إلى نص
    bytes_list = input("Enter النص الثنائي (ضع مسافة بين كل بايت): ")
    text_output = ''.join(chr(int(byte, 2)) for byte in bytes_list)
    print("Plain text:", text_output)

elif choice == '2':
    # تحويل من نص إلى ثنائي
    normal_text = input("Enter the text you want to convert to binary:")
    binary_output = ' '.join(format(ord(char), '08b') for char in normal_text)
    print("binary text:", binary_output)

else:
    print("Invalid selection .Please enter 1 or 2.")
