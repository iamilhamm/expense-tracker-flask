from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123.Algeria'
app.config['MYSQL_DB']='Python_Db'

mysql=MySQL(app)

@app.route('/')
def index():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM expense_tracker")
    data=cur.fetchall()
    return render_template('index.html', expense_tracker=data)


@app.route('/insert', methods=['POST'])
def insert():
    Category= request.form['category']
    Amount= request.form['amount']
    Description= request.form['description']
    cur= mysql.connection.cursor()
    cur.execute('INSERT INTO expense_tracker(Category, Amount, Description) VALUES(%s, %s, %s)',
                (Category, Amount, Description))
    mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM expense_tracker WHERE id = %s', (id,))
    mysql.connection.commit()
    return redirect(url_for('index'))


if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)