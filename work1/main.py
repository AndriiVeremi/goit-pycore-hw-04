def total_salary(path):
    
    total = 0
    count = 0
    
    try:        
        with open(path, "r", encoding="utf-8") as f:
            for i in f:
                try:
                    user = i.strip().split(",")
                    total += int(user[1])
                    count += 1
                except ValueError:
                    print(f"Невірний формат {i}")
            if count > 0:
                average = total / count    
                return total, average
                        
    except FileNotFoundError:
       print(f"File not found: {path}") 
       return None
    except Exception as err:
       print (f"Error: {err}")
       return None
    
total, average = total_salary("work1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


