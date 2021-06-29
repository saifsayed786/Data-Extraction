import nltk
import json
import string
import slate3k as slate

with open('Alien-Pets.pdf', 'rb') as f:
    extracted_text = slate.PDF(f)

with open('Alien.txt',"w+") as file1:
	file1.writelines(extracted_text)
	file1.seek(0)
	file2=file1.read()

def clean():
	from nltk.tokenize import word_tokenize
	tokens = word_tokenize(file2)

	# convert to lower case
	tokens = [w.lower() for w in tokens]

	# remove punctuation from each word
	table = str.maketrans('', '', string.punctuation)
	stripped = [w.translate(table) for w in tokens]

	# remove remaining tokens that are not alphabetic
	words = [word for word in stripped if word.isalpha()]

	# remove duplicate words
	#new_words = (list(set(words)))

	data={}
	data['myfile']=[]
	data['myfile'].append(words)

	#for appending the removed duplicated
	# data['myfile'].append(new_words)
	
	#print(type(data))

	with open("Alienfile.json", "wb") as f:
	    f.write(json.dumps(data,indent=2).encode("utf-8"))

if __name__ == '__main__':
	clean()