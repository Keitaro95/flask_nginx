import os

bind = '127.0.0.1:' + str(os.getenv('PORT', 9876))
proc_name = 'Infra-Practice-Flask'
workers = 1

