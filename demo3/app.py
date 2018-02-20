import os
import sys
import traceback
import threading
import time
import signal

from flask import Flask, url_for


app = Flask(__name__)


def dumpstacks(signal, frame):
    """https://stackoverflow.com/a/2569696/209050"""
    id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
    code = []
    app.logger.error("Got signal to dump stacks. Your wish is my command.")
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId, ""),
                                            threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('  File "%s", line %d, in %s' % (filename, lineno,
                                                        name))
            if line:
                code.append("    %s" % (line.strip()))
    app.logger.error("\n".join(code))


@app.route("/")
def hello():
    time.sleep(30)
    return "hello, world!"


if __name__ == "__main__":
    print "Running with pid={}".format(os.getpid())
    signal.signal(signal.SIGUSR1, dumpstacks)
    app.run(debug=False, port=5003)
