#!/usr/bin/python

group_list = []
data = []

class User(object):
    name = ""
    gid = ""
    def __init__(self, name, gid):
        self.name = name
        self.gid = gid
    def __str__(self):
        return self.name

class Group(object):
    id = ""
    name = ""
    users = []
    def __init__(self, gid, name):
        self.name = name
        self.id = gid
    def __str__(self):
        return self.name

##### index functions
def index_groups(f, group_list):
    for line in f.readlines():
        name = line.split(":")[0]
        gid = line.split(":")[2]
        # print name, gid
        groups_list=group_list.append(Group(gid, name))
        # data.append(line.split(":")[0])
    #print_groups(groups)


def index_users(f,group_list):
    for line in f.readlines():
        name = line.split(":")[0]
        gid = line.split(":")[3]
        user = User(name,gid)
        group_list=insert_user_in_group(user,group_list)
    return group_list



def insert_user_in_group(user, group_list):
    for group in group_list:
        if group.id == user.gid:
            print user.name, " is in ", group.name
            group.users.append(user)
    return group_list


##### displaying func
def print_groups(group_list):
    for group in group_list:
        print group.name
        for user in group.users:
            print "|--", user

def print_users(group_list):
    for group in group_list:
        print group.users

#def print tree

##### Main

with open("/etc/group","r") as f:
    print "\n* GROUPS *"
    index_groups(f, group_list);
#print_groups(group_list)

with open("/etc/passwd","r") as f:
    print "\n* USERS *"
    index_users(f, group_list);
#print_groups(group_list)
