from flask import Flask, render_template,request
from datetime import datetime

class WebHandler(Flask):

    def __init__(self,moduleName):
        super().__init__(moduleName)
        self.fecha_hora = ''
        @self.route('/', methods=['GET', 'POST'])
        def getMainWebPage():   
            if request.method == 'POST' or request.method == 'GET':
                self.fecha_hora = datetime.now()
            return render_template("index.html")
        
        @self.route('/form-example',methods=['GET', 'POST'])
        def getData():
            field1 = request.form.get('nombre')
            field2 = request.form.get('apellido')
            field3 = request.form.get('cuilt')

            return '''
                <h1>Con sus límites:</h1>
                <ul>
                    <li><h1>Name: {}</h1></li>
                    <li><h1>Apellido:= {}</h1></li>
                    <li><h1>CUILT: {}</h1></li>
                    <li><h1>Date: {}</h1></li>
                </ul>
                '''.format(field1,field2,field3,self.fecha_hora)
    def getDate(date):
        return date

    
app = WebHandler(__name__)

print()
    
if __name__ == '__main__':
    app.run()
