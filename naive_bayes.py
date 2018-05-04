#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@姓名: 
@学号: 
"""
import pickle as pk
import numpy as np
import sys


def generate_word_dict() -> None :
    """
    生成一个便于查找词频的字典（数据结构自己决定），然后通过pickle储存为.data文件。
    """
    with open("train.data","rb") as f:
        train_data = pk.load(f)  #载入train数据
    pass #请去掉pass，然后填写上你的代码
    
    with open("word_dict.data","rb") as f:
        pk.dump(your_word_dict,f) #参数名可以随意更改，文件名最好不要更改 


def naive_bayes_classifier(text:list(str),word_dict) -> int :
    """
    本函数要求对于输入的文章词袋进行朴素贝叶斯分类，返回这篇文章所属的类别int(0-3)。
    其中参数word_dict是打开的字典文件（通过generate_word_dict生成的）
    """
    pass #请去掉pass，然后填写上你的代码



def test():
    """
    本函数对测试集进行测试。建议不要修改这个函数。
    """
    with open("test.data","rb") as f:
        test_data = pk.load(f) 
    try:
        with open("word_dict.data","rb") as f:
            word_dict = pk.load(f)
    except:
        print("你的字典没有完成或者出了一些问题，请修改！")
        return
    tp = np.zeros(4)
    fp = np.zeros(4)
    try:
        for data in test_data:
            your_ans = naive_bayes_classifier(data[0],word_dict)
            if your_ans == data[1]:
                tp[data[1]] += 1
            else:
                fp[your_ans] += 1
    except :
        print("你的分类器没有完成或者出了一些问题，请修改！")
        return
    p = tp/(tp+fp)
    r = tp/200
    f = 2*p*r/(p+r)
    print("__"*30)
    for i,j in enumerate(['energy','estate','sports','entertainment']):
        print("对于",j,"的分类情况为:")
        print("准确度：",p[i],"  召回率：",r[i],"  F值：",f[i])
    print("__"*30)
    return  
    
if __name__ == "__main__":
    if len(sys.argv) != 1:
        if sys.argv[1] == 'train':
            print('正在生成字典（训练）...')
            try:
                generate_word_dict()
            except:
                print('generate_word_dict函数出了一些bug，请修改！')
            else:
                print('训练完成！')
    else:
        test()