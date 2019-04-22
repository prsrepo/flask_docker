from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis://localhost:6379", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)


@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)


def calculate_formula():
    formula = "ab+be+ui+iopi-i908u"

    value = "ab+be+ui+iopi-i908u"

    result = {}

    name = ''

    start_index = 0

    reset_flag = False

    for index, _char in enumerate(formula):

        if reset_flag:
            start_index = index

        if _char not in ['(', ')', '*', '+', '-', '/']:
            name += _char
        else:
            import pdb;pdb.set_trace()

            value = value[:start_index] + '1' + value[index + 1:]

            reset_flag = True

    print(value)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

