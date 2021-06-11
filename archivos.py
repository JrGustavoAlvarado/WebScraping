def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers) 
    
           
def write():
     names = ["Lionel", "Haland", "Gustavo", "Hectór"]
     with open("./archivos/numbers.txt","a", encoding="utf-8") as f:
          for name in names:
              f.write(name)
              f.write("\n")
 
     
    
if __name__ == '__main__':
    write()