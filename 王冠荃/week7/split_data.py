import random

def split(data_path):
    with open(data_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    data = lines[1:]
    random.shuffle(data)
    train_data = data[:int(len(data) * 0.8)]
    test_data = data[int(len(data) * 0.8):]
    with open('train_data.txt', 'w', encoding='utf8') as f_train:
        f_train.writelines(train_data)

    with open('valid_data.txt', 'w', encoding='utf8') as f_valid:
        f_valid.writelines(train_data)


if __name__ == "__main__":
    split("../文本分类练习数据集/文本分类练习.csv")