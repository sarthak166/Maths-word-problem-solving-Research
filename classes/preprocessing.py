'''Pre processing of the question

'''
class preprocessing(parsers.Parser):
	def __init__(self,question):
		self.question=question
		self.word_dic={}
		self.num_dic={}

	def distingush_word(self):
		'''Function to label all same nouns associated with a number
		'''
		ques=self.question
		for word in self.parse:
			if(word.dep_=="nummod"):
				qword=word.head.text
				cword=lemmatizer.lemmatize(word.head.text)
				try:
					match = next(val for key, val in self.word_dic.items() if cword in key)
					self.word_dic[cword]=self.word_dic[cword]+1
					print(self.word_dic[cword])
				except StopIteration:
					self.word_dic[cword]=1
				fword=cword+str(self.word_dic[cword])
				print(fword)
				qword=qword+' '
				fword=fword+' '
				new_question=str.replace(self.question,qword,fword, 1)
				print(new_question)
				self.question=new_question
		self.parse=super(Extract_direct,self).dependency_parsing(self.question)
		print(self.question)
		return self.question

			

