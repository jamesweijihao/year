from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('year.html')


@app.route('/convert')
def convert():
    tian = {0:'申',1:'酉',2:'戍',3:'亥',4:'子',5:'丑',6:'寅',7:'卯',8:'辰',9:'巳',10:'午',11:'未'}
    di = {0:'庚',1:'辛',2:'壬',3:'癸',4:'甲',5:'乙',6:'丙',7:'丁',8:'戊',9:'己'}
    get_year = int(request.args.get('year'))
    n = get_year%12
    m = get_year%10
    return_year = di[m]+tian[n]
    return render_template('convert.html',g_y=str(get_year),r_y=return_year)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='80')
