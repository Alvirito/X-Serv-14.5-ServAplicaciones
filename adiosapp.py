#!/usr/bin/python
import webapp

class adiosApp(webapp.webApp):

	def process(self,parsedRequest):
		"""Process the relevant elements of the request.

		Devuelve el codigo HTTP de la respuesta y una pag HTML.
		"""

		return("200OK", "<html><body><h1>ADIOS mundo :( </h1></body></html>")

if __name__=="__main__":
	testWeb=adiosApp("localhost",1234)
