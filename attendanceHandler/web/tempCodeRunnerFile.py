from flask import Flask, render_template

class WebHandler(Flask):

    def __init__(self,moduleName):
        super().__init__(moduleName)
        
    # def setRoutWebPage(self):
        @self.route('/')
        def getMainWebPage():
            return render_template("index.html")
        
        @self.route('/terceranio/seminario')
        def getSeminarioWebPage():
            return render_template("index.html")
            # return "¡Esta es otra ruta!"

if __name__ == '__main__':
    app = WebHandler(__name__)
    app.run()
