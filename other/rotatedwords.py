"""
如果一个单词通过循环右移获得的单词，我们称这些单词都为一种循环单词。
例如：picture 和 turepic 就是属于同一种循环单词。 现在给出n个单词，需要统计这个n个单词中有多少种循环单词。
"""
#输入包括n+1行：
#第一行为单词个数n(1 ≤ n ≤ 50)
#接下来的n行，每行一个单词word[i]，长度length(1 ≤ length ≤ 50)。由小写字母构成
#输出循环单词的种数

'''
示例1
输入
5
picture
turepic
icturep
word
ordw
输出2
'''

while True:
	try:
		n = int(input())
		words = []
		for i in range(n):
			words.append(input())

		count = 0
		all_words = []
		for word in words:
			if word not in all_words:
				count += 1
				all_words.append(word)
				new_word = word[1:] + word[:1]
				while new_word != word:
					all_words.append(new_word)
					new_word = new_word[1:] + new_word[:1]
		print(count)
	except:
		break
