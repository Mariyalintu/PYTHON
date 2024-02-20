import os
def find_string_in_file(file_path, search_string):
   
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if search_string.lower() in line.lower():
                print(f"Found '{search_string}' in {file_path} at line {line_number}:")
                print(line.strip())  
file_path = 'E:\\Idle\\sample.txt'  
search_string = 'is'  

find_string_in_file(file_path, search_string)





                                    
                                                                      
