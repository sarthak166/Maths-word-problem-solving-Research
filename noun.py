import spacy
nlp=spacy.load('en')
question1=u'There are 6 Students in the class and 18 candies. If candies are divided equally among students, how many does each student get?'
question2=u'Gwen was organizing her book case making sure each of the shelves had exactly 9 books on it. She has 2 types of books - mystery books and picture books. If she had 3 shelves of mystery books and 5 shelves of picture books,how many books did she have total?'
doc=nlp(question1)
doc1=nlp(question2)
for np in doc.noun_chunks:
	np.text
for np in doc1.noun_chunks:
	np.text 
