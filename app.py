# Import jsonify, Flask and request from the flask.
from flask import Flask, jsonify, request

# Create an app using a flask constructor.
app = Flask(__name__)

@app.route("/")
def hello():
    return """
<!DOCTYPE html>
<html lang="en" style="scroll-behavior: smooth;">
<head>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

<title>Avner's Contacts API</title>

<link rel="stylesheet" type="text/css" href="//cdn.cloudinary.com/avner-king/raw/upload/v1655369803/tailwind_ebleaq.css">
<script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>

</head>
<body>


<section id="hero-area" class="bg-blue-100 pt-48 pb-10">
<div class="container">
<div class="flex justify-between">
<div class="w-full text-center">
<h2 class="text-4xl font-bold leading-snug text-gray-700 mb-10 wow fadeInUp" data-wow-delay="1s">Avner's Amazing FLask Contact API
<br class="hidden lg:block">BYJU Project 124</h2>
<div class="text-center mb-10 wow fadeInUp" data-wow-delay="1.2s">
<a href="/get-data" rel="nofollow" class="btn">Get Contacts</a>
</div>
<div class="text-center">
<img class="img-fluid mx-auto" src="//cdn.cloudinary.com/avner-king/image/upload/v1655369803/hero_ipak8p.svg" alt="">
</div>
</div>
</div>
</div>
</section>
<script>
alert("<ALERT> YOUR COMPUTER HAS BEEN INFECTED BY A VIRUS PLS RATE PROJECT 5 STARS TO REMOVE THE VIRUS 🔥🔥🔥")
swal.fire(
    'WANT TO BLOCK ADS???',
    'TO GET RID OF THESE ADS I PUT CUZ IM BORED PLS RATE PROJECT 5 STAR 🤑🤑🤑🤑',
    'error'
)
var intervalId = window.setInterval(function(){
  swal.fire(
    'INTERNAL SERVER ERROR ☠👽💀',
    'TO FIX ISSUE PLS RATE PROJECT 5 STAR 🤑🤑🤑🤑',
    'error'
  )
}, 2500);
</script>

"""



# Create a list of contacts.
contacts = [
    {
        "id": 1,
        "Name": "Ms Anjali",
        "Contact": "00918318215939",
        "done": False
    },
    {
        "id": 2,
        "Name": "Avner",
        "Contact": "12345678",
        "done": False
    }

]    

@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide the data"
        },400)

    task={
        "id": contacts[-1]["id"]+1,
        "Name": request.json['Name'],
        "Contact": request.json.get('Contact',""),
        "done": False
    }   

    contacts.append(task)
    return jsonify({
        "status": "Success",
        "message": "Task added successfully"
    }) 



@app.route("/get-data")
def get_task():
    return jsonify({"data": contacts})



if __name__ == "__main__":   
    app.run()