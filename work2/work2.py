def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as f:           
            for i in f:
                try:
                    cat = i.strip().split(",")
                    new_cat = {}                 
                    new_cat.update({"id": cat[0], "name": cat[1], "age": cat[2]})
                    cats_info.append(new_cat)
                except ValueError:
                    print(f"Невірний формат {i}")                 
    except FileNotFoundError:
        print(f"File not found: {path}") 
        return None
    except Exception as err:
       print (f"Error: {err}")
       return None
    return cats_info      

cats_info = get_cats_info("work2/cats_file.txt")
print("cats_info -->", cats_info)
