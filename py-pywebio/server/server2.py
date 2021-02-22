from pywebio import hold, go_app, start_server
from pywebio.output import put_text, put_buttons, put_link


def task_1():
    put_text('task_1')
    put_buttons(['Go task 2'], [lambda: go_app('task_2')])
    hold()


def task_2():
    put_text('task_2')
    put_buttons(['Go task 1', "233"], [lambda: go_app('task_1', False), lambda: put_text("233")])
    hold()


def index():
    put_link('Go task 1', app='task_1')  # 使用app参数指定任务名
    put_link('Go task 2', app='task_2')
    hold()


urls = [index, task_1, task_2]
start_server(urls, debug=True, port=8899, host="127.0.0.1")  # 或 start_server({'index': index, 'task_1': task_1, 'task_2': task_2})
