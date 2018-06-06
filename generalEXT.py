'''
	The MessageParser and General classes are intended to be the 
	classes that persist from project to project. The General class
	here takes care of fucntions that are universal to all projects. If 
	the function in question applies to only a specific project,
	then it fits better in the venue extension.
'''

messageParser = mod('messageParserEXT').MessageParser

class General(messageParser):
	def __init__(self, my_op):
		messageParser.__init__(self, my_op)
		print("General init")
		return

	def Change_switch(self, message):
		vals 		= message.get('vals')

		op('constant1').par.value0 = vals

		return