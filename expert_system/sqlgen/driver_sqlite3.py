# $Id: driver_sqlite3.py 6de8ee4e7d2d 2010-03-29 mtnyogi $
# coding=utf-8

import os.path
import contextlib
import sqlite3 as db
from pyke import test
import load_sqlite3_schema

Sqlgen_dir = os.path.dirname(load_sqlite3_schema.__file__)
Sqlite3_db = os.path.join(Sqlgen_dir, "sqlite3.db")

class cursor(object):
    rowcount = 1        # This is only check for unique queries...
    def __init__(self, width):
        self.width = width
    def execute(self, str, parameters=None):
        print("execute got:")
        print(str)
        if parameters: print("with:", parameters)
    def fetchone(self, base = 44):
        return (base,) * self.width
    def fetchall(self):
        return tuple(self.fetchone(i) for i in range(1, 5))

def init():
    test.init()
    with contextlib.closing(db.connect(Sqlite3_db)) as conn:
        load_sqlite3_schema.load_schema(test.Engine, db, conn)

def run_plan(globals, locals):
    plan = locals['plan']
    args = locals['args']
    starting_keys = dict(list(zip(args[0], list(range(1, len(args[0]) + 1)))))
    print("executing the plan with debug database cursor")
    ans = plan(cursor(len(args[1])), starting_keys)
    print("plan returned:", ans)
    while True:
        print()
        data_values = input("%s: " % str(args[0])).split()
        if not data_values: break
        starting_keys = dict(list(zip(args[0], data_values)))
        print("executing the plan with real database cursor")
        with contextlib.closing(db.connect(Sqlite3_db)) as conn:
            with contextlib.closing(conn.cursor()) as cur:
                ans = plan(cur, starting_keys)
        print("plan returned:", ans)

def run():
    if not test.Did_init: init()
    test.run('database', fn_to_run_plan = run_plan)

def doc_test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    doc_test()

