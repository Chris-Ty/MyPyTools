import os 


def encrypt(ori_dir, new_dir):
    # 首先读目标文件
    results = []
    with open(ori_dir, encoding='utf-8') as rf:
        for line in rf.readlines():  # 读取每行
            for a_char in line:  # 读取每个字符
                # print(line)
                sec = bin(ord(a_char))  # 先将str转为ord数字，再将数字转为bin二进制
                # print(sec)
                results.append(sec)
    # 输出到新的文件
    with open(new_dir, 'w') as wf:
        wf.writelines(results)


def decrypt(ori_dir, new_dir):
    # 首先读目标文件
    with open(ori_dir, 'r') as rf:
        b_contents = rf.readlines()

    # 处理
    bi_str = ''.join(b_contents).split('0b')
    bi_str_drop_null = []
    for c in bi_str:
        if c is not '':
            bi_str_drop_null.append(c)
    restores = []
    for word_b2 in bi_str_drop_null:
        restores.append(chr(int(word_b2, base=2)))

    # 写入
    with open(new_dir, 'w') as wf:
        wf.writelines(''.join(restores))


target_dir = r'yourfile's dir'
generate_dir = r'the file you want to generate and its dir'
# encrypt(target_dir, generate_dir)


generate_dir = r'your 0b file's dir'
restore_dir = r'restore file dir'
# decrypt(generate_dir, restore_dir)
