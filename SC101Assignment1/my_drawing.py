from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc
from campy.graphics.gwindow import GWindow


picachu_color = '#FFBC42'

def main():
    # 創建一個新視窗
    window = GWindow(width=600, height=400)
    backgroung = GRect(600, 400)
    backgroung.filled = True
    backgroung.fill_color = '#FAE8EB'
    backgroung.color = '#FAE8EB'
    window.add(backgroung)

    #皮卡丘
    # 畫耳朵
    left_ear = GOval(8, 45)
    left_ear.filled = True
    left_ear.fill_color = 'black'
    left_ear.color = 'black'
    window.add(left_ear, 274, 155)

    left_ear1 = GOval(10, 45)
    left_ear1.filled = True
    left_ear1.fill_color = picachu_color
    left_ear1.color = picachu_color
    window.add(left_ear1, 273, 160)

    right_ear = GOval(45, 8)
    right_ear.filled = True
    right_ear.fill_color = 'black'
    right_ear.color = 'black'
    window.add(right_ear, 283, 186)

    right_ear = GOval(45, 10)
    right_ear.filled = True
    right_ear.fill_color = picachu_color
    right_ear.color = picachu_color
    window.add(right_ear, 278, 185)

    # 畫頭
    head = GOval(50, 50)
    head.filled = True
    head.fill_color = picachu_color
    head.color = picachu_color
    window.add(head, 258, 175)

    # 畫身體
    body = GOval(50, 60)
    body.filled = True
    body.fill_color = picachu_color
    body.color = picachu_color
    window.add(body, 258, 210)

    # 繪製眼睛
    pupil = GOval(10, 10)
    pupil.filled = True
    pupil.fill_color = 'black'
    pupil.color = 'black'
    window.add(pupil, 263, 190)

    # 繪製眼珠
    eye = GOval(2, 3)
    eye.filled = True
    eye.fill_color = 'white'
    eye.color = 'white'
    window.add(eye, 263, 192)

    # 繪製鼻子
    nose = GOval(2, 1)
    nose.filled = True
    nose.fill_color = 'black'
    nose.color = 'black'
    window.add(nose, 257, 200)

    # 繪製嘴巴
    mouth = GArc(10, 5, 180, 100)
    mouth.color = 'black'
    window.add(mouth, 259, 203)

    # 繪製臉頰
    cheek = GOval(11, 11)
    cheek.filled = True
    cheek.fill_color = 'red'
    cheek.color = 'red'
    window.add(cheek, 268, 198)

    # 畫腳
    left_foot = GOval(30, 10)
    left_foot.filled = True
    left_foot.fill_color = picachu_color
    left_foot.color = picachu_color
    window.add(left_foot, 258, 260)

    right_foot = GOval(30, 10)
    right_foot.filled = True
    right_foot.fill_color = picachu_color
    right_foot.color = picachu_color
    window.add(right_foot, 248, 250)

    # 畫尾巴
    tail = GPolygon()
    tail.add_vertex((303, 253))
    tail.add_vertex((314, 245))
    tail.add_vertex((313, 235))
    tail.add_vertex((328, 232))
    tail.add_vertex((326, 220))
    tail.add_vertex((356, 210))
    tail.add_vertex((360, 232))
    tail.add_vertex((332, 235))
    tail.add_vertex((329, 246))
    tail.add_vertex((314, 249))
    tail.filled = True
    tail.fill_color = picachu_color
    tail.color = picachu_color
    window.add(tail)


if __name__ == '__main__':
    main()
