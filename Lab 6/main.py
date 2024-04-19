import MyPandas

data = MyPandas.to_json("Titanic.csv")
MyPandas.show(data, param="top", num= 10)
MyPandas.info(data)
print()
MyPandas.delNaN(data)
MyPandas.info(data)