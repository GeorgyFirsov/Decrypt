from Generate.Generate import generate_dataset


file_path = './data/words_list.txt'

if __name__ == "__main__":
    dataset = generate_dataset(file_path)
