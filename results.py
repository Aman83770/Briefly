from flask import Blueprint
Result = Blueprint('Result' , __name__)

#k-means
@Result.route('/result',methods = ['POST', 'GET'])

def result():
    if request.method == 'POST':
        result = request.form['text']
        k=process(result)
        return render_template('final.html', summary=k)
        



#lxa
@Result.route('/result2',methods = ['POST', 'GET'])

def result2():
    if request.method == 'POST':
        result = request.form['text']
        result1 = request.form['name']
        fo=open("input.txt","w")
        fo.write(result)
        fo.close()
        k=process2(result1)
        fo=open("lxa.txt","w")
        for item in k:
            fo.write("%s\n" % item)
        fo.close()
        return render_template('final.html', summary=k)
        




            
#lsa
@Result.route('/result3',methods = ['POST', 'GET'])

def result3():
    if request.method == 'POST':
        result = request.form['text']
        result1 = request.form['name']
        fo=open("inputtext.txt","w")
        fo.write(result)
        fo.close()
        k=process3(result1)
        fo=open("lsa.txt","w")
        for item in k:
            fo.write("%s\n" % item)
        fo.close()
        return render_template('final.html', summary=k)
        
        
