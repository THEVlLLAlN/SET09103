from flask import Flask, request
app = Flask(__name__)


@app.route("/account/", methods=['POST','GET'])
def account():
    logged = 0
    if request.method =='POST':
        print request.form
        name = request.form['name']

        return "<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in as %s!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/logout'>Logout</a></body></html>" % name

    else:
      page ="""
        <html>
        <head>
        
        <style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style>
        </head>
        <h1 >Dungeons and Dragons: HUB</h1>
        <h2>Make a temporary username and log in!</h2>
        <form action="" method="post" name="form">
            <label for="name">Temporary Name</label>
            <input type ="text" name="name" id="name"/>
            <input type="submit" name ="submit" id="submit"/>
        </html>
        """
    return page

@app.route("/logout", methods=['POST','GET'])
def logout():
     if request.method =='POST':
        print request.form
        name = request.form['name']

        return "<html><head><style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style></head><h1>Dungeons and Dragons: HUB</h1><h2>You are logged in as %s!</h2><body><a href='http://webtech-47.napier.ac.uk:5000/logout'>Logout</a></body></html>" % name

     else:
      page ="""
        <html>
        <head>
        <style>html{background-color:#fefefe} body{font-family: Calibri; color:#454545; font-size:16px;margin:2em auto;max-width:800px;padding:1em;line-height:1.4;text-align:justify} h1 { text-align: Center} a {color: #07a} a:visited {color: #FF7E47} textarea{resize: none;} .btn { border: none; background-color: inherit; padding: 14px 28px; font-size: 16px; cursor: pointer; display: inline-block; }/* Green */ .success { color: #07a; } .success:hover { background-color: #07a; color: white; }</style>
        </head>
        <h1 color="blue">Dungeons and Dragons: HUB</h1>
        <h2>Make a temporary username and log in!</h2>
        <form action="" method="post" name="form">
            <label for="name">Temporary Name</label>
            <input type ="text" name="name" id="name"/>
            <input type="submit" name ="submit" id="submit"/>
        </html>
        """
     return page



if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=True)
