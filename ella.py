'''
描述
如果一个单词通过循环右移获得的单词，我们称这些单词都为一种循环单词。 现在给出一个单词集合，需要统计这个集合中有多少种不同的循环单词。

输入 : dict = ["picture", "turepic", "icturep", "word", "ordw", "lint"]
输出 : 3
说明 : 
"picture", "turepic", "icturep" 是相同的旋转单词。
"word", "ordw" 也相同。
"lint" 是第三个不同于前两个的单词。
'''
from copy import copy

# 先做成全局的
input_data = ["picture", "turepic", "icturep", "word", "ordw", "lint"]
input_data = ["pipip", "ipipp", "icturep", "word", "ordw", "lint"]
input_data = ["pipippppp", "ipipppppp", "picture", "turepic", "icturep", "word", "ordw", "lint"]
input_data = ["pipippppp", "ipipppppp", "pippppppi", "ippppppip", "ppppppipi", "picture", "turepic", "icturep", "word", "ordw", "lint"]




def shift_string(input_str):
    input_str = list(input_str)
    last_letter = input_str.pop()
    new_str = []
    new_str.append(last_letter)
    new_str.extend(input_str)
    return ''.join(new_str)


def run():
    '''
    output_dict = {
        "picture": 3,
        "word": 2,
        "lint": 1
    }

    每次输入字符串，字符串自己朝一个方向shift，每shift一次，和output_dict key 里对比一次
    字符串长度是几，就shift几次
    '''

    output_dict = {}
    # import pdb; pdb.set_trace()
    for input_str in input_data:
        str_length = len(input_str)
        output_keys = list(output_dict.keys())
        # 初始化 is_exist 代表在不在已知 output_dict key 里
        is_exist = False
        input_str_copy = copy(input_str)
        for i in range(str_length):
            # shift str_length times
            shifted_str = shift_string(input_str_copy)
            input_str_copy = shifted_str
            # print(shifted_str)
            if shifted_str in output_keys:
                is_exist = True
                current_count = output_dict[shifted_str]
                output_dict[shifted_str] = current_count + 1
                break
        # 走到这儿说明这个string 不在 output_dict 里
        if not is_exist:
            output_dict[input_str] = 1
    return output_dict



if __name__ == '__main__':
    output_dict = run()
    print(output_dict)
    print('答案是{}.'.format(len(output_dict)))


