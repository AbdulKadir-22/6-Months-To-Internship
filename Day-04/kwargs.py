
def marvel(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")


marvel( Ironman = "2008",
        CaptainAmerica = "2011",
        Spiderman = "2012")