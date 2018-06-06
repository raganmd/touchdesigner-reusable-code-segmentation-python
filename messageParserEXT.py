'''
	The MessageParser and General classes are intended to be the 
	classes that persist from project to project. The parser is the meta
	function that handles message receiving and sending.
'''

class MessageParser:

	def __init__(self, my_op):
		self.Me 	= my_op
		print("Parser init")
		return
	
	def Process_message(self, message):
		incoming_messagekind 		= message.get('messagekind')

		# test to see if a matching method exists
		if hasattr(self.Me, incoming_messagekind):
			function 				= getattr(self.Me, incoming_messagekind)

			# call the method if it exists
			function(message)
		
		else:
			# return an invalid message if no matching method exists
			print("Invalid Call")

		return