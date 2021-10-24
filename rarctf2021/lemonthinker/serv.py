from flask import Flask, request
from deeppavlov import build_model

app = Flask(__name__)

@app.route('/')
def main():
    return """
<!DOCTYPE html>
<html>
<body>
<h2>DeepPavlov</h2>
<form action="/generate" method="post">
  <label for="payload">Your string:</label><br>
  <input type="text" id="payload" name="payload"><br><br>
  <input type="submit" value="Submit">
</form> 
</body>
</html>
    """

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.getlist('payload')[0]
    print(text)
    model = build_model('tfidf_logreg_en_faq', download=True)
    res = model([text])
    print(res)
    return str(res[1][1])
  
if __name__ == "__main__":
  app.run("0.0.0.0", 5050)