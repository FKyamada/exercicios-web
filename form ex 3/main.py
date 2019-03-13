from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def student():
	return render_template("student.html")

@app.route("/result",methods=['POST'])
def result():
     if request.method == "POST":
     	result = request.form
     	print("result")
     	print(result)
     	return render_template("result.html",result)

if __name__ == "__main__":
		app.run(host="0.0.0.0",debug= True)

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/loginresult", methods=['POST'])
def login_result():
	if request.method == "POST":
	return render_template("loginresult.html")

@app.route("/loginresult", methods = ["POST"])
def login_result():
	if request.method == "POST":	
		result = result.form
		print("result")
		print(result)
	result = {"status":"correto"}
	if usuario_existe(result["email"]):

		if verifica_senha(result["email"], result["senha"]):
			return render_template("loginresult.html", result)
		else:
	result["status"] = "senha_incorreta"
			return render_template("loginresult.html",result)
		else:
	result["status"]="usuario_incorreto"
			return render_template("loginresult.html",result)
