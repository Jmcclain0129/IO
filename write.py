# reads lines of text in file named

# f = open('newfile.txt', 'r')
# f.write("Hello\n")
# f.close()

# appends "ADDS" word to same line of text in file named
# f = open('newfile.txt', 'a')
# f.write("Hello")
# f.close()

# appends "ADDS" word to new line of text in file named (must delete text file and run write.py again to create new file to see this effect
# f = open('newfile.txt', 'a')
# f.write("Hello\n")
# f.close()

f = open('newfile.txt', 'a')
lines = ['Hello','World','Welcome','To','File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()