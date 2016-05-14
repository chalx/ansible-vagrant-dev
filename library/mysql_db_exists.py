#!/usr/bin/env python

try:
    import MySQLdb
except ImportError:
    mysqldb_found = False
else:
    mysqldb_found = True


def db_exists(cursor, db):
    res = cursor.execute("SHOW DATABASES LIKE %s", (db.replace("_", "\_"),))
    return bool(res)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            login_user=dict(default=None, aliases=['user']),
            login_password=dict(default=None, aliases=['password']),
            login_host=dict(default="localhost"),
            login_port=dict(default=3306),
            name=dict(required=True, aliases=['db'])
        )
    )

    if not mysqldb_found:
        module.fail_json(msg="the python mysqldb module is required")

    dbname = module.params['name']
    login_user = module.params['login_user']
    login_password = module.params['login_password']
    login_host = module.params["login_host"]
    login_port = module.params["login_port"]

    try:
        conn = MySQLdb.connect(host=login_host, user=login_user, passwd=login_password, port=login_port)
        cursor = conn.cursor()
        module.exit_json(exists=db_exists(cursor, dbname))
    except Exception, e:
        module.fail_json(
            msg="unable to connect to database, check login_user and login_password are correct. Exception message: %s" % e)


from ansible.module_utils.basic import *

if __name__ == "__main__":
    main()
