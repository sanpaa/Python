movies = ["Exterminador do futuro",1985, "Arnold Schwarzenegger",["Rambo",1982,"Sylvester Stallone", ["Star Wars", 1977, "Luke Skywalker/ Mark Hamill", ["Tropa de Elite", 2007, "Wagner Moura"]]]]

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                      if isinstance(deeper_item,list):
                          for moredeeper_item in deeper_item:
                              if isinstance(moredeeper_item,list):
                                  for justmoredeeper_item in moredeeper_item:

                            else:
                                print(moredeeper_item)

                else:
                    print(deeper_item)    

        else:
            print(nested_item)
else:
    print(each_item)
    