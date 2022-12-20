file_name = "dsdfsd.fff"

def check_file_type(file):
    types = [".jpg", ".png"]
    for type in types:
        if type in file:
            return True
        else: return False

print(check_file_type(file_name))