file_name = "dsdfsd.ee"


def check_file_type(file):
    types = [".jpg", ".png"]
    return any(x for x in types if x in file)


print(check_file_type(file_name))
