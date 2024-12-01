def read_to_string(file):
    f = open(file)
    result = f.readline()
    f.close()

    return result
