
from pywebio import start_server, hold
from pywebio.output import put_text, output, put_scrollable
from pywebio.input import input, input_group


def outp(out, il):
    print("output")


    out.append("1234567")

    out.append("1234567yhgv")

    out.append(il["aaa"])


def index():
    print("run")
    put_text("12345")
    out = output()
    put_scrollable(out, keep_bottom=True)

    while True:
        il = input_group("233", [input(name="aaa", value="23456")])
        outp(out, il)



start_server(index, port=8899)