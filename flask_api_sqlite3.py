def createSqliteConnection(database):
    """ 
    Function that creates a connection to a sqlite3 database file.
	@param database -- The path and name of the database file to connect to.
    """
    conn = None
    try:
        print("----------Attempting to connect to database using Sqlite3 version {version} ...".format(version = sqlite3.version))
        conn = sqlite3.connect(database)
        print("----------Successfully to connected to {database}".format(database = database))
	except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def pandasToDatabase(csvDocument, database, tableName):
    conn = sqlite3.connect(database) 
    df = pd.read_csv(csvDocument)
    df.to_sql(tableName, conn, if_exists = "append", index = False)

if __name__ == '__main__':
    createSqliteConnection("data/datasciencejobs_database.db")
    pandasToDatabase("data/datasciencejobs_database.csv", "data/datasciencejobs_database.db", "tblJobs", )