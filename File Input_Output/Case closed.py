with open("text.txt", "r+") as my_file:
    my_file.write("Hello There")
    
    if my_file.closed is False:
        my_file.close()
        
    print my_file.closed