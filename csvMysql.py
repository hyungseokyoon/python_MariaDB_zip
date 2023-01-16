import pymysql
import os

def listdirs(base):
    repos_list = []
    for file in os.listdir(base):
        d = os.path.join(base, file)
        if os.path.isdir(d):
            repos_list.add(d)
    return repos_list

def listfiles(base):
    files_list = []
    for file in os.listdir(base):
        d = os.path.join(base, file)
        if not os.path.isdir(d):
            files_list.add(d)
    return files_list

# connection properties
conn = None
cur = None

sql = ""

#
conn = pymysql.connect(host="ec2-15-165-36-16.ap-northeast-2.compute.amazonaws.com", port=3306, user="yoon", password="yoon", db="sc_db")
curr = conn.cursor()

# sql = "show tables;"
# curr.execute(sql)

# insert data
base_dir = "/home/ubuntu/airflow/csv/"

# list all directories in base_dir
reposdir_list = listdirs(base_dir)

# get csv datas from reposdir
for repodir in reposdir_list:
    files_list = listfiles(repodir)
