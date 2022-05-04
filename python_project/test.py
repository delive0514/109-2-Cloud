from flask import Flask, request, render_template 
import pymysql 

db = pymysql.connect(host='localhost',
                    user='root',
                    password='',
                    database='cloud',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__) 
@app.route('/') 
def checked():
    cursor = db.cursor() 
    sql = "SELECT * FROM movie_seat" 
    cursor.execute(sql) 
    results = cursor.fetchall() 
    color=["0"]*24
    for i in range(0,len(color)):
        if(results[i]['isChecked']==0):
            color[i]="#FFFFFF"
        else:
            color[i]="#D5A466"
    return render_template('index.html', results=results,color = color)
@app.route("/test", methods=['POST'])
def test():
    name = request.values['name']
    identity = request.values['identity']
    row = request.values['row']
    col = request.values['col']
    
    cursor = db.cursor()
    sql =f"UPDATE `movie_seat` SET name='{name}',identity='{identity}',isChecked='1' WHERE SeatRow ='{row}' AND SeatCol ='{col}'"
    cursor.execute(sql)
    db.commit()
    print(sql)
    return render_template('test.html',**locals())

if __name__ == '__main__': 
    app.run(debug=True) 