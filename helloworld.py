import webapp2

class MainPage(webapp2.RequestHandler):
    #fromstring='''<form method="post" action="/">
    #<p>Enter Guess:<input type="text" name="guess"/></p>
    #<p><input type="submit"/></p>
    #</form>'''
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, webapp2!')
        #self.response.write(self.formstring)

    #def post(self):
    #    stguess = self.request.get('guess')
    #    answer =42
    #    self.response.write('<p>Guess:'+stguess+'</p>\n')
    #    self.response.write(self.formstring)
class ProductListHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('This is the productList Handler 1' )
        #self.response.write("This is the ProductHandler"
        #                    'The product id is %s'%product_id)

class ProductHandler(webapp2.RequestHandler):
    def get(self,id,id2):
        self.response.headers['Content-Type'] = 'text/plain'
        value = int(id)*int(id2)*2
        self.response.write(" The product jj is %s" % value)
        
routes = [
    (r'/', MainPage),
    (r'/products',ProductListHandler),
    (r'/products/(\d+)/(\d+)',ProductHandler),
]
application = webapp2.WSGIApplication(routes, debug=True)
