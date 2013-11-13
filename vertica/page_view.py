from pyvertica.connection import get_connection
import sys
import psycopg2

DSN = 'dbname=bidw host=vertica-load01.newokl.com port=5433 user=vertica pass=test'

## don't modify anything below this line (except for experimenting)

class SimpleQuoter(object):
    def sqlquote(x=None):
        return "'bar'"



if len(sys.argv) > 1:
    DSN = sys.argv[1]

print "Opening connection using dns:", DSN
conn = psycopg2.connect(DSN)
print "Encoding for this connection is", conn.encoding

curs = conn.cursor()
curs.execute("SELECT 1 AS foo")
print curs.fetchone()
curs.execute("SELECT 1 AS foo")
print curs.fetchmany()
curs.execute("SELECT 1 AS foo")
print curs.fetchall()

conn.rollback()

sys.exit(0)

sql_query = "select CONCAT(TO_CHAR(DATE(yoda.yoda.action_time)), CONCAT ('-', LPAD(TO_CHAR(HOUR(yoda.yoda.action_time)), 2, '0'))) as hours, count(*) page_count FROM yoda.yoda where yoda.yoda.action_name in ('signup_modal', 'join','login') group by 1 order by 1;"

results = curs.execute(sql_query, async=1)

#curs.execute("SELECT %(foo)s AS foo", {'foo':'bar'})
#curs.execute("SELECT %(foo)s AS foo", {'foo':None})
#curs.execute("SELECT %(foo)f AS foo", {'foo':42})
#curs.execute("SELECT %(foo)s AS foo", {'foo':SimpleQuoter()})