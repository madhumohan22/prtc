class pencil:
    def __init__(sellf,count,color,pen_height) -> None:
        sellf.count=count
        sellf.color=color
        sellf.pen_height=pen_height
    def details(sellf):
        print("count: ",sellf.count)
        print("color: ",sellf.color)
        print("height: ",sellf.pen_height)
    
reynolds=pencil("23",'blue',"20cm")
reynolds.details()

hero=pencil("21","black","23")
hero.details()
