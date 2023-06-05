from flask import Flask, render_template, jsonify, request
import openai
# import time
import bot

def page_not_found(e):
    return  render_template('404.html'), 404

app = Flask(__name__)
app.register_error_handler(404, page_not_found)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':

        data = [request.form['healthCondition'] , request.form['severity']]

        prompt = f'provide treatment options for {data[0]} with  {data[1]} severity.'

        res= {}
        use_api = False
        res['answer'] = 'API not in use.'
        if use_api:
            res['answer'] = bot.askGPT(prompt)
        print(res)
        # time.sleep(3)
        return jsonify(res), 200

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= '8888', debug= True)