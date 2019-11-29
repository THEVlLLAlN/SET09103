from flask import Flask, request, redirect, session
import sqlite3
app = Flask(__name__)
app.secret_key='eggs'
@app.route("/makepost", methods=['POST','GET'])
def make_post():
    
    if session['usernames']==None:
        return redirect('http://webtech-47.napier.ac.uk:5000/')
    if request.method =='POST':
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        print request.form
        post = request.form['post']
        username = str(session['usernames'])

        cur.execute("INSERT INTO posts (contents, poster) VALUES ('%s','%s')" %(post,username,))
        conn.commit()
        conn.close()


        return redirect('http://webtech-47.napier.ac.uk:5000/hub')
    else:
        
        return "<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/hub'>Back to the hub</a><br><br><form action='' method='post' name='form'> <label for='name'>Post</label> <input type ='text' name='post' id='post'/><input type='submit' name ='submit' id='submit'/> </body></html>" 

@app.route("/privateMessaging", methods=['POST','GET'])
def pm():
    if session['loggedd']!= None:
        if request.method=='POST':
            print request.form
            message = request.form['message']
            reciever = request.form['reciever']
            username = session['usernames']
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO messages (sender, message, reciever) VALUES('%s','%s','%s')" %(username,message,reciever))
            conn.commit()
            conn.close()
            return redirect ('http://webtech-47.napier.ac.uk:5000/privateMessaging')
        else:
            username = session['usernames']
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM messages WHERE reciever='%s';"%username)
            results = cur.fetchall()
            post_list =""
            for row in results:
                row2=str(row).replace(", u","---")
                post_list = post_list +"<div style='background-color:lightblue'>" + row2 + "</div>" + "<br>"




            conn.commit()
            conn.close()

        return "<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/hub'>Back to the hub</a><br><br><form action='' method='post' name='form'> <label for='name'>Message</label> <input type ='text' name='message' id='message'/><br><label for='reciever'>Reciever</label><input type='text' name='reciever' id='reciever'/><input type='submit' name ='submit' id='submit'/><br>%s </body></html>" %post_list
    else: 
        return redirect('http://webtech-47.napier.ac.uk:5000/')
@app.route("/hub", methods=['POST','GET'])
def hub():
    if session['loggedd']==None:
        return redirect('http://webtech-47.napier.ac.uk:5000/')
    else:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()

        post_list ="<br>"
        cur.execute("SELECT * FROM posts")
        results = cur.fetchall()

        for row in results:
            row2=str(row).replace(", u","---")
            row2=row2.replace("None---","<b>Post:  </b>")
            row2=row2.replace("---","<b>    Poster:  </b>")
            post_list = post_list +"<div style='background-color:lightblue'>" + row2 + "</div>" + "<br>"



        post_list.replace(',','-')

        conn.commit()
        conn.close()
        return"<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/logout'>Logout</a><br>Wanna join in? <a href='http://webtech-47.napier.ac.uk:5000/makepost'> Make your own post!</a>---------------------<a href='http://webtech-47.napier.ac.uk:5000/privateMessaging'> Or privately message another user</a><br>%s</body></html>" % post_list
 
@app.route("/", methods=['POST','GET'])
def account():
    firstboot=0
    if request.method =='POST':
        print request.form
        username = request.form['name']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES ('%s','%s')" %(username,password,))
        post_list =""
        session['usernames'] = username
        session['loggedd'] = 2
        cur.execute("SELECT * FROM posts")
        results = cur.fetchall()
        for row in results:
            row2=str(row).replace(", u","---")
            row2=row2.replace("None---","<b>Post:  </b>")
            row2=row2.replace("---","<b>    Poster:  </b>")
            post_list = post_list +"<div style='background-color:lightblue'>" + row2 + "</div>" + "<br>"

            
        

        conn.commit()
        conn.close()
        return"<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/logout'>Logout</a><br>Wanna join in? <a href='http://webtech-47.napier.ac.uk:5000/makepost'> Make your own post!</a>---------------------<a href='http://webtech-47.napier.ac.uk:5000/privateMessaging'> Or privately message another user</a><br>%s</body></html>" % post_list

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
     session['usernames']=None
     session['loggedd']=None
     if request.method =='POST':
        print request.form
        username = request.form['name']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        for row in cur.execute("SELECT * FROM users WHERE username='%s' AND password='%s'" %(username,password,)): 
            logged=1
            post_list =""
            cur.execute("SELECT * FROM posts")
            results = cur.fetchall()
            for row in results:
                row2=str(row).replace(", u","---")
                row2=row2.replace("None---","<b>Post:  </b>")
                row2=row2.replace("---","<b>    Poster:  </b>")
                post_list = post_list +"<div style='background-color:lightblue'>" + row2 + "</div>" + "<br>"

            session['usernames']=username
            session['loggedd']=2
            return"<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/logout'>Logout</a><br>Wanna join in? <a href='http://webtech-47.napier.ac.uk:5000/makepost'> Make your own post!</a>---------------------<a href='http://webtech-47.napier.ac.uk:5000/privateMessaging'> Or privately message another user</a><br>%s</body></html>" % post_list
        else:
            return" <html> <head> <style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style> </head> <h1 color='blue'>Dungeons and Dragons: HUB</h1><h2>Please log in to access this site, dont have an account? <a href='http://webtech-47.napier.ac.uk:5000/'> Register!</a></h2><form action='' method='post' name='form'> <label for='name'>Username</label> <input type ='text' name='name' id='name'/> <br> <label for'password'>Password </label> <input type ='text' name='password' id='password'> <input type='submit' name ='submit' id='submit'/><br><body>There was no account with that credientials found, try again? </body> </html>" 
    

        
        
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
