from flask import Flask, render_template, request
import sqlite3
from dbsetup import create_connection, select_all_records, update_record, database_startup
from questionaire import get_questions

app = Flask(__name__)
database = './poll.db'
conn = create_connection(database)
cur = conn.cursor()
poll_data = get_questions()

def check_arg(vote):
    if(vote == poll_data['fields'][0]):
        update_record(conn, 'OPTION_1')
    elif(vote == poll_data['fields'][1]):
        update_record(conn, 'OPTION_2')
    elif(vote == poll_data['fields'][2]):
        update_record(conn, 'OPTION_3')
    elif(vote == poll_data['fields'][3]):
        update_record(conn, 'OPTION_4')
    else:
        raise exception()

@app.route('/')
def root():
    return render_template('poll.html', data = poll_data)

@app.route('/poll_results', methods=['POST', 'GET'])
def poll_results():
    vote = request.args.get('field')
    check_arg(vote)
    conn.commit()
    options = list(select_all_records(conn)[0])
    print(options)
    return render_template('results.html', data=poll_data, results=options)


if __name__ == '__main__':
    database_startup()
    app.run(debug=True, port=5000)
