def run():
    my_list = [1, "Hello", True, 4.5 ]
    my_dict = {"firstname": "Gustavo" , "lastname": "Alvarado"}

super_list = [
    {"firstname": "Gustavo" , "lastname":  "Alvarado"},
    {"firstname": "Jerry" , "lastname":  "Montes"},
    {"firstname": "Dulfina" , "lastname": "Montes"},
    {"firstname": "Canela" , "lastname":  "Montes"},
    {"firstname": "nina" , "lastname":  "Montes"},
]

super_dict = {
    "natural_nums": [1, 2, 3, 4, 5,],
    "integer_nums": [-1, -2, 0, 1, 2],
    "floating_nums": [ 1.1 , 2.2 , 2.3 , 2.4]
}    

for key,value in super_dict.items():
    print(key,"-",value)
    

if __name__ == '__main__':
    run()
