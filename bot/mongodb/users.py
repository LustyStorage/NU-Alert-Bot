#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Prince Mendiratta
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pymongo import MongoClient
from bot import MONGO_URL
from bot import logging
import dns.resolver

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

# url, params = MONGO_URL.split("?")
# MONGO_URL = url + "?ssl=true&ssl_cert_reqs=CERT_NONE&" + params
client = MongoClient(MONGO_URL)


def add_client_to_db(chat_id, f_name, usname):
    # Add user to database
    mydb = client.dtu
    mycol = mydb.users
    chat_id = str(chat_id)
    mydict = {
        "Chat Id": "{}".format(chat_id),
        "First Name": "{}".format(f_name),
        "Username": "{}".format(usname),
    }
    mm = mydb.users.count_documents({"Chat Id": "{}".format(chat_id)})
    add_status = 0
    if mm == 0:
        mycol.insert_one(mydict)
        logging.info("[*] New user, {} added!".format(usname))
        add_status = 1
    else:
        add_status = 0
    total_users = len(mycol.distinct("Chat Id"))
    # client.close()
    return add_status, total_users


def user_list():
    mydb = client.dtu
    mycol = mydb.users
    broadcast_list = mycol.distinct("Chat Id")
    # client.close()
    return broadcast_list


def remove_client_from_db(chat_id):
    mydb = client.dtu
    mycol = mydb.users
    mycol.remove({"Chat Id": chat_id})
    print("[*] A user, {} has been deleted!".format(chat_id))
    # client.close()
