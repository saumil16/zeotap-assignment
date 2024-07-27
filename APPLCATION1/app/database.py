import sqlite3

def initialize_database():
    conn = sqlite3.connect('rule_engine.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rules (
                 id INTEGER PRIMARY KEY,
                 rule_string TEXT,
                 ast BLOB)''')
    conn.commit()
    conn.close()



def save_rule(rule_string, ast):
    conn = sqlite3.connect('rule_engine.db')
    c = conn.cursor()
    c.execute("INSERT INTO rules (rule_string, ast) VALUES (?, ?)",(rule_string, repr(ast)))
    conn.commit()
    conn.close()



def load_rules():
    conn = sqlite3.connect('rule_engine.db')
    c = conn.cursor()
    c.execute("SELECT rule_string, ast FROM rules")
    rules = c.fetchall()
    conn.close()
    return rules

initialize_database()