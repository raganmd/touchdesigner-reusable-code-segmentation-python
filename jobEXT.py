'''
	The Specific class handles the requirements that are specific to a 
	particular job. We separate these functions into two classes as there
	are always cases where a particular venue has a particular requirement
	that doesn't fit with the schema of a larger system. We might find
	that one of these functions can be generalized and pulled into the
	General class, but if you're writing something that's specific to a
	single job or venue, this is the place for that function.
'''

General = mod("generalEXT").General

class Specific(General):
	def __init__(self):
		General.__init__(self)
		return

	def Image_order(self, message):
		
		vals 					= message.get('vals')

		if vals:
			op('table1')[1, 2] 	= "'moviefilein2 moviefilein1'"

		else:
			op('table1')[1, 2] 	= "'moviefilein1 moviefilein2'"

		return