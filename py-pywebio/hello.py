from pywebio.input import input
from pywebio.output import put_text, put_file

def main():
    h = input("输入：", value="hello world")
    print(h)
    put_text(h)

if __name__ == '__main__':
    main()