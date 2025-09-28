def swap_case(s):
    
        new_s = []
        for i in s:
            if i.isupper():
                new_s.append(i.lower())
            elif i.isdigit():
                new_s.append(i)
            elif i.isspace():
                new_s.append(i)
            elif i.islower():
                new_s.append(i.upper())
            
            
        return "".join(new_s)
def main():
    
    while True:
        text=input()
        if 0<len(text)<=1000:
                    print(swap_case(text))
                    break
        else:
                    print("please enter a valid string")
                    continue
main()
