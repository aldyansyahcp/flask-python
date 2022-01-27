from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "DUMB"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/var")
def vari():
    nilai = 100
    return render_template("var.html", nilai = nilai)
    
@app.route("/loop")
def loop():
    nama = [
        "Meliodas",
        "Ban",
        "Diane",
        "King",
        "Merlin",
        "Gowther",
        "Escanor"
    ]
    return render_template("loop.html", nam=nama)

@app.route("/lese")
def lese():
    akun = "gacor"
    return render_template("lese.html", akun=akun)

@app.route("/parsinginteger/<int:nilai>")
def parser(nilai):
    return f"<center><h2>nilai integernya adalah {nilai}</center></h2>"
    #http://127.0.0.1:5000/parsing/100(integer)
    
@app.route("/parsinstring/<string:nilai>")
def parse(nilai):
    return f"<center><h2>nilai string adalah {nilai}</center></h2>"
    #http://127.0.0.1:5000/parsin/oke(string)
    
@app.route("/parsingargument/")
def pargur():
    data = request.args.get("nilai")
    return "<center><h2>nilai dari parsing argument adalah {}</center></h2>".format(data)
    #http://127.0.0.1:5000/parsingargument/?nilai=100(parameter)

@app.route("/session/<nilai>")
def ses1(nilai):
    session["nomer"] = nilai
    return "<center><h1>Berhasil set nilai</h1></center>"

@app.route("/session/cek")
def cek():
    try:
        data = session["nomer"]
        return "<center><h1>Nilai diset sebesar {}</h1></center>".format(data)
    except KeyError:
        return "<center><h1>Nilai sudah anda reset</h1></center>"

@app.route("/session/reset")
def resett():
    session.pop("nomer")
    return "<center><h1>Nilai sudah direset anda bisa set lagi di <br><a href='http://127.0.0.1:5000/session/'>disini</a></h1></center>"

if __name__ == "__main__":
    app.run(debug=True)
