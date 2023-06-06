from flask import Flask, render_template, jsonify, request
import openai
import bot

def page_not_found(e):
    return  render_template('404.html'), 404

app = Flask(__name__)
app.register_error_handler(404, page_not_found)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':

        data = [request.form['healthCondition'] , request.form['severity']]

        if data[0] == "" or data[1] == "":
            res = {'response' : 'Bad request' , 'valid' : 'false'}
            return jsonify(res), 400
        
        upper_limit  = 100
        prompt = f'provide treatment options for {data[0]} with  {data[1]} severity in {upper_limit} words.'

        res= {}
        use_api = False
        res['response'] = 'API not in use.'
        res['valid'] = 'true'

        if use_api:
            res['response'] = bot.askGPT(prompt)
            res['valid'] = 'true'
        print(res)

        return jsonify(res), 200

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= '8888', debug= True)