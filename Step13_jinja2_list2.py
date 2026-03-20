#Step13_jinja2_list2.py

from jinja2 import Template

board_template = """
    {% for board in boards %}
    글번호 {{ board.id }} 작성자 {{ board["writer"] }} 제목 {{  board["title"] }}
    {% endfor %}
"""


# 게시글 목록이 담긴 리스트
posts: list = [
    {"id": 1, "writer": '작성자1','title':'제목1'},
    {"id": 2, "writer": '작성자2','title':'제목2'},
    {"id": 3, "writer": '작성자3','title':'제목3'}
]

temp:Template = Template(board_template)
result = temp.render(boards=posts)

print(' board result : ', result)

