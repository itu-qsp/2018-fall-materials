def mysterious_function(data_list):
    for passnum in range(len(data_list) - 1, 0, -1):
        for idx in range(passnum):
            if data_list[idx] > data_list[idx + 1]:
                temp = data_list[idx]
                data_list[idx] = data_list[idx + 1]
                data_list[idx + 1] = temp


if __name__ == '__main__':
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mysterious_function(data)
    print(data)