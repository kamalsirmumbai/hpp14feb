from  flask  import  *
from pickle import  load
import os

with open("hpp.pkl", "rb") as f:
	model = load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		area = float(request.form.get("area"))
		price = model.predict([[area]])
		msg = "Price = ₹" + str(round(price[0], 2)) + " crores"
		return render_template("home.html", msg=msg)
	else:
		return render_template("home.html")


#port = int(os.environ.get("PORT", 5000))

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=port)



