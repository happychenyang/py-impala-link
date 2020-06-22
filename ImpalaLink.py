#!/usr/bin/python
#-*- coding: utf-8 -*-
from impala.dbapi import connect

class ImpalaLink(object):
    """mysql数据库操作类"""

    def __init__(self, opts):
        self.conn = connect(
            host=opts['host'],
            port=opts['port'],
            user=opts.get('user', None),
            password=opts.get('password', None),
            database=opts.get('database', None),
            auth_mechanism=opts.get('auth_mechanism', 'NOSASL')
        )

    def execute(self, sql, args):
        """执行"""
        cursor = self.conn.cursor()
        if args and isinstance(args, list):
            cursor.executemany(sql, args)
        else:
            cursor.execute(sql, args)
        return cursor

    def insert(self, sql, args=None):
        """插入记录"""
        cursor = None
        try:
            cursor = self.execute(sql, args)
            row_id = cursor.lastrowid
            return row_id
        except:
            raise
        finally:
            cursor and cursor.close()

    def update(self, sql, args=None):
        """更新记录"""
        cursor = None
        try:
            cursor = self.execute(sql, args)
            row_count = cursor.rowcount
            if not row_count:
                return 0
            return row_count
        except:
            raise
        finally:
            cursor and cursor.close()

    def delete(self, sql, args=None):
        """删除记录"""
        cursor = None
        try:
            cursor = self.execute(sql, args)
            row_count = cursor.rowcount
            return row_count
        except:
            raise
        finally:
            cursor and cursor.close()

    def query(self, sql, args=None):
        """查询"""
        cursor = None
        try:
            cursor = self.execute(sql, args)
            return cursor.fetchall()
        except:
            raise
        finally:
            cursor and cursor.close()

    def query_one(self, sql, args=None):
        """查询返回一条数据"""
        cursor = None
        try:
            cursor = self.execute(sql, args)
            return cursor.fetchone()
        except:
            raise
        finally:
            cursor and cursor.close()