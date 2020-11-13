from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/jobs/datascience/all', methods=['GET'])
def apiViewAll():
    conn = sqlite3.connect('data/datasciencejobs_database.db')
    conn.row_factory = dictFactory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM tblJobs;').fetchall()
    return jsonify(all_books)

@app.route('/api/v1/jobs/datascience', methods=['GET'])
def apiViewByFilter():
    '''
    Function that allows users to filter the results in the API
	based on specified input.
    '''
    query_parameters = request.args
    id = query_parameters.get('id')
    dateTime = query_parameters.get('dateTime')
    cleanContent = query_parameters.get('cleanContent')
    country = query_parameters.get('country')
    query = "SELECT * FROM tblJobs WHERE"    to_filter = []
    if id:
        query += ' id=? AND'
        to_filter.append(id)    
	if dateTime:
        query += ' dateTime=? AND'
        to_filter.append(dateTime)
	if cleanContent:
        query += ' cleanContent=? AND'
        to_filter.append(cleanContent)
	if country:
        query += ' country=? AND'
        to_filter.append(country)    
	if not (id or dateTime or cleanContent or country):
        return pageNotFound(404)    
	query = query[:-4] + ';'
    conn = sqlite3.connect('data/datasciencejobs_database.db')
    conn.row_factory = dictFactory
    cur = conn.cursor()    
	results = cur.execute(query, to_filter).fetchall()    
	return jsonify(results)

app.run()