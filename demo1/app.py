from flask import Flask, request, redirect, url_for


app = Flask(__name__)


INDEX = """
<html>
  <head></head>
  <body>
    <form action="" method="POST">
      <label for="answer">What's the answer to life, the universe, and everything?</label>
      <input id="answer" name="answer" type="text">
      <br>{error}
    </form>
  </body>
</html>
"""


@app.route("/", methods=['GET', 'POST'])
def hello():
    error = u""
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer != 42:
            error = u"Wrong answer: {} != 42".format(answer)
        else:
            return redirect(url_for('winner'))

    return INDEX.format(error=error)


@app.route("/winner")
def winner():
    return 'YOU WIN! <a href="/">back</a>'
