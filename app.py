from flask import Flask, render_template, request
import MySQLdb
app = Flask(__name__)
import random
conn = MySQLdb.connect(host="localhost",user="root",password="",db="bugtrack")
import uuid



cursor = conn.cursor()

@app.route('/')
def selectBugReportOption():
    return render_template("index.html")

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/track', methods = ['POST'])
def trackBug():
    if request.method == 'POST':
        return render_template('trackbug.html')

@app.route('/successtrack', methods=['POST'])
def trackedBug():
    if request.method == 'POST':
        bugid = int(request.form["bugid"])
        dbugid = cursor.execute("SELECT bugid FROM buginfo where bugid=%s", [bugid])
        if dbugid:
            bug_details = [cursor.execute("SELECT * FROM buginfo WHERE bugid=%s", [bugid])]
            bug_details = cursor.fetchall()
            return render_template("successtrack.html", bugdetails=bug_details)
        else:
            return render_template("trackbug.html", msg="No details found for that bugid")

@app.route('/file', methods=['POST'])
def fileBugReport():
    if request.method == 'POST':
        return render_template("bugreportfile.html")

@app.route('/success', methods=['POST'])
def filedBugReport():
    if request.method == 'POST':
        id = uuid.uuid1()
        id = int(str(id.int)[:4])
        ids = [cursor.execute("SELECT bugid FROM buginfo")]
        for i in ids:
            if id == i:
                filedBugReport()
        tob = str(request.form['tob'])
        description = str(request.form['desc'])
        priority = int(request.form['priority'])
        status = str(request.form['status'])
        name = str(request.form['cname'])
        result = cursor.execute("INSERT INTO buginfo (bugid, tob, description, priority, status, name) VALUES (%s, %s, %s, %s, %s, %s)", [id, tob, description, priority, status, name])
        conn.commit()
        if result:
            return render_template("success.html", id=str(id)+" is the id for further reference")


@app.route('/edit', methods = ['POST'])
def editBug():
    if request.method == 'POST':
        return render_template("editbug.html")

@app.route('/successedit', methods = ['POST'])
def editedBug():
    if request.method == 'POST':
        bugid = int(request.form['bugide'])
        dbugid = cursor.execute("SELECT bugid FROM buginfo where bugid=%s", [bugid])
        if dbugid:
            tob = str(request.form['tobe'])
            description = str(request.form['desce'])
            priority = int(request.form['prioritye'])
            status = str(request.form['statuse'])
            name = str(request.form['cnamee'])
            result = cursor.execute("UPDATE buginfo SET tob=%s, description=%s, priority=%s, status=%s, name=%s WHERE bugid=%s", [tob, description, priority, status, name, bugid])
            conn.commit()
            if result:
                return render_template("successedit.html", id= " details was updated")
        else:
            return render_template("editbug.html", msg="bugid does not exist to edit")

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000, debug=True)