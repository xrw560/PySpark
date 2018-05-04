#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@author: zhouning
@file:bayes_1.py
@time:2018/5/4 23:27
"""
import re, collections


# 把语料中的单词全部抽取出来，转成小写，并且去除单词中间的特殊符号
def words(text): return re.findall('[a-z]+', text.lower())


def train(features):
    """
        要是遇到我们从来没有见过的新词怎么办。假如说一个词拼写完全正确，但是语料中没有包含这个词，从而这个词也永远不会出现在训练集中。于是，我们就要返回出现这个词的概率是0。这个情况不太妙，因为概率为0这个代表了这个事件绝对不可能发生，而在我们的概率模型中，我们期望一个很小的概率来代表这种情况lambda: 1
    """
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model


NWORDS = train(words(open('big.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

"""
编辑距离 ：两个词之间的编辑距离定义为使用了几次插入(在词中插入一个单字母)，删除(删除一个单字母)，交换(交换相邻两个字母)，替换(把一个字母替换成另一个)的操作从一个词变到另一个词
"""


def edits1(word):
    """
    返回所有与单词w编辑距离为1的集合
    """
    n = len(word)
    return set([word[0:i] + word[i + 1:] for i in range(n)]  # deletion
               + [word[0:i] + word[i + 1] + word[i + 2:] for i in range(n - 1)]  # transposition
               + [word[0:i] + c + word[i + 1:] for i in range(n) for c in alphabet]  # alteration
               + [word[0:i] + c + word[i:] for i in range(n + 1) for c in alphabet]  # insertion
               )


def known_edits2(word):
    """
    返回所有与单词w编辑距离为2的集合
    在这些编辑距离小于2的词中间，只把那些正确的词作为候选词
    """
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)


def known(words):
    return set(w for w in words if w in NWORDS)


"""
正常来说把一个元音拼成另一个的概率要大于辅音(因为人常常把hello打成hallo这样)；把单词的第一个字母拼错的概率会相对小，等等。
但是为了简单起见，选择了一个简单的方法：编辑距离为1的正确单词比编辑距离为2的优先级高，而编辑距离为0的正确单词优先级比编辑距离为1的高
"""


def correct(word):
    """
    如果known(set)非空，candidate就会选取这个集合，而不继续计算后面的
    """
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=lambda w: NWORDS[w])


if __name__ == '__main__':
    print(correct("appl"))
