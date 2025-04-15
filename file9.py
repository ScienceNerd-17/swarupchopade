
f = open("demo.txt", "w")
f.write("Hello World.\nThis is a demo file.")
f.close()
s= open("demo.txt", "r")
c = s.read()
s.close()
d = open("demo 1.txt", "w")
d.write(c)
d.close()
print("File copied successfully!")



file_name = input("Enter the file name: ")
file = open(file_name, "w")
file.write("Hello World ..This is a demo file.")
file.close()
source = open(file_name, "r")
content = source.read()
source.close()


 
word_count = len(content.split())
print(f"Word count: {word_count}")



print("\nFile content in uppercase:")
print(content.upper())



char_count = len(content)
print(f"Character count: {char_count}")



search_word = input("\nEnter the word to count occurrences: ")
word_occurrence = content.lower().split().count(search_word.lower())
print(f"The word '{search_word}' occurs {word_occurrence} times in the file.")



