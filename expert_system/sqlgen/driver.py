# $Id: driver.py 6de8ee4e7d2d 2010-03-29 mtnyogi $
# coding=utf-8

import contextlib
from pyke import test
import load_mysql_schema


class cursor(object):
    rowcount = 1  # This is only check for unique queries...

    def __init__(self, width):
        self.width = width

    def execute(self, str, parameters=None):
        print("execute got:")
        print(str)
        if parameters: print("with:", parameters)

    def fetchone(self, base=44):
        return (base,) * self.width

    def fetchall(self):
        return tuple(self.fetchone(i) for i in range(1, 5))


def init():
    global db
    import MySQLdb as db
    test.init(__file__)
    with contextlib.closing(db.connect(host='192.168.138.134', user="root", passwd="root",
                                       db="movie_db")) \
            as conn:
        load_mysql_schema.load_schema(test.Engine, db, conn)


def run_plan(globals, locals):
    plan = locals['plan']
    args = locals['args']
    print(">> args:", args)
    print(">> args[0]", args[0])
    print(">> args[1]", args[1])
    print(">> len(args[0]):", len(args[0]))
    # starting_keys = dict(list(zip(args[0], list(range(1, len(args[0]) + 1)))))
    starting_keys = dict(list(zip(args[0], list(range(2, 3)))))
    print(">> starting_keys:", starting_keys)
    print("executing the plan with debug database cursor")
    ans = plan(cursor(len(args[1])), starting_keys)
    print("plan returned:", ans)
    while True:
        print()
        data_values = input("%s: " % str(args[0])).split()
        if not data_values: break
        starting_keys = dict(list(zip(args[0], data_values)))
        print("executing the plan with real database cursor2")
        with contextlib.closing(db.connect(user="movie_user",
                                           passwd="user_pw",
                                           db="movie_db")) \
                as conn:
            with contextlib.closing(conn.cursor()) as cur:
                ans = plan(cur, starting_keys)
        print("plan returned:", ans)


def run():
    if not test.Did_init: init()
    test.run('database', fn_to_run_plan=run_plan)


def doc_test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])


if __name__ == "__main__":
    # doc_test()
    init()
    run()
