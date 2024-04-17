import MyPandas

data = MyPandas.to_json("Titanic.csv")
MyPandas.show(data, param="top", num= 10)
MyPandas.info(data)
MyPandas.delNaN(data)
MyPandas.show(data, param="top", num= 20)
MyPandas.info(data)