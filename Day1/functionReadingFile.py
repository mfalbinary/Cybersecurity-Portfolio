def  readingfile (myfile,verbose=False) :
     try:
         with open(myfile,'r')as file :
            counter=0
            content=[]
            for line in file:
             counter+=1
             content.append(line)
             if verbose:
                print(line.strip())
         return f"[✔]File '{myfile}' has {counter} lines."    
     except FileNotFoundError:
        print("File not found")   
     return f"[!] File not found"