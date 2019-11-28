from flask import Flask, request, redirect
import sqlite3
app = Flask(__name__)

@app.route("/makepost", methods=['POST','GET'])
def make_post():
    if request.method =='POST':
        return redirect('http://webtech-47.napier.ac.uk:5000/hub')
    else:
        return ""


@app.route("/hub", methods=['POST','GET'])
def hub():
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()

        post_list =""
        cur.execute("SELECT * FROM posts")
        results = cur.fetchall()
        for row in results:
            post_list = post_list + str(row) + "<br>"

        conn.commit()
        conn.close()
        return"<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/logout'>Logout</a><br>Wanna join in? <a href='http://webtech-47.napier.ac.uk:5000/makepost'> Make your own post!</a><br>%s</body></html>" % post_list
 
@app.route("/", methods=['POST','GET'])
def account():
    logged = 0
    if request.method =='POST':
        print request.form
        username = request.form['name']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES ('%s','%s')" %(username,password,))
        post_list =""
        cur.execute("SELECT * FROM posts")
        results = cur.fetchall()
        for row in results:
            post_list = post_list + str(row) + "<br>"

        conn.commit()
        conn.close()
        return"<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/logout'>Logout</a><br>Wanna join in? <a href='http://webtech-47.napier.ac.uk:5000/makepost'> Make your own post!</a><br>%s</body></html>" % post_list

    else:
      
      page ="""
        <html>
        <head>
        
        <style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style>
        </head>
        <h1 >Dungeons and Dragons: HUB</h1>
        <h2>Please Sign up in order to access this site. Already signed up? <a href='http://webtech-47.napier.ac.uk:5000/logout'> Log in!</a></h2>
        <form action="" method="post" name="form">
            <label for="name">Username</label>
            
            <input type ="text" name="name" id="name"/>
<br>
            <label for"password">Password  </label>
            <input type ="text" name="password" id="password">
            <br>
            <input type="submit" name ="Register" id="submit"/>
        </html>
        """
    return page

@app.route("/logout", methods=['POST','GET'])
def logout():
     logged=0
     if request.method =='POST':
        print request.form
        username = request.form['name']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT * FROM users WHERE username='%s' AND password='%s'" %(username,password,)): 
            logged+=1
            post_list =""
            cur.execute("SELECT * FROM posts")
            results = cur.fetchall()
            for row in results:
                post_list = post_list + str(row) + "<br>"

             
            return"<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/logout'>Logout</a><br>Wanna join in? <a href='http://webtech-47.napier.ac.uk:5000/makepost'> Make your own post!</a><br>%s</body></html>" % post_list
        else:
            return" <html> <head> <style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style> </head> <h1 color='blue'>Dungeons and Dragons: HUB</h1> <h2>Make a temporary username and log in!</h2> <form action='' method='post' name='form'> <label for='name'>Username</label> <input type ='text' name='name' id='name'/> <br> <label for'password'>Password </label> <input type ='text' name='password' id='password'> <input type='submit' name ='submit' id='submit'/><br><body>There was no account with that credientials found, try again? </body> </html>" 
    

        
        
        conn.commit()
        conn.close()
     else:
            page ="""
        <html>
        <head>
        <style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style>
        </head>
        <h1 color="blue">Dungeons and Dragons: HUB</h1>
        <h2>Log into your account, dont have an account? <a href='http://webtech-47.napier.ac.uk:5000/'>Register!</a></h2>
        <form action="" method="post" name="form">
            <label for="name">Username</label>
            <input type ="text" name="name" id="name"/>
            <br>
            <label for"password">Password  </label>
            <input type ="text" name="password" id="password">
            <input type="submit" name ="submit" id="submit"/>
        </html>
        """
            
            return page

if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=True)
