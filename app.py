import mysql.connector as MySql
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
Dbms = MySql.connect(host="localhost", user="root", passwd="shetty", database="petrol")
cursor = Dbms.cursor()
cursor.execute("Use petrol")


# payment
@app.route('/payment_enter', methods=['GET', 'POST'])
def index_payment():

    if request.method == 'GET':
        return render_template('payment.html')

    if request.method == 'POST':
        pid = request.form.get("pid")
        amt = request.form.get("amt")
        date = request.form.get("date")
        time = request.form.get("time")
        uid = request.form.get("uid")
        fid = request.form.get("fid")
        cursor.execute("INSERT INTO buys(pid, amt, date,time,uid,fid) VALUES(%s,%s,%s,%s,%s,%s)",
                       (pid, amt, date, time, uid,fid,))
        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('payment.html')

#trigger





# fuel
@app.route('/fuel_enter', methods=['GET', 'POST'])
def index_ppd():
    if request.method == 'GET':
        return render_template('fuel.html')

    if request.method == 'POST':
        fid = request.form.get("fid")
        fuel_type = request.form.get("fuel_type")
        ppid = request.form.get("ppid")
        rem_qty = request.form.get("rem_qty")
        price = request.form.get("price")
        cursor.execute("INSERT INTO fuel(fid, fuel_type, ppid,rem_qty,price) VALUES(%s,%s,%s,%s,%s)", (fid, fuel_type, ppid,rem_qty,price))
        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('fuel.html')

#crud_fuel_updates

@app.route("/update_fuel_button", methods=['POST'])
def update_fuel_record():
    fid = request.form.get("fid")
    fuel_type = request.form.get("fuel_type")
    ppid = request.form.get("ppid")
    rem_qty = request.form.get("rem_qty")
    price = request.form.get("price")

    cursor.execute("""
                update fuel
                set fid=%s, fuel_type=%s, ppid=%s,rem_qty=%s,price=%s,
                where fid=%s
                """, (fid, fuel_type, ppid,rem_qty,price,))

    Dbms.commit()
    return "Successfully updated a data"







#tax
@app.route('/tax_enter', methods=['GET', 'POST'])
def index_ppg():

    if request.method == 'GET':
        return render_template('tax.html')

    if request.method == 'POST':
        tid = request.form.get("tid")
        fid = request.form.get("fid")
        tax = request.form.get("tax")
        cursor.execute("INSERT INTO tax1(tid,fid, tax) VALUES(%s,%s,%s)", (tid,fid,tax))

        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('tax.html')




#crud_delete_tax
@app.route("/add_tax_button", methods=['POST'])
def add_tax_record():
    tid = request.form.get("tid")
    fid = request.form.get("fid")
    amt = request.form.get("amt")

    cursor.execute("""
                INSERT INTO tax(tid,fid, amt) VALUES(%s,%s,%s)
                """, (tid,fid,amt,))
    Dbms.commit()
    return "Successfully added a tax data"




@app.route('/view_tax')
def render_all_orders():
    cursor.execute("""SELECT * FROM tax""")
    tax_query=cursor.fetchall()

    return render_template("order_details.html", orders=tax_query)

@app.route('/delete_tax_button', methods=['POST'])
def delete_orders():
    tid = request.form.get("tid")

    cursor.execute("""
            DELETE FROM tax WHERE tid=%s
            """,(tid,))
    Dbms.commit()
    return "tax deleted Successfully"





# user
@app.route('/register_enter', methods=['GET', 'POST'])
def index_register():

    if request.method == 'GET':
        return render_template('registration.html')

    if request.method == 'POST':
        uid = request.form.get("uid")
        date = request.form.get("date")
        fid = request.form.get("fid")
        qty = request.form.get("qty")
        amt = request.form.get("amt")
        ppid = request.form.get("ppid")
        name = request.form.get("name")
        phone = request.form.get("phone")
        address = request.form.get("address")


        #cursor.execute("INSERT INTO user(uid, date,fid,qty,amt,ppid,name,phone,address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       #(uid, date,fid,qty,amt,ppid,name,phone,address))
        cursor.execute(
            "INSERT INTO user1(uid, date) VALUES(%s,%s)",
            (uid, date,))
        cursor.execute(
            "INSERT INTO user2(uid,fid,qty,amt,ppid) VALUES(%s,%s,%s,%s,%s)",
            (uid, fid, qty, amt, ppid,))
        cursor.execute(
            "INSERT INTO user3(uid,name,phone,address) VALUES(%s,%s,%s,%s)",
            (uid, name, phone, address))
        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('registration.html')









# petrol_pump
@app.route('/petrol_pump_enter', methods=['GET', 'POST'])
def index_petrol_pump():

    if request.method == 'GET':
        return render_template('petrol_pump.html')

    if request.method == 'POST':
        ppid = request.form.get("ppid")
        branch = request.form.get("branch")
        city = request.form.get("city")
        state = request.form.get("state")
        reg_no = request.form.get("reg_no")
        owner = request.form.get("owner")
        cursor.execute("INSERT INTO petrol_pump(ppid, branch, city, state, reg_no, owner) VALUES(%s,%s,%s,%s,%s,%s)",
                       (ppid, branch, city, state, reg_no, owner))
        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('petrol_pump.html')









#crud_petrol_updates

@app.route("/update_petrol_button", methods=['GET','POST'])
def update_petrol_record():
    if request.method == "GET":
        return render_template('crud_updates.html')

    if request.method == "POST":
        ppid = request.form.get("ppid")
        branch = request.form.get("branch")
        city = request.form.get("city")
        state = request.form.get("state")
        reg_no = request.form.get("reg_no")
        owner = request.form.get("owner")

        cursor.execute("""
                update petrol_pump
                set branch=%s, city=%s, state=%s, reg_no=%s, owner=%s
                where ppid=%s
                """, (branch, city, state, reg_no, owner,ppid, ))

        Dbms.commit()
        return render_template('crud_updates.html')









@app.route('/')
def home():
    return render_template('petrolpump1.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route("/fuel")
def fuel():
    return render_template('fuel.html')


@app.route('/tax')
def tax():
    return render_template('tax.html')


@app.route('/payment')
def payment():
    return render_template('payment.html')


@app.route('/petrol_pump')
def petrol_pump():
    return render_template('petrol_pump.html')

@app.route('/crud_updates')
def crud_updates():
    return render_template('crud_updates.html')


if __name__ == '__main__':
    app.run(debug=True)
