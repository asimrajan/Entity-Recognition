import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('averaged_perceptron_tagger')


def enty(sentence):
	dic = {}
	sentence = nltk.word_tokenize(sentence)
	sentence = nltk.pos_tag(sentence)
	print("this is sent : ",sentence)
	for k,v in sentence:
		dic[k] = v
	return dic
	#return render_template("temp.html",data=dic))