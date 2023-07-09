"""
File: my_drawing.py
Name:溫孟哲
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow
WIDTH = 550
HEIGHT = 770
window = GWindow(WIDTH, HEIGHT)


def main():
    """
    A lion sleeps in the heart of every brave man. The days that break you are the days that make you.
    """
    background()
    lion()


def background():
    bg = GRect(WIDTH, HEIGHT)
    bg.filled = True
    bg.fill_color = 'black'
    window.add(bg)



def lion():

    green1 = GPolygon()
    green1.filled = True
    green1.fill_color = 'darkgreen'
    green1.add_vertex((550, 770))
    green1.add_vertex((460, 770))
    green1.add_vertex((527, 734))
    window.add(green1)

    green2 = GPolygon()
    green2.filled = True
    green2.fill_color = 'darkgreen'
    green2.add_vertex((514, 710))
    green2.add_vertex((460, 770))
    green2.add_vertex((527, 734))
    window.add(green2)

    green3 = GPolygon()
    green3.filled = True
    green3.fill_color = 'darkgreen'
    green3.add_vertex((460, 770))
    green3.add_vertex((514, 710))
    green3.add_vertex((493, 693))
    window.add(green3)

    green4 = GPolygon()
    green4.filled = True
    green4.fill_color = 'darkgreen'
    green4.add_vertex((460, 770))
    green4.add_vertex((404, 770))
    green4.add_vertex((435, 713))
    green4.add_vertex((450, 716))
    window.add(green4)

    green5 = GPolygon()
    green5.filled = True
    green5.fill_color = 'darkgreen'
    green5.add_vertex((404, 770))
    green5.add_vertex((342, 770))
    green5.add_vertex((385, 703))
    green5.add_vertex((410, 721))
    window.add(green5)

    green6 = GPolygon()
    green6.filled = True
    green6.fill_color = 'darkgreen'
    green6.add_vertex((342, 770))
    green6.add_vertex((308, 770))
    green6.add_vertex((362, 721))
    window.add(green6)

    green7 = GPolygon()
    green7.filled = True
    green7.fill_color = 'darkgreen'
    green7.add_vertex((308, 770))
    green7.add_vertex((269, 770))
    green7.add_vertex((309, 734))
    window.add(green7)

    green8 = GPolygon()
    green8.filled = True
    green8.fill_color = 'darkgreen'
    green8.add_vertex((269, 770))
    green8.add_vertex((206, 770))
    green8.add_vertex((232, 748))
    window.add(green8)

    green9 = GPolygon()
    green9.filled = True
    green9.fill_color = 'darkgreen'
    green9.add_vertex((206, 770))
    green9.add_vertex((191, 732))
    green9.add_vertex((175, 757))
    green9.add_vertex((146, 736))
    green9.add_vertex((128, 770))
    window.add(green9)

    green10 = GPolygon()
    green10.filled = True
    green10.fill_color = 'darkgreen'
    green10.add_vertex((128, 770))
    green10.add_vertex((86, 750))
    green10.add_vertex((84, 704))
    green10.add_vertex((108, 726))
    window.add(green10)

    green11 = GPolygon()
    green11.filled = True
    green11.fill_color = 'darkgreen'
    green11.add_vertex((128, 770))
    green11.add_vertex((40, 770))
    green11.add_vertex((84, 704))
    green11.add_vertex((86, 750))
    window.add(green11)

    green12 = GPolygon()
    green12.filled = True
    green12.fill_color = 'darkgreen'
    green12.add_vertex((40, 770))
    green12.add_vertex((0, 770))
    green12.add_vertex((0, 743))
    green12.add_vertex((47, 739))
    window.add(green12)

    green13 = GPolygon()
    green13.filled = True
    green13.fill_color = 'darkgreen'
    green13.add_vertex((0, 743))
    green13.add_vertex((47, 739))
    green13.add_vertex((55, 701))
    green13.add_vertex((0, 712))
    window.add(green13)

    green14 = GPolygon()
    green14.filled = True
    green14.fill_color = 'darkgreen'
    green14.add_vertex((0, 712))
    green14.add_vertex((0, 627))
    green14.add_vertex((17, 601))
    green14.add_vertex((23, 643))
    window.add(green14)

    green15 = GPolygon()
    green15.filled = True
    green15.fill_color = 'darkgreen'
    green15.add_vertex((550, 650))
    green15.add_vertex((530, 610))
    green15.add_vertex((531, 578))
    green15.add_vertex((550, 557))
    window.add(green15)

    green16 = GPolygon()
    green16.filled = True
    green16.fill_color = 'darkgreen'
    green16.add_vertex((550, 517))
    green16.add_vertex((514, 488))
    green16.add_vertex((523, 470))
    green16.add_vertex((550, 475))
    window.add(green16)

    green17 = GPolygon()
    green17.filled = True
    green17.fill_color = 'darkgreen'
    green17.add_vertex((550, 475))
    green17.add_vertex((550, 413))
    green17.add_vertex((527, 402))
    window.add(green17)

    green18 = GPolygon()
    green18.filled = True
    green18.fill_color = 'darkgreen'
    green18.add_vertex((550, 141))
    green18.add_vertex((533, 150))
    green18.add_vertex((512, 121))
    green18.add_vertex((550, 104))
    window.add(green18)

    green19 = GPolygon()
    green19.filled = True
    green19.fill_color = 'darkgreen'
    green19.add_vertex((550, 104))
    green19.add_vertex((514, 84))
    green19.add_vertex((550, 74))
    window.add(green19)

    green20 = GPolygon()
    green20.filled = True
    green20.fill_color = 'darkgreen'
    green20.add_vertex((550, 74))
    green20.add_vertex((505, 64))
    green20.add_vertex((550, 0))
    window.add(green20)

    green21 = GPolygon()
    green21.filled = True
    green21.fill_color = 'darkgreen'
    green21.add_vertex((550, 0))
    green21.add_vertex((505, 64))
    green21.add_vertex((507, 0))
    window.add(green21)

    green22 = GPolygon()
    green22.filled = True
    green22.fill_color = 'darkgreen'
    green22.add_vertex((505, 64))
    green22.add_vertex((507, 0))
    green22.add_vertex((466, 32))
    window.add(green22)

    green23 = GPolygon()
    green23.filled = True
    green23.fill_color = 'darkgreen'
    green23.add_vertex((507, 0))
    green23.add_vertex((466, 32))
    green23.add_vertex((430, 0))
    window.add(green23)

    green24 = GPolygon()
    green24.filled = True
    green24.fill_color = 'darkgreen'
    green24.add_vertex((430, 0))
    green24.add_vertex((466, 32))
    green24.add_vertex((480, 45))
    green24.add_vertex((412, 39))
    green24.add_vertex((383, 23))
    window.add(green24)

    green25 = GPolygon()
    green25.filled = True
    green25.fill_color = 'darkgreen'
    green25.add_vertex((355, 0))
    green25.add_vertex((319, 23))
    green25.add_vertex((234, 0))
    window.add(green25)

    green26 = GPolygon()
    green26.filled = True
    green26.fill_color = 'darkgreen'
    green26.add_vertex((172, 0))
    green26.add_vertex((199, 23))
    green26.add_vertex((234, 0))
    window.add(green26)

    green27 = GPolygon()
    green27.filled = True
    green27.fill_color = 'darkgreen'
    green27.add_vertex((172, 0))
    green27.add_vertex((160, 29))
    green27.add_vertex((117, 0))
    window.add(green27)

    green28 = GPolygon()
    green28.filled = True
    green28.fill_color = 'darkgreen'
    green28.add_vertex((117, 0))
    green28.add_vertex((139, 43))
    green28.add_vertex((0, 0))
    window.add(green28)

    green29 = GPolygon()
    green29.filled = True
    green29.fill_color = 'darkgreen'
    green29.add_vertex((0, 0))
    green29.add_vertex((52, 57))
    green29.add_vertex((0, 67))
    window.add(green29)

    green30 = GPolygon()
    green30.filled = True
    green30.fill_color = 'darkgreen'
    green30.add_vertex((0, 67))
    green30.add_vertex((38, 80))
    green30.add_vertex((0, 120))
    window.add(green30)

    green31 = GPolygon()
    green31.filled = True
    green31.fill_color = 'darkgreen'
    green31.add_vertex((0, 120))
    green31.add_vertex((46, 116))
    green31.add_vertex((0, 157))
    window.add(green31)

    green32 = GPolygon()
    green32.filled = True
    green32.fill_color = 'darkgreen'
    green32.add_vertex((0, 547))
    green32.add_vertex((35, 455))
    green32.add_vertex((0, 456))
    window.add(green32)

    green33 = GPolygon()
    green33.filled = True
    green33.fill_color = 'darkgreen'
    green33.add_vertex((0, 456))
    green33.add_vertex((0, 404))
    green33.add_vertex((50, 359))
    window.add(green33)

    green34 = GPolygon()
    green34.filled = True
    green34.fill_color = 'darkgreen'
    green34.add_vertex((0, 353))
    green34.add_vertex((0, 306))
    green34.add_vertex((46, 301))
    window.add(green34)

    green35 = GPolygon()
    green35.filled = True
    green35.fill_color = 'darkgreen'
    green35.add_vertex((0, 0))
    green35.add_vertex((53, 57))
    green35.add_vertex((87, 27))
    window.add(green35)

    green36 = GPolygon()
    green36.filled = True
    green36.fill_color = 'darkgreen'
    green36.add_vertex((0, 306))
    green36.add_vertex((0, 270))
    green36.add_vertex((57, 240))
    window.add(green36)




    yellow1 = GPolygon()
    yellow1.filled = True
    yellow1.fill_color = 'gold'
    yellow1.add_vertex((550, 770))
    yellow1.add_vertex((514, 710))
    yellow1.add_vertex((550, 710))
    window.add(yellow1)

    yellow2 = GPolygon()
    yellow2.filled = True
    yellow2.fill_color = 'gold'
    yellow2.add_vertex((550, 710))
    yellow2.add_vertex((514, 710))
    yellow2.add_vertex((550, 650))
    window.add(yellow2)

    yellow3 = GPolygon()
    yellow3.filled = True
    yellow3.fill_color = 'gold'
    yellow3.add_vertex((550, 650))
    yellow3.add_vertex((514, 710))
    yellow3.add_vertex((493, 693))
    yellow3.add_vertex((504, 667))
    window.add(yellow3)

    yellow4 = GPolygon()
    yellow4.filled = True
    yellow4.fill_color = 'gold'
    yellow4.add_vertex((493, 693))
    yellow4.add_vertex((460, 770))
    yellow4.add_vertex((450, 716))
    yellow4.add_vertex((435, 713))
    window.add(yellow4)

    yellow5 = GPolygon()
    yellow5.filled = True
    yellow5.fill_color = 'gold'
    yellow5.add_vertex((435, 713))
    yellow5.add_vertex((404, 770))
    yellow5.add_vertex((410, 721))
    yellow5.add_vertex((385, 703))
    window.add(yellow5)

    yellow6 = GPolygon()
    yellow6.filled = True
    yellow6.fill_color = 'gold'
    yellow6.add_vertex((385, 703))
    yellow6.add_vertex((342, 770))
    yellow6.add_vertex((362, 721))
    yellow6.add_vertex((345, 694))
    window.add(yellow6)

    yellow7 = GPolygon()
    yellow7.filled = True
    yellow7.fill_color = 'gold'
    yellow7.add_vertex((362, 721))
    yellow7.add_vertex((345, 694))
    yellow7.add_vertex((324, 681))
    yellow7.add_vertex((338, 742))
    window.add(yellow7)

    yellow8 = GPolygon()
    yellow8.filled = True
    yellow8.fill_color = 'gold'
    yellow8.add_vertex((324, 681))
    yellow8.add_vertex((338, 742))
    yellow8.add_vertex((310, 770))
    yellow8.add_vertex((308, 707))
    window.add(yellow8)

    yellow9 = GPolygon()
    yellow9.filled = True
    yellow9.fill_color = 'gold'
    yellow9.add_vertex((308, 707))
    yellow9.add_vertex((309, 734))
    yellow9.add_vertex((269, 770))
    yellow9.add_vertex((297, 673))
    window.add(yellow9)

    yellow10 = GPolygon()
    yellow10.filled = True
    yellow10.fill_color = 'gold'
    yellow10.add_vertex((265, 716))
    yellow10.add_vertex((269, 770))
    yellow10.add_vertex((232, 748))
    yellow10.add_vertex((241, 725))
    yellow10.add_vertex((254, 680))
    window.add(yellow10)

    yellow11 = GPolygon()
    yellow11.filled = True
    yellow11.fill_color = 'gold'
    yellow11.add_vertex((241, 725))
    yellow11.add_vertex((232, 748))
    yellow11.add_vertex((206, 770))
    yellow11.add_vertex((219, 699))
    window.add(yellow11)

    yellow12 = GPolygon()
    yellow12.filled = True
    yellow12.fill_color = 'gold'
    yellow12.add_vertex((219, 699))
    yellow12.add_vertex((206, 770))
    yellow12.add_vertex((191, 732))
    yellow12.add_vertex((195, 708))
    window.add(yellow12)

    yellow13 = GPolygon()
    yellow13.filled = True
    yellow13.fill_color = 'gold'
    yellow13.add_vertex((195, 708))
    yellow13.add_vertex((191, 732))
    yellow13.add_vertex((175, 757))
    yellow13.add_vertex((146, 736))
    yellow13.add_vertex((155, 700))
    yellow13.add_vertex((176, 667))
    yellow13.add_vertex((180, 628))
    yellow13.add_vertex((188, 653))
    window.add(yellow13)

    yellow14 = GPolygon()
    yellow14.filled = True
    yellow14.fill_color = 'gold'
    yellow14.add_vertex((155, 700))
    yellow14.add_vertex((146, 736))
    yellow14.add_vertex((121, 702))
    yellow14.add_vertex((129, 647))
    window.add(yellow14)

    yellow15 = GPolygon()
    yellow15.filled = True
    yellow15.fill_color = 'gold'
    yellow15.add_vertex((121, 702))
    yellow15.add_vertex((146, 736))
    yellow15.add_vertex((128, 770))
    yellow15.add_vertex((108, 726))
    window.add(yellow15)

    yellow16 = GPolygon()
    yellow16.filled = True
    yellow16.fill_color = 'gold'
    yellow16.add_vertex((121, 702))
    yellow16.add_vertex((108, 726))
    yellow16.add_vertex((84, 704))
    yellow16.add_vertex((95, 685))
    yellow16.add_vertex((129, 647))
    window.add(yellow16)

    yellow17 = GPolygon()
    yellow17.filled = True
    yellow17.fill_color = 'gold'
    yellow17.add_vertex((84, 704))
    yellow17.add_vertex((40, 770))
    yellow17.add_vertex((55, 701))
    yellow17.add_vertex((77, 687))
    window.add(yellow17)

    yellow18 = GPolygon()
    yellow18.filled = True
    yellow18.fill_color = 'gold'
    yellow18.add_vertex((77, 687))
    yellow18.add_vertex((55, 701))
    yellow18.add_vertex((48, 630))
    yellow18.add_vertex((62, 606))
    window.add(yellow18)

    yellow19 = GPolygon()
    yellow19.filled = True
    yellow19.fill_color = 'gold'
    yellow19.add_vertex((48, 630))
    yellow19.add_vertex((55, 701))
    yellow19.add_vertex((0, 712))
    yellow19.add_vertex((23, 643))
    window.add(yellow19)

    yellow20 = GPolygon()
    yellow20.filled = True
    yellow20.fill_color = 'gold'
    yellow20.add_vertex((550, 650))
    yellow20.add_vertex((504, 667))
    yellow20.add_vertex((528, 632))
    yellow20.add_vertex((530, 610))
    window.add(yellow20)

    yellow21 = GPolygon()
    yellow21.filled = True
    yellow21.fill_color = 'gold'
    yellow21.add_vertex((504, 667))
    yellow21.add_vertex((528, 632))
    yellow21.add_vertex((530, 610))
    yellow21.add_vertex((531, 578))
    yellow21.add_vertex((515, 598))
    window.add(yellow21)

    yellow22 = GPolygon()
    yellow22.filled = True
    yellow22.fill_color = 'gold'
    yellow22.add_vertex((480, 601))
    yellow22.add_vertex((504, 667))
    yellow22.add_vertex((458, 654))
    window.add(yellow22)

    yellow23 = GPolygon()
    yellow23.filled = True
    yellow23.fill_color = 'gold'
    yellow23.add_vertex((458, 654))
    yellow23.add_vertex((504, 667))
    yellow23.add_vertex((493, 693))
    yellow23.add_vertex((475, 700))
    window.add(yellow23)

    yellow24 = GPolygon()
    yellow24.filled = True
    yellow24.fill_color = 'gold'
    yellow24.add_vertex((458, 654))
    yellow24.add_vertex((475, 700))
    yellow24.add_vertex((435, 713))
    window.add(yellow24)

    yellow25 = GPolygon()
    yellow25.filled = True
    yellow25.fill_color = 'gold'
    yellow25.add_vertex((458, 654))
    yellow25.add_vertex((435, 713))
    yellow25.add_vertex((435, 563))
    window.add(yellow25)

    yellow26 = GPolygon()
    yellow26.filled = True
    yellow26.fill_color = 'gold'
    yellow26.add_vertex((435, 713))
    yellow26.add_vertex((410, 674))
    yellow26.add_vertex((385, 703))
    window.add(yellow26)

    yellow27 = GPolygon()
    yellow27.filled = True
    yellow27.fill_color = 'gold'
    yellow27.add_vertex((385, 665))
    yellow27.add_vertex((385, 703))
    yellow27.add_vertex((345, 694))
    yellow27.add_vertex((383, 633))
    window.add(yellow27)

    yellow28 = GPolygon()
    yellow28.filled = True
    yellow28.fill_color = 'gold'
    yellow28.add_vertex((43, 570))
    yellow28.add_vertex((48, 630))
    yellow28.add_vertex((23, 643))
    yellow28.add_vertex((17, 601))
    window.add(yellow28)

    yellow29 = GPolygon()
    yellow29.filled = True
    yellow29.fill_color = 'gold'
    yellow29.add_vertex((43, 570))
    yellow29.add_vertex((17, 601))
    yellow29.add_vertex((0, 627))
    yellow29.add_vertex((0, 547))
    yellow29.add_vertex((60, 547))
    window.add(yellow29)

    yellow30 = GPolygon()
    yellow30.filled = True
    yellow30.fill_color = 'gold'
    yellow30.add_vertex((515, 598))
    yellow30.add_vertex((480, 601))
    yellow30.add_vertex((496, 555))
    window.add(yellow30)

    yellow31 = GPolygon()
    yellow31.filled = True
    yellow31.fill_color = 'gold'
    yellow31.add_vertex((515, 598))
    yellow31.add_vertex((496, 555))
    yellow31.add_vertex((485, 511))
    yellow31.add_vertex((510, 521))
    window.add(yellow31)

    yellow32 = GPolygon()
    yellow32.filled = True
    yellow32.fill_color = 'gold'
    yellow32.add_vertex((480, 601))
    yellow32.add_vertex((496, 555))
    yellow32.add_vertex((485, 511))
    yellow32.add_vertex((478, 546))
    window.add(yellow32)

    yellow33 = GPolygon()
    yellow33.filled = True
    yellow33.fill_color = 'gold'
    yellow33.add_vertex((550, 557))
    yellow33.add_vertex((530, 540))
    yellow33.add_vertex((514, 488))
    yellow33.add_vertex((550, 517))
    window.add(yellow33)

    yellow34 = GPolygon()
    yellow34.filled = True
    yellow34.fill_color = 'gold'
    yellow34.add_vertex((550, 413))
    yellow34.add_vertex((527, 402))
    yellow34.add_vertex((550, 359))
    window.add(yellow34)

    yellow35 = GPolygon()
    yellow35.filled = True
    yellow35.fill_color = 'gold'
    yellow35.add_vertex((527, 402))
    yellow35.add_vertex((550, 359))
    yellow35.add_vertex((523, 374))
    yellow35.add_vertex((491, 361))
    window.add(yellow35)

    yellow36 = GPolygon()
    yellow36.filled = True
    yellow36.fill_color = 'gold'
    yellow36.add_vertex((527, 402))
    yellow36.add_vertex((491, 361))
    yellow36.add_vertex((500, 403))
    yellow36.add_vertex((530, 427))
    yellow36.add_vertex((550, 475))
    window.add(yellow36)

    yellow37 = GPolygon()
    yellow37.filled = True
    yellow37.fill_color = 'gold'
    yellow37.add_vertex((523, 374))
    yellow37.add_vertex((550, 359))
    yellow37.add_vertex((530, 312))
    window.add(yellow37)

    yellow38 = GPolygon()
    yellow38.filled = True
    yellow38.fill_color = 'gold'
    yellow38.add_vertex((550, 244))
    yellow38.add_vertex((535, 245))
    yellow38.add_vertex((527, 187))
    yellow38.add_vertex((550, 185))
    window.add(yellow38)

    yellow39 = GPolygon()
    yellow39.filled = True
    yellow39.fill_color = 'gold'
    yellow39.add_vertex((550, 185))
    yellow39.add_vertex((527, 187))
    yellow39.add_vertex((533, 150))
    yellow39.add_vertex((550, 141))
    window.add(yellow39)

    yellow40 = GPolygon()
    yellow40.filled = True
    yellow40.fill_color = 'gold'
    yellow40.add_vertex((454, 333))
    yellow40.add_vertex((459, 355))
    yellow40.add_vertex((435, 346))
    yellow40.add_vertex((433, 300))
    window.add(yellow40)

    yellow41 = GPolygon()
    yellow41.filled = True
    yellow41.fill_color = 'gold'
    yellow41.add_vertex((459, 355))
    yellow41.add_vertex((435, 346))
    yellow41.add_vertex((436, 381))
    yellow41.add_vertex((465, 425))
    yellow41.add_vertex((477, 446))
    window.add(yellow41)

    yellow42 = GPolygon()
    yellow42.filled = True
    yellow42.fill_color = 'gold'
    yellow42.add_vertex((436, 381))
    yellow42.add_vertex((465, 425))
    yellow42.add_vertex((437, 437))
    window.add(yellow42)

    yellow43 = GPolygon()
    yellow43.filled = True
    yellow43.fill_color = 'gold'
    yellow43.add_vertex((465, 425))
    yellow43.add_vertex((437, 437))
    yellow43.add_vertex((470, 471))
    yellow43.add_vertex((477, 446))
    window.add(yellow43)

    yellow44 = GPolygon()
    yellow44.filled = True
    yellow44.fill_color = 'gold'
    yellow44.add_vertex((523, 374))
    yellow44.add_vertex((530, 312))
    yellow44.add_vertex((487, 323))
    yellow44.add_vertex((501, 330))
    window.add(yellow44)

    yellow45 = GPolygon()
    yellow45.filled = True
    yellow45.fill_color = 'gold'
    yellow45.add_vertex((430, 0))
    yellow45.add_vertex((383, 23))
    yellow45.add_vertex((319, 23))
    yellow45.add_vertex((355, 0))
    window.add(yellow45)

    yellow46 = GPolygon()
    yellow46.filled = True
    yellow46.fill_color = 'gold'
    yellow46.add_vertex((487, 323))
    yellow46.add_vertex((530, 312))
    yellow46.add_vertex((480, 278))
    yellow46.add_vertex((477, 304))
    window.add(yellow46)

    yellow47 = GPolygon()
    yellow47.filled = True
    yellow47.fill_color = 'gold'
    yellow47.add_vertex((480, 278))
    yellow47.add_vertex((530, 312))
    yellow47.add_vertex((522, 290))
    yellow47.add_vertex((487, 245))
    window.add(yellow47)

    yellow48 = GPolygon()
    yellow48.filled = True
    yellow48.fill_color = 'gold'
    yellow48.add_vertex((487, 245))
    yellow48.add_vertex((477, 304))
    yellow48.add_vertex((453, 257))
    yellow48.add_vertex((455, 237))
    window.add(yellow48)

    yellow49 = GPolygon()
    yellow49.filled = True
    yellow49.fill_color = 'gold'
    yellow49.add_vertex((455, 237))
    yellow49.add_vertex((487, 245))
    yellow49.add_vertex((511, 249))
    yellow49.add_vertex((481, 210))
    yellow49.add_vertex((455, 204))
    window.add(yellow49)

    yellow50 = GPolygon()
    yellow50.filled = True
    yellow50.fill_color = 'gold'
    yellow50.add_vertex((533, 148))
    yellow50.add_vertex((513, 151))
    yellow50.add_vertex((496, 148))
    yellow50.add_vertex((514, 120))
    window.add(yellow50)

    yellow51 = GPolygon()
    yellow51.filled = True
    yellow51.fill_color = 'gold'
    yellow51.add_vertex((550, 74))
    yellow51.add_vertex((505, 64))
    yellow51.add_vertex((480, 46))
    yellow51.add_vertex((478, 95))
    window.add(yellow51)

    yellow52 = GPolygon()
    yellow52.filled = True
    yellow52.fill_color = 'gold'
    yellow52.add_vertex((479, 67))
    yellow52.add_vertex((444, 59))
    yellow52.add_vertex((412, 39))
    yellow52.add_vertex((480, 45))
    window.add(yellow52)

    yellow53 = GPolygon()
    yellow53.filled = True
    yellow53.fill_color = 'gold'
    yellow53.add_vertex((478, 95))
    yellow53.add_vertex((479, 67))
    yellow53.add_vertex((444, 59))
    yellow53.add_vertex((427, 80))
    window.add(yellow53)

    yellow54 = GPolygon()
    yellow54.filled = True
    yellow54.fill_color = 'gold'
    yellow54.add_vertex((0, 547))
    yellow54.add_vertex((60, 547))
    yellow54.add_vertex((78, 526))
    yellow54.add_vertex((78, 512))
    window.add(yellow54)

    yellow55 = GPolygon()
    yellow55.filled = True
    yellow55.fill_color = 'gold'
    yellow55.add_vertex((0, 547))
    yellow55.add_vertex((78, 512))
    yellow55.add_vertex((42, 506))
    yellow55.add_vertex((26, 476))
    window.add(yellow55)

    yellow56 = GPolygon()
    yellow56.filled = True
    yellow56.fill_color = 'gold'
    yellow56.add_vertex((78, 512))
    yellow56.add_vertex((42, 506))
    yellow56.add_vertex((35, 493))
    yellow56.add_vertex((60, 479))
    window.add(yellow56)

    yellow57 = GPolygon()
    yellow57.filled = True
    yellow57.fill_color = 'gold'
    yellow57.add_vertex((60, 479))
    yellow57.add_vertex((78, 512))
    yellow57.add_vertex((82, 475))
    yellow57.add_vertex((78, 467))
    window.add(yellow57)

    yellow58 = GPolygon()
    yellow58.filled = True
    yellow58.fill_color = 'gold'
    yellow58.add_vertex((35, 493))
    yellow58.add_vertex((60, 479))
    yellow58.add_vertex((35, 455))
    yellow58.add_vertex((26, 476))
    window.add(yellow58)

    yellow59 = GPolygon()
    yellow59.filled = True
    yellow59.fill_color = 'gold'
    yellow59.add_vertex((60, 479))
    yellow59.add_vertex((35, 455))
    yellow59.add_vertex((72, 455))
    yellow59.add_vertex((78, 467))
    window.add(yellow59)

    yellow60 = GPolygon()
    yellow60.filled = True
    yellow60.fill_color = 'gold'
    yellow60.add_vertex((72, 455))
    yellow60.add_vertex((23, 412))
    yellow60.add_vertex((0, 456))
    window.add(yellow60)

    yellow61 = GPolygon()
    yellow61.filled = True
    yellow61.fill_color = 'gold'
    yellow61.add_vertex((72, 455))
    yellow61.add_vertex((23, 412))
    yellow61.add_vertex((60, 406))
    window.add(yellow61)

    yellow62 = GPolygon()
    yellow62.filled = True
    yellow62.fill_color = 'gold'
    yellow62.add_vertex((23, 412))
    yellow62.add_vertex((60, 406))
    yellow62.add_vertex((50, 359))
    window.add(yellow62)

    yellow63 = GPolygon()
    yellow63.filled = True
    yellow63.fill_color = 'gold'
    yellow63.add_vertex((50, 359))
    yellow63.add_vertex((0, 404))
    yellow63.add_vertex((0, 353))
    yellow63.add_vertex((14, 338))
    window.add(yellow63)

    yellow64 = GPolygon()
    yellow64.filled = True
    yellow64.fill_color = 'gold'
    yellow64.add_vertex((50, 359))
    yellow64.add_vertex((14, 338))
    yellow64.add_vertex((46, 301))
    yellow64.add_vertex((65, 298))
    window.add(yellow64)

    yellow65 = GPolygon()
    yellow65.filled = True
    yellow65.fill_color = 'gold'
    yellow65.add_vertex((50, 359))
    yellow65.add_vertex((72, 455))
    yellow65.add_vertex((72, 394))
    yellow65.add_vertex((100, 331))
    window.add(yellow65)

    yellow66 = GPolygon()
    yellow66.filled = True
    yellow66.fill_color = 'gold'
    yellow66.add_vertex((50, 359))
    yellow66.add_vertex((100, 331))
    yellow66.add_vertex((65, 298))
    window.add(yellow66)

    yellow67 = GPolygon()
    yellow67.filled = True
    yellow67.fill_color = 'gold'
    yellow67.add_vertex((65, 298))
    yellow67.add_vertex((0, 306))
    yellow67.add_vertex((28, 274))
    yellow67.add_vertex((78, 250))
    window.add(yellow67)

    yellow68 = GPolygon()
    yellow68.filled = True
    yellow68.fill_color = 'gold'
    yellow68.add_vertex((28, 274))
    yellow68.add_vertex((78, 250))
    yellow68.add_vertex((100, 223))
    yellow68.add_vertex((57, 240))
    window.add(yellow68)

    yellow69 = GPolygon()
    yellow69.filled = True
    yellow69.fill_color = 'gold'
    yellow69.add_vertex((0, 270))
    yellow69.add_vertex((57, 240))
    yellow69.add_vertex((50, 200))
    yellow69.add_vertex((0, 244))
    window.add(yellow69)

    yellow70 = GPolygon()
    yellow70.filled = True
    yellow70.fill_color = 'gold'
    yellow70.add_vertex((57, 240))
    yellow70.add_vertex((50, 200))
    yellow70.add_vertex((92, 173))
    window.add(yellow70)

    yellow71 = GPolygon()
    yellow71.filled = True
    yellow71.fill_color = 'gold'
    yellow71.add_vertex((57, 240))
    yellow71.add_vertex((92, 173))
    yellow71.add_vertex((143, 167))
    yellow71.add_vertex((100, 223))
    window.add(yellow71)

    yellow72 = GPolygon()
    yellow72.filled = True
    yellow72.fill_color = 'gold'
    yellow72.add_vertex((0, 202))
    yellow72.add_vertex((39, 165))
    yellow72.add_vertex((46, 116))
    yellow72.add_vertex((0, 157))
    window.add(yellow72)

    yellow73 = GPolygon()
    yellow73.filled = True
    yellow73.fill_color = 'gold'
    yellow73.add_vertex((39, 165))
    yellow73.add_vertex((46, 116))
    yellow73.add_vertex((72, 99))
    yellow73.add_vertex((94, 135))
    window.add(yellow73)

    yellow74 = GPolygon()
    yellow74.filled = True
    yellow74.fill_color = 'gold'
    yellow74.add_vertex((46, 116))
    yellow74.add_vertex((72, 99))
    yellow74.add_vertex((38, 80))
    yellow74.add_vertex((0, 120))
    window.add(yellow74)

    yellow75 = GPolygon()
    yellow75.filled = True
    yellow75.fill_color = 'gold'
    yellow75.add_vertex((0, 67))
    yellow75.add_vertex((38, 80))
    yellow75.add_vertex((57, 67))
    yellow75.add_vertex((52, 57))
    window.add(yellow75)

    yellow76 = GPolygon()
    yellow76.filled = True
    yellow76.fill_color = 'gold'
    yellow76.add_vertex((57, 67))
    yellow76.add_vertex((52, 57))
    yellow76.add_vertex((88, 27))
    yellow76.add_vertex((132, 90))
    window.add(yellow76)

    yellow77 = GPolygon()
    yellow77.filled = True
    yellow77.fill_color = 'gold'
    yellow77.add_vertex((88, 27))
    yellow77.add_vertex((132, 90))
    yellow77.add_vertex((173, 63))
    yellow77.add_vertex((137, 41))
    window.add(yellow77)

    yellow78 = GPolygon()
    yellow78.filled = True
    yellow78.fill_color = 'gold'
    yellow78.add_vertex((132, 90))
    yellow78.add_vertex((173, 63))
    yellow78.add_vertex((213, 83))
    yellow78.add_vertex((189, 96))
    window.add(yellow78)

    yellow79 = GPolygon()
    yellow79.filled = True
    yellow79.fill_color = 'gold'
    yellow79.add_vertex((173, 63))
    yellow79.add_vertex((213, 83))
    yellow79.add_vertex((160, 29))
    yellow79.add_vertex((117, 0))
    yellow79.add_vertex((139, 43))
    window.add(yellow79)

    yellow80 = GPolygon()
    yellow80.filled = True
    yellow80.fill_color = 'gold'
    yellow80.add_vertex((160, 29))
    yellow80.add_vertex((172, 0))
    yellow80.add_vertex((199, 23))
    yellow80.add_vertex((263, 38))
    yellow80.add_vertex((206, 50))
    window.add(yellow80)

    yellow81 = GPolygon()
    yellow81.filled = True
    yellow81.fill_color = 'gold'
    yellow81.add_vertex((199, 23))
    yellow81.add_vertex((263, 38))
    yellow81.add_vertex((262, 8))
    yellow81.add_vertex((234, 0))
    window.add(yellow81)

    yellow82 = GPolygon()
    yellow82.filled = True
    yellow82.fill_color = 'gold'
    yellow82.add_vertex((263, 38))
    yellow82.add_vertex((262, 8))
    yellow82.add_vertex((319, 23))
    yellow82.add_vertex((296, 44))
    window.add(yellow82)

    yellow83 = GPolygon()
    yellow83.filled = True
    yellow83.fill_color = 'gold'
    yellow83.add_vertex((319, 23))
    yellow83.add_vertex((296, 44))
    yellow83.add_vertex((350, 48))
    yellow83.add_vertex((383, 23))
    window.add(yellow83)

    yellow84 = GPolygon()
    yellow84.filled = True
    yellow84.fill_color = 'gold'
    yellow84.add_vertex((350, 48))
    yellow84.add_vertex((383, 23))
    yellow84.add_vertex((412, 39))
    yellow84.add_vertex((394, 48))
    window.add(yellow84)

    yellow85 = GPolygon()
    yellow85.filled = True
    yellow85.fill_color = 'gold'
    yellow85.add_vertex((412, 39))
    yellow85.add_vertex((394, 48))
    yellow85.add_vertex((403, 67))
    yellow85.add_vertex((444, 59))
    window.add(yellow85)

    yellow86 = GPolygon()
    yellow86.filled = True
    yellow86.fill_color = 'gold'
    yellow86.add_vertex((403, 67))
    yellow86.add_vertex((444, 59))
    yellow86.add_vertex((427, 80))
    yellow86.add_vertex((388, 99))
    window.add(yellow86)

    yellow87 = GPolygon()
    yellow87.filled = True
    yellow87.fill_color = 'gold'
    yellow87.add_vertex((354, 80))
    yellow87.add_vertex((388, 99))
    yellow87.add_vertex((403, 67))
    window.add(yellow87)

    yellow88 = GPolygon()
    yellow88.filled = True
    yellow88.fill_color = 'gold'
    yellow88.add_vertex((354, 80))
    yellow88.add_vertex((388, 99))
    yellow88.add_vertex((380, 119))
    yellow88.add_vertex((335, 114))
    window.add(yellow88)

    yellow89 = GPolygon()
    yellow89.filled = True
    yellow89.fill_color = 'gold'
    yellow89.add_vertex((380, 119))
    yellow89.add_vertex((335, 114))
    yellow89.add_vertex((343, 144))
    yellow89.add_vertex((373, 136))
    window.add(yellow89)

    yellow89 = GPolygon()
    yellow89.filled = True
    yellow89.fill_color = 'gold'
    yellow89.add_vertex((306, 148))
    yellow89.add_vertex((335, 114))
    yellow89.add_vertex((343, 144))
    window.add(yellow89)

    yellow90 = GPolygon()
    yellow90.filled = True
    yellow90.fill_color = 'gold'
    yellow90.add_vertex((306, 148))
    yellow90.add_vertex((335, 114))
    yellow90.add_vertex((307, 87))
    window.add(yellow90)

    yellow91 = GPolygon()
    yellow91.filled = True
    yellow91.fill_color = 'gold'
    yellow91.add_vertex((306, 148))
    yellow91.add_vertex((282, 122))
    yellow91.add_vertex((307, 87))
    window.add(yellow91)

    yellow92 = GPolygon()
    yellow92.filled = True
    yellow92.fill_color = 'gold'
    yellow92.add_vertex((306, 148))
    yellow92.add_vertex((282, 122))
    yellow92.add_vertex((255, 164))
    window.add(yellow92)

    yellow93 = GPolygon()
    yellow93.filled = True
    yellow93.fill_color = 'gold'
    yellow93.add_vertex((282, 122))
    yellow93.add_vertex((271, 87))
    yellow93.add_vertex((239, 144))
    yellow93.add_vertex((270, 141))
    window.add(yellow93)

    yellow94 = GPolygon()
    yellow94.filled = True
    yellow94.fill_color = 'gold'
    yellow94.add_vertex((271, 87))
    yellow94.add_vertex((239, 144))
    yellow94.add_vertex((234, 111))
    yellow94.add_vertex((246, 85))
    window.add(yellow94)

    yellow95 = GPolygon()
    yellow95.filled = True
    yellow95.fill_color = 'gold'
    yellow95.add_vertex((234, 111))
    yellow95.add_vertex((246, 85))
    yellow95.add_vertex((213, 83))
    yellow95.add_vertex((190, 95))
    yellow95.add_vertex((184, 114))
    window.add(yellow95)

    yellow96 = GPolygon()
    yellow96.filled = True
    yellow96.fill_color = 'gold'
    yellow96.add_vertex((234, 111))
    yellow96.add_vertex((184, 114))
    yellow96.add_vertex((205, 131))
    yellow96.add_vertex((193, 177))
    yellow96.add_vertex((216, 149))
    window.add(yellow96)

    yellow97 = GPolygon()
    yellow97.filled = True
    yellow97.fill_color = 'gold'
    yellow97.add_vertex((395, 149))
    yellow97.add_vertex((390, 174))
    yellow97.add_vertex((408, 212))
    yellow97.add_vertex((419, 172))
    window.add(yellow97)

    yellow98 = GPolygon()
    yellow98.filled = True
    yellow98.fill_color = 'gold'
    yellow98.add_vertex((408, 212))
    yellow98.add_vertex((419, 172))
    yellow98.add_vertex((444, 185))
    yellow98.add_vertex((452, 205))
    window.add(yellow98)

    yellow99 = GPolygon()
    yellow99.filled = True
    yellow99.fill_color = 'gold'
    yellow99.add_vertex((77, 552))
    yellow99.add_vertex((112, 552))
    yellow99.add_vertex((118, 525))
    yellow99.add_vertex((103, 503))
    window.add(yellow99)

    yellow100 = GPolygon()
    yellow100.filled = True
    yellow100.fill_color = 'gold'
    yellow100.add_vertex((215, 512))
    yellow100.add_vertex((245, 533))
    yellow100.add_vertex((268, 511))
    yellow100.add_vertex((295, 530))
    yellow100.add_vertex((324, 512))
    window.add(yellow100)

    yellow101 = GPolygon()
    yellow101.filled = True
    yellow101.fill_color = 'gold'
    yellow101.add_vertex((162, 445))
    yellow101.add_vertex((199, 393))
    yellow101.add_vertex((195, 350))
    yellow101.add_vertex((153, 410))
    window.add(yellow101)

    yellow102 = GPolygon()
    yellow102.filled = True
    yellow102.fill_color = 'gold'
    yellow102.add_vertex((145, 421))
    yellow102.add_vertex((103, 373))
    yellow102.add_vertex((123, 365))
    window.add(yellow102)

    yellow103 = GPolygon()
    yellow103.filled = True
    yellow103.fill_color = 'gold'
    yellow103.add_vertex((153, 338))
    yellow103.add_vertex((156, 360))
    yellow103.add_vertex((195, 350))
    yellow103.add_vertex((203, 310))
    window.add(yellow103)

    yellow104 = GPolygon()
    yellow104.filled = True
    yellow104.fill_color = 'gold'
    yellow104.add_vertex((153, 338))
    yellow104.add_vertex((203, 310))
    yellow104.add_vertex((163, 310))
    yellow104.add_vertex((131, 338))
    window.add(yellow104)

    yellow105 = GPolygon()
    yellow105.filled = True
    yellow105.fill_color = 'gold'
    yellow105.add_vertex((163, 310))
    yellow105.add_vertex((131, 338))
    yellow105.add_vertex((133, 315))
    yellow105.add_vertex((143, 283))
    window.add(yellow105)

    yellow106 = GPolygon()
    yellow106.filled = True
    yellow106.fill_color = 'gold'
    yellow106.add_vertex((133, 315))
    yellow106.add_vertex((143, 283))
    yellow106.add_vertex((113, 275))
    yellow106.add_vertex((112, 302))
    window.add(yellow106)

    yellow107 = GPolygon()
    yellow107.filled = True
    yellow107.fill_color = 'gold'
    yellow107.add_vertex((113, 275))
    yellow107.add_vertex((65, 298))
    yellow107.add_vertex((112, 258))
    yellow107.add_vertex((145, 233))
    window.add(yellow107)

    yellow108 = GPolygon()
    yellow108.filled = True
    yellow108.fill_color = 'gold'
    yellow108.add_vertex((195, 350))
    yellow108.add_vertex((201, 407))
    yellow108.add_vertex((221, 332))
    yellow108.add_vertex((219, 318))
    yellow108.add_vertex((203, 310))
    window.add(yellow108)

    yellow109 = GPolygon()
    yellow109.filled = True
    yellow109.fill_color = 'gold'
    yellow109.add_vertex((216, 393))
    yellow109.add_vertex((226, 384))
    yellow109.add_vertex((239, 371))
    yellow109.add_vertex((259, 380))
    yellow109.add_vertex((262, 398))
    window.add(yellow109)

    yellow110 = GPolygon()
    yellow110.filled = True
    yellow110.fill_color = 'gold'
    yellow110.add_vertex((226, 384))
    yellow110.add_vertex((239, 371))
    yellow110.add_vertex((257, 354))
    yellow110.add_vertex((258, 320))
    yellow110.add_vertex((219, 318))
    window.add(yellow110)

    yellow111 = GPolygon()
    yellow111.filled = True
    yellow111.fill_color = 'gold'
    yellow111.add_vertex((262, 398))
    yellow111.add_vertex((290, 373))
    yellow111.add_vertex((331, 397))
    window.add(yellow111)

    yellow112 = GPolygon()
    yellow112.filled = True
    yellow112.fill_color = 'gold'
    yellow112.add_vertex((219, 318))
    yellow112.add_vertex((258, 320))
    yellow112.add_vertex((276, 320))
    yellow112.add_vertex((225, 262))
    window.add(yellow112)

    yellow113 = GPolygon()
    yellow113.filled = True
    yellow113.fill_color = 'gold'
    yellow113.add_vertex((172, 227))
    yellow113.add_vertex((200, 240))
    yellow113.add_vertex((211, 222))
    yellow113.add_vertex((199, 205))
    window.add(yellow113)

    yellow114 = GPolygon()
    yellow114.filled = True
    yellow114.fill_color = 'gold'
    yellow114.add_vertex((200, 240))
    yellow114.add_vertex((211, 222))
    yellow114.add_vertex((231, 226))
    yellow114.add_vertex((225, 262))
    window.add(yellow114)

    yellow115 = GPolygon()
    yellow115.filled = True
    yellow115.fill_color = 'gold'
    yellow115.add_vertex((199, 205))
    yellow115.add_vertex((211, 222))
    yellow115.add_vertex((231, 226))
    yellow115.add_vertex((225, 190))
    window.add(yellow115)

    yellow116 = GPolygon()
    yellow116.filled = True
    yellow116.fill_color = 'gold'
    yellow116.add_vertex((225, 190))
    yellow116.add_vertex((256, 163))
    yellow116.add_vertex((255, 193))
    yellow116.add_vertex((225, 190))
    window.add(yellow116)

    yellow117 = GPolygon()
    yellow117.filled = True
    yellow117.fill_color = 'gold'
    yellow117.add_vertex((274, 318))
    yellow117.add_vertex((314, 284))
    yellow117.add_vertex((297, 272))
    yellow117.add_vertex((281, 280))
    window.add(yellow117)

    yellow118 = GPolygon()
    yellow118.filled = True
    yellow118.fill_color = 'gold'
    yellow118.add_vertex((257, 241))
    yellow118.add_vertex((243, 281))
    yellow118.add_vertex((225, 262))
    yellow118.add_vertex((231, 226))
    window.add(yellow118)




    red1 = GPolygon()
    red1.filled = True
    red1.fill_color = 'darkred'
    red1.add_vertex((504, 667))
    red1.add_vertex((515, 598))
    red1.add_vertex((480, 601))
    window.add(red1)

    red2 = GPolygon()
    red2.filled = True
    red2.fill_color = 'darkred'
    red2.add_vertex((458, 654))
    red2.add_vertex((435, 563))
    red2.add_vertex((480, 601))
    window.add(red2)

    red3 = GPolygon()
    red3.filled = True
    red3.fill_color = 'darkred'
    red3.add_vertex((435, 563))
    red3.add_vertex((435, 648))
    red3.add_vertex((410, 606))
    red3.add_vertex((407, 539))
    window.add(red3)

    red4 = GPolygon()
    red4.filled = True
    red4.fill_color = 'darkred'
    red4.add_vertex((383, 633))
    red4.add_vertex((339, 630))
    red4.add_vertex((363, 586))
    red4.add_vertex((385, 605))
    window.add(red4)

    red5 = GPolygon()
    red5.filled = True
    red5.fill_color = 'darkred'
    red5.add_vertex((363, 586))
    red5.add_vertex((339, 630))
    red5.add_vertex((334, 570))
    red5.add_vertex((350, 547))
    window.add(red5)

    red6 = GPolygon()
    red6.filled = True
    red6.fill_color = 'darkred'
    red6.add_vertex((314, 652))
    red6.add_vertex((254, 680))
    red6.add_vertex((298, 620))
    window.add(red6)

    red7 = GPolygon()
    red7.filled = True
    red7.fill_color = 'darkred'
    red7.add_vertex((314, 652))
    red7.add_vertex((254, 680))
    red7.add_vertex((265, 716))
    red7.add_vertex((297, 673))
    window.add(red7)

    red8 = GPolygon()
    red8.filled = True
    red8.fill_color = 'darkred'
    red8.add_vertex((254, 680))
    red8.add_vertex((220, 659))
    red8.add_vertex((241, 725))
    window.add(red8)

    red9 = GPolygon()
    red9.filled = True
    red9.fill_color = 'darkred'
    red9.add_vertex((254, 680))
    red9.add_vertex((220, 659))
    red9.add_vertex((250, 647))
    red9.add_vertex((267, 623))
    window.add(red9)

    red10 = GPolygon()
    red10.filled = True
    red10.fill_color = 'darkred'
    red10.add_vertex((220, 659))
    red10.add_vertex((250, 647))
    red10.add_vertex((238, 618))
    window.add(red10)

    red11 = GPolygon()
    red11.filled = True
    red11.fill_color = 'darkred'
    red11.add_vertex((220, 659))
    red11.add_vertex((241, 725))
    red11.add_vertex((219, 699))
    red11.add_vertex((195, 708))
    red11.add_vertex((209, 630))
    window.add(red11)

    red12 = GPolygon()
    red12.filled = True
    red12.fill_color = 'darkred'
    red12.add_vertex((209, 630))
    red12.add_vertex((195, 708))
    red12.add_vertex((188, 653))
    red12.add_vertex((180, 628))
    red12.add_vertex((218, 598))
    window.add(red12)

    red13 = GPolygon()
    red13.filled = True
    red13.fill_color = 'darkred'
    red13.add_vertex((180, 628))
    red13.add_vertex((163, 603))
    red13.add_vertex((187, 570))
    red13.add_vertex((200, 566))
    window.add(red13)

    red14 = GPolygon()
    red14.filled = True
    red14.fill_color = 'darkred'
    red14.add_vertex((187, 570))
    red14.add_vertex((163, 603))
    red14.add_vertex((129, 647))
    red14.add_vertex((147, 570))
    red14.add_vertex((197, 528))
    window.add(red14)

    red15 = GPolygon()
    red15.filled = True
    red15.fill_color = 'darkred'
    red15.add_vertex((147, 570))
    red15.add_vertex((129, 647))
    red15.add_vertex((110, 575))
    red15.add_vertex((145, 517))
    window.add(red15)

    red16 = GPolygon()
    red16.filled = True
    red16.fill_color = 'darkred'
    red16.add_vertex((110, 575))
    red16.add_vertex((129, 647))
    red16.add_vertex((95, 685))
    window.add(red16)

    red17 = GPolygon()
    red17.filled = True
    red17.fill_color = 'darkred'
    red17.add_vertex((218, 598))
    red17.add_vertex((200, 566))
    red17.add_vertex((225, 555))
    red17.add_vertex((249, 578))
    window.add(red17)

    red18 = GPolygon()
    red18.filled = True
    red18.fill_color = 'darkred'
    red18.add_vertex((84, 574))
    red18.add_vertex((77, 512))
    red18.add_vertex((71, 535))
    red18.add_vertex((43, 570))
    red18.add_vertex((48, 630))
    window.add(red18)

    red19 = GPolygon()
    red19.filled = True
    red19.fill_color = 'darkred'
    red19.add_vertex((550, 557))
    red19.add_vertex((531, 578))
    red19.add_vertex((515, 598))
    red19.add_vertex((510, 521))
    red19.add_vertex((530, 540))
    window.add(red19)

    red20 = GPolygon()
    red20.filled = True
    red20.fill_color = 'darkred'
    red20.add_vertex((478, 546))
    red20.add_vertex((480, 601))
    red20.add_vertex((435, 563))
    red20.add_vertex((457, 530))
    window.add(red20)

    red21 = GPolygon()
    red21.filled = True
    red21.fill_color = 'darkred'
    red21.add_vertex((457, 530))
    red21.add_vertex((435, 563))
    red21.add_vertex((423, 497))
    window.add(red21)

    red22 = GPolygon()
    red22.filled = True
    red22.fill_color = 'darkred'
    red22.add_vertex((478, 546))
    red22.add_vertex((457, 530))
    red22.add_vertex((423, 497))
    red22.add_vertex((470, 471))
    red22.add_vertex((456, 502))
    window.add(red22)

    red23 = GPolygon()
    red23.filled = True
    red23.fill_color = 'darkred'
    red23.add_vertex((423, 497))
    red23.add_vertex((470, 471))
    red23.add_vertex((437, 437))
    window.add(red23)

    red24 = GPolygon()
    red24.filled = True
    red24.fill_color = 'darkred'
    red24.add_vertex((514, 488))
    red24.add_vertex((523, 470))
    red24.add_vertex((530, 429))
    red24.add_vertex((495, 473))
    window.add(red24)

    red25 = GPolygon()
    red25.filled = True
    red25.fill_color = 'darkred'
    red25.add_vertex((530, 429))
    red25.add_vertex((514, 488))
    red25.add_vertex((550, 475))
    window.add(red25)

    red26 = GPolygon()
    red26.filled = True
    red26.fill_color = 'darkred'
    red26.add_vertex((550, 359))
    red26.add_vertex((530, 312))
    red26.add_vertex((522, 290))
    red26.add_vertex((550, 244))
    window.add(red26)

    red27 = GPolygon()
    red27.filled = True
    red27.fill_color = 'darkred'
    red27.add_vertex((522, 290))
    red27.add_vertex((550, 244))
    red27.add_vertex((535, 245))
    red27.add_vertex((510, 249))
    red27.add_vertex((486, 244))
    window.add(red27)

    red28 = GPolygon()
    red28.filled = True
    red28.fill_color = 'darkred'
    red28.add_vertex((495, 473))
    red28.add_vertex((530, 429))
    red28.add_vertex((469, 408))
    red28.add_vertex((477, 446))
    window.add(red28)

    red29 = GPolygon()
    red29.filled = True
    red29.fill_color = 'darkred'
    red29.add_vertex((457, 334))
    red29.add_vertex((489, 360))
    red29.add_vertex((460, 308))
    red29.add_vertex((447, 291))
    red29.add_vertex((432, 300))
    window.add(red29)

    red30 = GPolygon()
    red30.filled = True
    red30.fill_color = 'darkred'
    red30.add_vertex((481, 210))
    red30.add_vertex((490, 184))
    red30.add_vertex((444, 185))
    red30.add_vertex((452, 205))
    window.add(red30)

    red31 = GPolygon()
    red31.filled = True
    red31.fill_color = 'darkred'
    red31.add_vertex((490, 184))
    red31.add_vertex((513, 151))
    red31.add_vertex((496, 148))
    red31.add_vertex((474, 155))
    window.add(red31)

    red32 = GPolygon()
    red32.filled = True
    red32.fill_color = 'darkred'
    red32.add_vertex((490, 184))
    red32.add_vertex((474, 155))
    red32.add_vertex((459, 159))
    red32.add_vertex((444, 185))
    window.add(red32)

    red33 = GPolygon()
    red33.filled = True
    red33.fill_color = 'darkred'
    red33.add_vertex((459, 159))
    red33.add_vertex((444, 185))
    red33.add_vertex((394, 158))
    red33.add_vertex((395, 149))
    window.add(red33)

    red34 = GPolygon()
    red34.filled = True
    red34.fill_color = 'darkred'
    red34.add_vertex((425, 112))
    red34.add_vertex((480, 121))
    red34.add_vertex((513, 83))
    window.add(red34)

    red35 = GPolygon()
    red35.filled = True
    red35.fill_color = 'darkred'
    red35.add_vertex((145, 517))
    red35.add_vertex((147, 570))
    red35.add_vertex((197, 528))
    red35.add_vertex((215, 512))
    red35.add_vertex((182, 512))
    red35.add_vertex((145, 470))
    window.add(red35)

    red36 = GPolygon()
    red36.filled = True
    red36.fill_color = 'darkred'
    red36.add_vertex((145, 470))
    red36.add_vertex((123, 470))
    red36.add_vertex((121, 498))
    red36.add_vertex((145, 518))
    window.add(red36)

    red37 = GPolygon()
    red37.filled = True
    red37.fill_color = 'darkred'
    red37.add_vertex((0, 244))
    red37.add_vertex((50, 200))
    red37.add_vertex((16, 190))
    red37.add_vertex((0, 202))
    window.add(red37)

    red38 = GPolygon()
    red38.filled = True
    red38.fill_color = 'darkred'
    red38.add_vertex((50, 200))
    red38.add_vertex((16, 190))
    red38.add_vertex((39, 165))
    red38.add_vertex((92, 173))
    window.add(red38)

    red39 = GPolygon()
    red39.filled = True
    red39.fill_color = 'darkred'
    red39.add_vertex((263, 38))
    red39.add_vertex((244, 56))
    red39.add_vertex((288, 74))
    red39.add_vertex((331, 46))
    window.add(red39)

    red40 = GPolygon()
    red40.filled = True
    red40.fill_color = 'darkred'
    red40.add_vertex((92, 173))
    red40.add_vertex((107, 156))
    red40.add_vertex((130, 130))
    red40.add_vertex((205, 131))
    red40.add_vertex((147, 165))
    window.add(red40)

    red41 = GPolygon()
    red41.filled = True
    red41.fill_color = 'darkred'
    red41.add_vertex((130, 130))
    red41.add_vertex((205, 131))
    red41.add_vertex((184, 114))
    red41.add_vertex((190, 95))
    window.add(red41)

    red42 = GPolygon()
    red42.filled = True
    red42.fill_color = 'darkred'
    red42.add_vertex((130, 130))
    red42.add_vertex((190, 95))
    red42.add_vertex((132, 90))
    window.add(red42)

    red43 = GPolygon()
    red43.filled = True
    red43.fill_color = 'darkred'
    red43.add_vertex((130, 130))
    red43.add_vertex((132, 90))
    red43.add_vertex((89, 78))
    red43.add_vertex((103, 115))
    window.add(red43)

    red44 = GPolygon()
    red44.filled = True
    red44.fill_color = 'darkred'
    red44.add_vertex((161, 169))
    red44.add_vertex((144, 205))
    red44.add_vertex((193, 177))
    window.add(red44)

    red45 = GPolygon()
    red45.filled = True
    red45.fill_color = 'darkred'
    red45.add_vertex((123, 470))
    red45.add_vertex((72, 455))
    red45.add_vertex((145, 421))
    window.add(red45)

    red46 = GPolygon()
    red46.filled = True
    red46.fill_color = 'darkred'
    red46.add_vertex((72, 455))
    red46.add_vertex((145, 421))
    red46.add_vertex((72, 394))
    window.add(red46)

    red47 = GPolygon()
    red47.filled = True
    red47.fill_color = 'darkred'
    red47.add_vertex((145, 421))
    red47.add_vertex((72, 394))
    red47.add_vertex((100, 331))
    red47.add_vertex((103, 373))
    window.add(red47)

    red48 = GPolygon()
    red48.filled = True
    red48.fill_color = 'darkred'
    red48.add_vertex((319, 428))
    red48.add_vertex((327, 450))
    red48.add_vertex((366, 456))
    red48.add_vertex((311, 471))
    window.add(red48)

    red49 = GPolygon()
    red49.filled = True
    red49.fill_color = 'darkred'
    red49.add_vertex((123, 365))
    red49.add_vertex((170, 388))
    red49.add_vertex((195, 350))
    red49.add_vertex((156, 360))
    window.add(red49)

    red50 = GPolygon()
    red50.filled = True
    red50.fill_color = 'darkred'
    red50.add_vertex((258, 320))
    red50.add_vertex((280, 334))
    red50.add_vertex((286, 358))
    red50.add_vertex((306, 359))
    red50.add_vertex((323, 310))
    window.add(red50)

    red51 = GPolygon()
    red51.filled = True
    red51.fill_color = 'darkred'
    red51.add_vertex((323, 310))
    red51.add_vertex((306, 359))
    red51.add_vertex((329, 368))
    red51.add_vertex((351, 376))
    window.add(red51)

    red52 = GPolygon()
    red52.filled = True
    red52.fill_color = 'darkred'
    red52.add_vertex((329, 368))
    red52.add_vertex((351, 376))
    red52.add_vertex((374, 422))
    red52.add_vertex((355, 411))
    red52.add_vertex((331, 397))
    window.add(red52)

    red53 = GPolygon()
    red53.filled = True
    red53.fill_color = 'darkred'
    red53.add_vertex((323, 310))
    red53.add_vertex((351, 376))
    red53.add_vertex((374, 392))
    red53.add_vertex((377, 360))
    red53.add_vertex((356, 340))
    window.add(red53)

    red54 = GPolygon()
    red54.filled = True
    red54.fill_color = 'darkred'
    red54.add_vertex((374, 392))
    red54.add_vertex((377, 360))
    red54.add_vertex((414, 350))
    red54.add_vertex((402, 370))
    window.add(red54)

    red55 = GPolygon()
    red55.filled = True
    red55.fill_color = 'darkred'
    red55.add_vertex((374, 392))
    red55.add_vertex((402, 370))
    red55.add_vertex((411, 381))
    red55.add_vertex((392, 413))
    window.add(red55)

    red56 = GPolygon()
    red56.filled = True
    red56.fill_color = 'darkred'
    red56.add_vertex((411, 381))
    red56.add_vertex((392, 413))
    red56.add_vertex((393, 460))
    red56.add_vertex((421, 405))
    window.add(red56)

    red57 = GPolygon()
    red57.filled = True
    red57.fill_color = 'darkred'
    red57.add_vertex((411, 381))
    red57.add_vertex((421, 405))
    red57.add_vertex((436, 379))
    red57.add_vertex((436, 346))
    window.add(red57)

    red58 = GPolygon()
    red58.filled = True
    red58.fill_color = 'darkred'
    red58.add_vertex((377, 360))
    red58.add_vertex((414, 350))
    red58.add_vertex((414, 328))
    red58.add_vertex((393, 324))
    window.add(red58)

    red59 = GPolygon()
    red59.filled = True
    red59.fill_color = 'darkred'
    red59.add_vertex((414, 328))
    red59.add_vertex((393, 324))
    red59.add_vertex((412, 291))
    red59.add_vertex((422, 303))
    window.add(red59)

    red60 = GPolygon()
    red60.filled = True
    red60.fill_color = 'darkred'
    red60.add_vertex((404, 277))
    red60.add_vertex((383, 297))
    red60.add_vertex((356, 314))
    red60.add_vertex((323, 310))
    window.add(red60)

    red61 = GPolygon()
    red61.filled = True
    red61.fill_color = 'darkred'
    red61.add_vertex((274, 318))
    red61.add_vertex((323, 310))
    red61.add_vertex((314, 284))
    window.add(red61)

    red62 = GPolygon()
    red62.filled = True
    red62.fill_color = 'darkred'
    red62.add_vertex((323, 310))
    red62.add_vertex((314, 284))
    red62.add_vertex((332, 257))
    red62.add_vertex((335, 271))
    window.add(red62)

    red63 = GPolygon()
    red63.filled = True
    red63.fill_color = 'darkred'
    red63.add_vertex((447, 291))
    red63.add_vertex((432, 300))
    red63.add_vertex((421, 304))
    red63.add_vertex((423, 276))
    red63.add_vertex((438, 226))
    window.add(red63)

    red64 = GPolygon()
    red64.filled = True
    red64.fill_color = 'darkred'
    red64.add_vertex((423, 276))
    red64.add_vertex((438, 226))
    red64.add_vertex((408, 212))
    red64.add_vertex((408, 244))
    window.add(red64)

    red65 = GPolygon()
    red65.filled = True
    red65.fill_color = 'darkred'
    red65.add_vertex((408, 212))
    red65.add_vertex((390, 174))
    red65.add_vertex((371, 175))
    red65.add_vertex((377, 199))
    window.add(red65)

    red66 = GPolygon()
    red66.filled = True
    red66.fill_color = 'darkred'
    red66.add_vertex((404, 277))
    red66.add_vertex((403, 248))
    red66.add_vertex((387, 236))
    red66.add_vertex((382, 263))
    window.add(red66)

    red67 = GPolygon()
    red67.filled = True
    red67.fill_color = 'darkred'
    red67.add_vertex((387, 236))
    red67.add_vertex((382, 263))
    red67.add_vertex((373, 255))
    red67.add_vertex((362, 247))
    red67.add_vertex((371, 234))
    window.add(red67)

    red68 = GPolygon()
    red68.filled = True
    red68.fill_color = 'darkred'
    red68.add_vertex((387, 236))
    red68.add_vertex((371, 234))
    red68.add_vertex((363, 211))
    red68.add_vertex((384, 223))
    window.add(red68)

    red69 = GPolygon()
    red69.filled = True
    red69.fill_color = 'darkred'
    red69.add_vertex((371, 234))
    red69.add_vertex((362, 247))
    red69.add_vertex((332, 257))
    red69.add_vertex((351, 222))
    window.add(red69)

    red70 = GPolygon()
    red70.filled = True
    red70.fill_color = 'darkred'
    red70.add_vertex((270, 178))
    red70.add_vertex((255, 191))
    red70.add_vertex((267, 228))
    red70.add_vertex((278, 240))
    red70.add_vertex((280, 208))
    window.add(red70)

    red71 = GPolygon()
    red71.filled = True
    red71.fill_color = 'darkred'
    red71.add_vertex((255, 191))
    red71.add_vertex((267, 228))
    red71.add_vertex((267, 272))
    red71.add_vertex((247, 212))
    window.add(red71)







    orange1 = GPolygon()
    orange1.filled = True
    orange1.fill_color = 'chocolate'
    orange1.add_vertex((269, 770))
    orange1.add_vertex((265, 716))
    orange1.add_vertex((297, 673))
    window.add(orange1)

    orange2 = GPolygon()
    orange2.filled = True
    orange2.fill_color = 'chocolate'
    orange2.add_vertex((435, 713))
    orange2.add_vertex((410, 674))
    orange2.add_vertex((410, 606))
    orange2.add_vertex((435, 648))
    window.add(orange2)

    orange3 = GPolygon()
    orange3.filled = True
    orange3.fill_color = 'chocolate'
    orange3.add_vertex((410, 606))
    orange3.add_vertex((410, 674))
    orange3.add_vertex((385, 703))
    orange3.add_vertex((385, 665))
    window.add(orange3)

    orange4 = GPolygon()
    orange4.filled = True
    orange4.fill_color = 'chocolate'
    orange4.add_vertex((383, 633))
    orange4.add_vertex((345, 694))
    orange4.add_vertex((339, 630))
    window.add(orange4)

    orange4 = GPolygon()
    orange4.filled = True
    orange4.fill_color = 'chocolate'
    orange4.add_vertex((345, 694))
    orange4.add_vertex((324, 681))
    orange4.add_vertex((314, 652))
    orange4.add_vertex((342, 664))
    window.add(orange4)

    orange6 = GPolygon()
    orange6.filled = True
    orange6.fill_color = 'chocolate'
    orange6.add_vertex((342, 664))
    orange6.add_vertex((314, 652))
    orange6.add_vertex((337, 603))
    window.add(orange6)

    orange7 = GPolygon()
    orange7.filled = True
    orange7.fill_color = 'chocolate'
    orange7.add_vertex((297, 673))
    orange7.add_vertex((314, 652))
    orange7.add_vertex((324, 681))
    orange7.add_vertex((308, 707))
    window.add(orange7)

    orange8 = GPolygon()
    orange8.filled = True
    orange8.fill_color = 'chocolate'
    orange8.add_vertex((180, 628))
    orange8.add_vertex((176, 667))
    orange8.add_vertex((155, 700))
    orange8.add_vertex((163, 603))
    window.add(orange8)

    orange9 = GPolygon()
    orange9.filled = True
    orange9.fill_color = 'chocolate'
    orange9.add_vertex((155, 700))
    orange9.add_vertex((163, 603))
    orange9.add_vertex((129, 647))
    window.add(orange9)

    orange10 = GPolygon()
    orange10.filled = True
    orange10.fill_color = 'chocolate'
    orange10.add_vertex((110, 575))
    orange10.add_vertex((95, 685))
    orange10.add_vertex((94, 625))
    orange10.add_vertex((93, 587))
    orange10.add_vertex((84, 574))
    orange10.add_vertex((77, 552))
    orange10.add_vertex((112, 552))
    window.add(orange10)

    orange11 = GPolygon()
    orange11.filled = True
    orange11.fill_color = 'chocolate'
    orange11.add_vertex((95, 630))
    orange11.add_vertex((94, 625))
    orange11.add_vertex((93, 587))
    orange11.add_vertex((84, 574))
    orange11.add_vertex((62, 606))
    orange11.add_vertex((72, 657))
    window.add(orange11)

    orange12 = GPolygon()
    orange12.filled = True
    orange12.fill_color = 'chocolate'
    orange12.add_vertex((95, 630))
    orange12.add_vertex((72, 657))
    orange12.add_vertex((77, 687))
    orange12.add_vertex((84, 704))
    orange12.add_vertex((95, 685))
    window.add(orange12)

    orange13 = GPolygon()
    orange13.filled = True
    orange13.fill_color = 'chocolate'
    orange13.add_vertex((530, 540))
    orange13.add_vertex((514, 488))
    orange13.add_vertex((495, 473))
    orange13.add_vertex((485, 511))
    orange13.add_vertex((510, 521))
    window.add(orange13)

    orange14 = GPolygon()
    orange14.filled = True
    orange14.fill_color = 'chocolate'
    orange14.add_vertex((485, 511))
    orange14.add_vertex((495, 473))
    orange14.add_vertex((477, 446))
    orange14.add_vertex((470, 471))
    window.add(orange14)

    orange15 = GPolygon()
    orange15.filled = True
    orange15.fill_color = 'chocolate'
    orange15.add_vertex((485, 511))
    orange15.add_vertex((470, 471))
    orange15.add_vertex((456, 502))
    orange15.add_vertex((478, 546))
    window.add(orange15)

    orange16 = GPolygon()
    orange16.filled = True
    orange16.fill_color = 'chocolate'
    orange16.add_vertex((550, 104))
    orange16.add_vertex((512, 121))
    orange16.add_vertex((514, 84))
    window.add(orange16)

    orange17 = GPolygon()
    orange17.filled = True
    orange17.fill_color = 'chocolate'
    orange17.add_vertex((469, 408))
    orange17.add_vertex((530, 429))
    orange17.add_vertex((500, 403))
    orange17.add_vertex((490, 361))
    window.add(orange17)

    orange18 = GPolygon()
    orange18.filled = True
    orange18.fill_color = 'chocolate'
    orange18.add_vertex((469, 408))
    orange18.add_vertex((490, 361))
    orange18.add_vertex((454, 333))
    window.add(orange18)

    orange19 = GPolygon()
    orange19.filled = True
    orange19.fill_color = 'chocolate'
    orange19.add_vertex((523, 374))
    orange19.add_vertex((501, 330))
    orange19.add_vertex((487, 323))
    orange19.add_vertex((460, 308))
    orange19.add_vertex((490, 361))
    window.add(orange19)

    orange20 = GPolygon()
    orange20.filled = True
    orange20.fill_color = 'chocolate'
    orange20.add_vertex((460, 308))
    orange20.add_vertex((487, 323))
    orange20.add_vertex((438, 230))
    orange20.add_vertex((447, 291))
    window.add(orange20)

    orange21 = GPolygon()
    orange21.filled = True
    orange21.fill_color = 'chocolate'
    orange21.add_vertex((499, 232))
    orange21.add_vertex((511, 249))
    orange21.add_vertex((535, 246))
    orange21.add_vertex((526, 186))
    window.add(orange21)

    orange22 = GPolygon()
    orange22.filled = True
    orange22.fill_color = 'chocolate'
    orange22.add_vertex((481, 210))
    orange22.add_vertex((500, 232))
    orange22.add_vertex((526, 186))
    orange22.add_vertex((490, 184))
    window.add(orange22)

    orange23 = GPolygon()
    orange23.filled = True
    orange23.fill_color = 'chocolate'
    orange23.add_vertex((526, 186))
    orange23.add_vertex((490, 184))
    orange23.add_vertex((513, 151))
    orange23.add_vertex((533, 148))
    window.add(orange23)

    orange24 = GPolygon()
    orange24.filled = True
    orange24.fill_color = 'chocolate'
    orange24.add_vertex((496, 148))
    orange24.add_vertex((514, 120))
    orange24.add_vertex((513, 83))
    orange24.add_vertex((480, 121))
    window.add(orange24)

    orange25 = GPolygon()
    orange25.filled = True
    orange25.fill_color = 'chocolate'
    orange25.add_vertex((496, 148))
    orange25.add_vertex((480, 121))
    orange25.add_vertex((423, 154))
    orange25.add_vertex((459, 159))
    window.add(orange25)

    orange26 = GPolygon()
    orange26.filled = True
    orange26.fill_color = 'chocolate'
    orange26.add_vertex((423, 154))
    orange26.add_vertex((480, 121))
    orange26.add_vertex((425, 112))
    orange26.add_vertex((395, 149))
    window.add(orange26)

    orange27 = GPolygon()
    orange27.filled = True
    orange27.fill_color = 'chocolate'
    orange27.add_vertex((395, 149))
    orange27.add_vertex((373, 136))
    orange27.add_vertex((308, 148))
    orange27.add_vertex((343, 175))
    orange27.add_vertex((390, 174))
    orange27.add_vertex((394, 158))
    window.add(orange27)

    orange28 = GPolygon()
    orange28.filled = True
    orange28.fill_color = 'chocolate'
    orange28.add_vertex((39, 165))
    orange28.add_vertex((92, 173))
    orange28.add_vertex((107, 156))
    orange28.add_vertex((94, 135))
    window.add(orange28)

    orange29 = GPolygon()
    orange29.filled = True
    orange29.fill_color = 'chocolate'
    orange29.add_vertex((107, 156))
    orange29.add_vertex((94, 135))
    orange29.add_vertex((72, 99))
    orange29.add_vertex((130, 130))
    window.add(orange29)

    orange30 = GPolygon()
    orange30.filled = True
    orange30.fill_color = 'chocolate'
    orange30.add_vertex((57, 67))
    orange30.add_vertex((38, 80))
    orange30.add_vertex((72, 99))
    orange30.add_vertex((103, 115))
    orange30.add_vertex((89, 78))
    window.add(orange30)

    orange31 = GPolygon()
    orange31.filled = True
    orange31.fill_color = 'chocolate'
    orange31.add_vertex((160, 29))
    orange31.add_vertex((206, 50))
    orange31.add_vertex((263, 38))
    orange31.add_vertex((213, 83))
    window.add(orange31)

    orange32 = GPolygon()
    orange32.filled = True
    orange32.fill_color = 'chocolate'
    orange32.add_vertex((213, 83))
    orange32.add_vertex((244, 56))
    orange32.add_vertex((288, 74))
    orange32.add_vertex((271, 87))
    window.add(orange32)

    orange33 = GPolygon()
    orange33.filled = True
    orange33.fill_color = 'chocolate'
    orange33.add_vertex((288, 74))
    orange33.add_vertex((271, 87))
    orange33.add_vertex((282, 122))
    orange33.add_vertex((307, 87))
    window.add(orange33)

    orange34 = GPolygon()
    orange34.filled = True
    orange34.fill_color = 'chocolate'
    orange34.add_vertex((288, 74))
    orange34.add_vertex((307, 87))
    orange34.add_vertex((354, 80))
    orange34.add_vertex((331, 46))
    window.add(orange34)

    orange35 = GPolygon()
    orange35.filled = True
    orange35.fill_color = 'chocolate'
    orange35.add_vertex((354, 80))
    orange35.add_vertex((307, 87))
    orange35.add_vertex((335, 114))
    window.add(orange35)

    orange36 = GPolygon()
    orange36.filled = True
    orange36.fill_color = 'chocolate'
    orange36.add_vertex((354, 80))
    orange36.add_vertex((331, 46))
    orange36.add_vertex((368, 49))
    window.add(orange36)

    orange37 = GPolygon()
    orange37.filled = True
    orange37.fill_color = 'chocolate'
    orange37.add_vertex((354, 80))
    orange37.add_vertex((368, 49))
    orange37.add_vertex((394, 48))
    orange37.add_vertex((403, 67))
    window.add(orange37)

    orange38 = GPolygon()
    orange38.filled = True
    orange38.fill_color = 'chocolate'
    orange38.add_vertex((145, 517))
    orange38.add_vertex((110, 575))
    orange38.add_vertex((121, 498))
    window.add(orange38)

    orange39 = GPolygon()
    orange39.filled = True
    orange39.fill_color = 'chocolate'
    orange39.add_vertex((161, 169))
    orange39.add_vertex((193, 177))
    orange39.add_vertex((205, 131))
    orange39.add_vertex((147, 165))
    window.add(orange39)

    orange40 = GPolygon()
    orange40.filled = True
    orange40.fill_color = 'chocolate'
    orange40.add_vertex((147, 165))
    orange40.add_vertex((98, 223))
    orange40.add_vertex((144, 205))
    orange40.add_vertex((161, 169))
    window.add(orange40)

    orange41 = GPolygon()
    orange41.filled = True
    orange41.fill_color = 'chocolate'
    orange41.add_vertex((98, 223))
    orange41.add_vertex((144, 205))
    orange41.add_vertex((145, 233))
    orange41.add_vertex((112, 258))
    window.add(orange41)

    orange42 = GPolygon()
    orange42.filled = True
    orange42.fill_color = 'chocolate'
    orange42.add_vertex((98, 223))
    orange42.add_vertex((112, 258))
    orange42.add_vertex((65, 298))
    orange42.add_vertex((78, 250))
    window.add(orange42)

    orange43 = GPolygon()
    orange43.filled = True
    orange43.fill_color = 'chocolate'
    orange43.add_vertex((77, 552))
    orange43.add_vertex((103, 503))
    orange43.add_vertex((82, 470))
    orange43.add_vertex((80, 510))
    window.add(orange43)

    orange44 = GPolygon()
    orange44.filled = True
    orange44.fill_color = 'chocolate'
    orange44.add_vertex((118, 525))
    orange44.add_vertex((72, 455))
    orange44.add_vertex((123, 470))
    window.add(orange44)

    orange45 = GPolygon()
    orange45.filled = True
    orange45.fill_color = 'chocolate'
    orange45.add_vertex((145, 470))
    orange45.add_vertex((182, 512))
    orange45.add_vertex((215, 512))
    orange45.add_vertex((170, 466))
    window.add(orange45)

    orange46 = GPolygon()
    orange46.filled = True
    orange46.fill_color = 'chocolate'
    orange46.add_vertex((145, 470))
    orange46.add_vertex((170, 466))
    orange46.add_vertex((210, 461))
    orange46.add_vertex((162, 445))
    orange46.add_vertex((152, 408))
    orange46.add_vertex((123, 470))
    window.add(orange46)

    orange47 = GPolygon()
    orange47.filled = True
    orange47.fill_color = 'chocolate'
    orange47.add_vertex((300, 497))
    orange47.add_vertex((339, 484))
    orange47.add_vertex((375, 500))
    orange47.add_vertex((324, 512))
    window.add(orange47)

    orange48 = GPolygon()
    orange48.filled = True
    orange48.fill_color = 'chocolate'
    orange48.add_vertex((375, 500))
    orange48.add_vertex((339, 484))
    orange48.add_vertex((311, 471))
    orange48.add_vertex((366, 456))
    window.add(orange48)

    orange49 = GPolygon()
    orange49.filled = True
    orange49.fill_color = 'chocolate'
    orange49.add_vertex((375, 500))
    orange49.add_vertex((366, 456))
    orange49.add_vertex((374, 422))
    orange49.add_vertex((393, 460))
    window.add(orange49)

    orange50 = GPolygon()
    orange50.filled = True
    orange50.fill_color = 'chocolate'
    orange50.add_vertex((366, 456))
    orange50.add_vertex((374, 422))
    orange50.add_vertex((355, 411))
    orange50.add_vertex((327, 450))
    window.add(orange50)

    orange51 = GPolygon()
    orange51.filled = True
    orange51.fill_color = 'chocolate'
    orange51.add_vertex((355, 411))
    orange51.add_vertex((327, 450))
    orange51.add_vertex((319, 428))
    orange51.add_vertex((331, 397))
    window.add(orange51)

    orange52 = GPolygon()
    orange52.filled = True
    orange52.fill_color = 'chocolate'
    orange52.add_vertex((265, 413))
    orange52.add_vertex((241, 413))
    orange52.add_vertex((253, 452))
    orange52.add_vertex((263, 452))
    orange52.add_vertex((265, 413))
    orange52.add_vertex((288, 413))
    orange52.add_vertex((272, 452))
    orange52.add_vertex((263, 452))
    window.add(orange52)

    orange53 = GPolygon()
    orange53.filled = True
    orange53.fill_color = 'chocolate'
    orange53.add_vertex((103, 373))
    orange53.add_vertex((123, 365))
    orange53.add_vertex((131, 338))
    orange53.add_vertex((100, 331))
    window.add(orange53)

    orange54 = GPolygon()
    orange54.filled = True
    orange54.fill_color = 'chocolate'
    orange54.add_vertex((123, 365))
    orange54.add_vertex((131, 338))
    orange54.add_vertex((153, 338))
    orange54.add_vertex((156, 360))
    window.add(orange54)

    orange55 = GPolygon()
    orange55.filled = True
    orange55.fill_color = 'chocolate'
    orange55.add_vertex((131, 338))
    orange55.add_vertex((100, 331))
    orange55.add_vertex((112, 302))
    orange55.add_vertex((133, 315))
    window.add(orange55)

    orange56 = GPolygon()
    orange56.filled = True
    orange56.fill_color = 'chocolate'
    orange56.add_vertex((100, 331))
    orange56.add_vertex((112, 302))
    orange56.add_vertex((113, 275))
    orange56.add_vertex((65, 298))
    window.add(orange56)

    orange57 = GPolygon()
    orange57.filled = True
    orange57.fill_color = 'chocolate'
    orange57.add_vertex((239, 371))
    orange57.add_vertex((259, 380))
    orange57.add_vertex((286, 358))
    orange57.add_vertex((257, 354))
    window.add(orange57)

    orange58 = GPolygon()
    orange58.filled = True
    orange58.fill_color = 'chocolate'
    orange58.add_vertex((259, 380))
    orange58.add_vertex((286, 358))
    orange58.add_vertex((306, 359))
    orange58.add_vertex((262, 398))
    window.add(orange58)

    orange59 = GPolygon()
    orange59.filled = True
    orange59.fill_color = 'chocolate'
    orange59.add_vertex((257, 354))
    orange59.add_vertex((286, 358))
    orange59.add_vertex((280, 334))
    orange59.add_vertex((258, 320))
    window.add(orange59)

    orange60 = GPolygon()
    orange60.filled = True
    orange60.fill_color = 'chocolate'
    orange60.add_vertex((323, 310))
    orange60.add_vertex((356, 340))
    orange60.add_vertex((356, 314))
    window.add(orange60)

    orange61 = GPolygon()
    orange61.filled = True
    orange61.fill_color = 'chocolate'
    orange61.add_vertex((356, 340))
    orange61.add_vertex((356, 314))
    orange61.add_vertex((393, 324))
    orange61.add_vertex((377, 360))
    window.add(orange61)

    orange62 = GPolygon()
    orange62.filled = True
    orange62.fill_color = 'chocolate'
    orange62.add_vertex((356, 314))
    orange62.add_vertex((393, 324))
    orange62.add_vertex((383, 297))
    window.add(orange62)

    orange63 = GPolygon()
    orange63.filled = True
    orange63.fill_color = 'chocolate'
    orange63.add_vertex((383, 297))
    orange63.add_vertex((393, 324))
    orange63.add_vertex((412, 291))
    orange63.add_vertex((404, 277))
    window.add(orange63)

    orange64 = GPolygon()
    orange64.filled = True
    orange64.fill_color = 'chocolate'
    orange64.add_vertex((113, 275))
    orange64.add_vertex((178, 252))
    orange64.add_vertex((225, 262))
    orange64.add_vertex((200, 240))
    orange64.add_vertex((172, 227))
    window.add(orange64)

    orange65 = GPolygon()
    orange65.filled = True
    orange65.fill_color = 'chocolate'
    orange65.add_vertex((216, 150))
    orange65.add_vertex((234, 155))
    orange65.add_vertex((239, 144))
    orange65.add_vertex((234, 111))
    window.add(orange65)

    orange66 = GPolygon()
    orange66.filled = True
    orange66.fill_color = 'chocolate'
    orange66.add_vertex((332, 257))
    orange66.add_vertex((335, 271))
    orange66.add_vertex((373, 255))
    orange66.add_vertex((362, 247))
    window.add(orange66)

    orange67 = GPolygon()
    orange67.filled = True
    orange67.fill_color = 'chocolate'
    orange67.add_vertex((404, 277))
    orange67.add_vertex((412, 291))
    orange67.add_vertex((421, 304))
    orange67.add_vertex((421, 276))
    orange67.add_vertex((408, 244))
    orange67.add_vertex((403, 248))
    window.add(orange67)

    orange68 = GPolygon()
    orange68.filled = True
    orange68.fill_color = 'chocolate'
    orange68.add_vertex((408, 212))
    orange68.add_vertex((408, 244))
    orange68.add_vertex((403, 248))
    orange68.add_vertex((387, 236))
    orange68.add_vertex((384, 223))
    window.add(orange68)

    orange69 = GPolygon()
    orange69.filled = True
    orange69.fill_color = 'chocolate'
    orange69.add_vertex((408, 212))
    orange69.add_vertex((384, 223))
    orange69.add_vertex((363, 211))
    orange69.add_vertex((377, 199))
    window.add(orange69)

    orange70 = GPolygon()
    orange70.filled = True
    orange70.fill_color = 'chocolate'
    orange70.add_vertex((363, 211))
    orange70.add_vertex((377, 199))
    orange70.add_vertex((371, 175))
    orange70.add_vertex((354, 193))
    window.add(orange70)

    orange71 = GPolygon()
    orange71.filled = True
    orange71.fill_color = 'chocolate'
    orange71.add_vertex((371, 175))
    orange71.add_vertex((354, 193))
    orange71.add_vertex((331, 233))
    orange71.add_vertex((342, 175))
    window.add(orange71)

    orange72 = GPolygon()
    orange72.filled = True
    orange72.fill_color = 'chocolate'
    orange72.add_vertex((274, 318))
    orange72.add_vertex((281, 280))
    orange72.add_vertex((266, 270))
    orange72.add_vertex((257, 298))
    window.add(orange72)

    orange73 = GPolygon()
    orange73.filled = True
    orange73.fill_color = 'chocolate'
    orange73.add_vertex((266, 270))
    orange73.add_vertex((257, 298))
    orange73.add_vertex((243, 281))
    orange73.add_vertex((257, 241))
    window.add(orange73)

    orange74 = GPolygon()
    orange74.filled = True
    orange74.fill_color = 'chocolate'
    orange74.add_vertex((257, 241))
    orange74.add_vertex((231, 226))
    orange74.add_vertex((247, 213))
    window.add(orange74)

    orange75 = GPolygon()
    orange75.filled = True
    orange75.fill_color = 'chocolate'
    orange75.add_vertex((231, 226))
    orange75.add_vertex((247, 213))
    orange75.add_vertex((255, 191))
    orange75.add_vertex((226, 189))
    window.add(orange75)

    orange76 = GPolygon()
    orange76.filled = True
    orange76.fill_color = 'chocolate'
    orange76.add_vertex((266, 270))
    orange76.add_vertex((281, 280))
    orange76.add_vertex((297, 272))
    orange76.add_vertex((295, 244))
    window.add(orange76)

    orange77 = GPolygon()
    orange77.filled = True
    orange77.fill_color = 'chocolate'
    orange77.add_vertex((297, 272))
    orange77.add_vertex((295, 244))
    orange77.add_vertex((332, 257))
    orange77.add_vertex((314, 284))
    window.add(orange77)

    orange78 = GPolygon()
    orange78.filled = True
    orange78.fill_color = 'chocolate'
    orange78.add_vertex((308, 148))
    orange78.add_vertex((317, 200))
    orange78.add_vertex((280, 208))
    window.add(orange78)

    orange79 = GPolygon()
    orange79.filled = True
    orange79.fill_color = 'chocolate'
    orange79.add_vertex((317, 200))
    orange79.add_vertex((280, 208))
    orange79.add_vertex((278, 240))
    orange79.add_vertex((295, 244))
    window.add(orange79)

    orange80 = GPolygon()
    orange80.filled = True
    orange80.fill_color = 'chocolate'
    orange80.add_vertex((308, 148))
    orange80.add_vertex((280, 208))
    orange80.add_vertex((270, 178))
    orange80.add_vertex((278, 157))
    window.add(orange80)

    orange81 = GPolygon()
    orange81.filled = True
    orange81.fill_color = 'chocolate'
    orange81.add_vertex((270, 178))
    orange81.add_vertex((278, 157))
    orange81.add_vertex((255, 164))
    orange81.add_vertex((255, 191))
    window.add(orange81)

    orange82 = GPolygon()
    orange82.filled = True
    orange82.fill_color = 'chocolate'
    orange82.add_vertex((267, 272))
    orange82.add_vertex((295, 244))
    orange82.add_vertex((278, 240))
    orange82.add_vertex((267, 228))
    window.add(orange82)






    white1 = GPolygon()
    white1.filled = True
    white1.fill_color = 'white'
    white1.add_vertex((187, 570))
    white1.add_vertex((200, 566))
    white1.add_vertex((225, 555))
    white1.add_vertex((215, 512))
    white1.add_vertex((197, 528))
    window.add(white1)

    white2 = GPolygon()
    white2.filled = True
    white2.fill_color = 'white'
    white2.add_vertex((215, 512))
    white2.add_vertex((225, 555))
    white2.add_vertex((249, 578))
    white2.add_vertex((261, 547))
    white2.add_vertex((245, 533))
    window.add(white2)

    white3 = GPolygon()
    white3.filled = True
    white3.fill_color = 'white'
    white3.add_vertex((261, 547))
    white3.add_vertex((245, 533))
    white3.add_vertex((268, 511))
    white3.add_vertex((295, 530))
    window.add(white3)

    white4 = GPolygon()
    white4.filled = True
    white4.fill_color = 'white'
    white4.add_vertex((261, 547))
    white4.add_vertex((295, 530))
    white4.add_vertex((322, 575))
    white4.add_vertex((294, 558))
    window.add(white4)

    white5 = GPolygon()
    white5.filled = True
    white5.fill_color = 'white'
    white5.add_vertex((261, 547))
    white5.add_vertex((294, 558))
    white5.add_vertex((285, 585))
    white5.add_vertex((254, 565))
    window.add(white5)

    white6 = GPolygon()
    white6.filled = True
    white6.fill_color = 'white'
    white6.add_vertex((295, 530))
    white6.add_vertex((322, 575))
    white6.add_vertex((324, 512))
    window.add(white6)

    white7 = GPolygon()
    white7.filled = True
    white7.fill_color = 'white'
    white7.add_vertex((322, 575))
    white7.add_vertex((324, 512))
    white7.add_vertex((350, 547))
    window.add(white7)

    white8 = GPolygon()
    white8.filled = True
    white8.fill_color = 'white'
    white8.add_vertex((170, 466))
    white8.add_vertex((210, 461))
    white8.add_vertex((242, 494))
    white8.add_vertex((215, 512))
    window.add(white8)

    white9 = GPolygon()
    white9.filled = True
    white9.fill_color = 'white'
    white9.add_vertex((210, 461))
    white9.add_vertex((242, 494))
    white9.add_vertex((263, 487))
    white9.add_vertex((238, 451))
    window.add(white9)

    white10 = GPolygon()
    white10.filled = True
    white10.fill_color = 'white'
    white10.add_vertex((210, 461))
    white10.add_vertex((238, 451))
    white10.add_vertex((207, 432))
    white10.add_vertex((162, 445))
    window.add(white10)

    white11 = GPolygon()
    white11.filled = True
    white11.fill_color = 'white'
    white11.add_vertex((207, 432))
    white11.add_vertex((162, 445))
    white11.add_vertex((199, 393))
    window.add(white11)

    white12 = GPolygon()
    white12.filled = True
    white12.fill_color = 'white'
    white12.add_vertex((263, 487))
    white12.add_vertex((300, 497))
    white12.add_vertex((339, 484))
    white12.add_vertex((311, 471))
    window.add(white12)

    white13 = GPolygon()
    white13.filled = True
    white13.fill_color = 'white'
    white13.add_vertex((263, 487))
    white13.add_vertex((311, 471))
    white13.add_vertex((319, 428))
    white13.add_vertex((287, 454))
    window.add(white13)

    white14 = GPolygon()
    white14.filled = True
    white14.fill_color = 'white'
    white14.add_vertex((145, 421))
    white14.add_vertex((123, 365))
    white14.add_vertex((170, 388))
    window.add(white14)

    white15 = GPolygon()
    white15.filled = True
    white15.fill_color = 'white'
    white15.add_vertex((241, 413))
    white15.add_vertex((288, 413))
    white15.add_vertex((331, 397))
    white15.add_vertex((262, 398))
    window.add(white15)

    white16 = GPolygon()
    white16.filled = True
    white16.fill_color = 'white'
    white16.add_vertex((241, 413))
    white16.add_vertex((262, 398))
    white16.add_vertex((216, 393))
    white16.add_vertex((201, 407))
    window.add(white16)

    white17 = GPolygon()
    white17.filled = True
    white17.fill_color = 'white'
    white17.add_vertex((201, 407))
    white17.add_vertex((216, 393))
    white17.add_vertex((226, 384))
    white17.add_vertex((221, 332))
    window.add(white17)

    white18 = GPolygon()
    white18.filled = True
    white18.fill_color = 'white'
    white18.add_vertex((143, 283))
    white18.add_vertex((163, 310))
    white18.add_vertex((203, 310))
    white18.add_vertex((176, 291))
    window.add(white18)

    white19 = GPolygon()
    white19.filled = True
    white19.fill_color = 'white'
    white19.add_vertex((178, 252))
    white19.add_vertex((201, 275))
    white19.add_vertex((219, 318))
    white19.add_vertex((225, 262))
    window.add(white19)

    white20 = GPolygon()
    white20.filled = True
    white20.fill_color = 'white'
    white20.add_vertex((306, 359))
    white20.add_vertex((290, 373))
    white20.add_vertex((331, 397))
    white20.add_vertex((329, 368))
    window.add(white20)

    white21 = GPolygon()
    white21.filled = True
    white21.fill_color = 'white'
    white21.add_vertex((113, 275))
    white21.add_vertex((172, 227))
    white21.add_vertex((185, 218))
    white21.add_vertex((145, 222))
    white21.add_vertex((145, 233))
    window.add(white21)

    white22 = GPolygon()
    white22.filled = True
    white22.fill_color = 'white'
    white22.add_vertex((185, 218))
    white22.add_vertex((145, 222))
    white22.add_vertex((144, 205))
    white22.add_vertex((176, 186))
    window.add(white22)

    white23 = GPolygon()
    white23.filled = True
    white23.fill_color = 'white'
    white23.add_vertex((185, 218))
    white23.add_vertex((176, 186))
    white23.add_vertex((193, 177))
    white23.add_vertex((226, 189))
    window.add(white23)

    white24 = GPolygon()
    white24.filled = True
    white24.fill_color = 'white'
    white24.add_vertex((193, 177))
    white24.add_vertex((226, 189))
    white24.add_vertex((234, 155))
    white24.add_vertex((216, 150))
    window.add(white24)

    white25 = GPolygon()
    white25.filled = True
    white25.fill_color = 'white'
    white25.add_vertex((226, 189))
    white25.add_vertex((234, 155))
    white25.add_vertex((239, 144))
    white25.add_vertex((270, 141))
    white25.add_vertex((255, 166))
    window.add(white25)

    white26 = GPolygon()
    white26.filled = True
    white26.fill_color = 'white'
    white26.add_vertex((408, 212))
    white26.add_vertex((454, 205))
    white26.add_vertex((456, 239))
    white26.add_vertex((454, 258))
    white26.add_vertex((438, 230))
    window.add(white26)

    white27 = GPolygon()
    white27.filled = True
    white27.fill_color = 'white'
    white27.add_vertex((371, 234))
    white27.add_vertex((351, 222))
    white27.add_vertex((331, 233))
    white27.add_vertex((354, 193))
    window.add(white27)

    white28 = GPolygon()
    white28.filled = True
    white28.fill_color = 'white'
    white28.add_vertex((351, 222))
    white28.add_vertex((331, 233))
    white28.add_vertex((295, 244))
    white28.add_vertex((332, 257))
    window.add(white28)

    white29 = GPolygon()
    white29.filled = True
    white29.fill_color = 'white'
    white29.add_vertex((331, 233))
    white29.add_vertex((295, 244))
    white29.add_vertex((317, 200))
    white29.add_vertex((342, 175))
    window.add(white29)

    white30 = GPolygon()
    white30.filled = True
    white30.fill_color = 'white'
    white30.add_vertex((317, 200))
    white30.add_vertex((342, 175))
    white30.add_vertex((308, 148))
    window.add(white30)









    yellowgreen1 = GPolygon()
    yellowgreen1.filled = True
    yellowgreen1.fill_color = 'yellowgreen'
    yellowgreen1.add_vertex((176, 291))
    yellowgreen1.add_vertex((201, 275))
    yellowgreen1.add_vertex((178, 252))
    yellowgreen1.add_vertex((161, 276))
    window.add(yellowgreen1)

    yellowgreen2 = GPolygon()
    yellowgreen2.filled = True
    yellowgreen2.fill_color = 'yellowgreen'
    yellowgreen2.add_vertex((372, 290))
    yellowgreen2.add_vertex((360, 294))
    yellowgreen2.add_vertex((343, 288))
    yellowgreen2.add_vertex((371, 271))
    window.add(yellowgreen2)

    yellowgreen3 = GPolygon()
    yellowgreen3.filled = True
    yellowgreen3.fill_color = 'yellowgreen'
    yellowgreen3.add_vertex((371, 271))
    yellowgreen3.add_vertex((343, 288))
    yellowgreen3.add_vertex((335, 271))
    yellowgreen3.add_vertex((355, 263))
    window.add(yellowgreen3)


if __name__ == '__main__':
    main()
