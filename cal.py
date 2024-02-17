
def calculate(s:str):
    i = j = 0
    curr = prev = res =0
    curr_opa = '+'
    while i < len(s):
        curr_char = s[i]
        if curr_char.isdigit():
            while i < len(s) and s[i].isdigit():
                curr = curr * 10 + int(s[i])
                i += 1
            i -= 1
            
            if curr_opa == '+':
                res += curr
                prev = curr
            elif curr_opa == '-':
                res -= curr
                prev = -curr
            elif curr_opa == '*':
                res -= prev
                res += prev * curr
                prev = prev * curr
            else:
                res -= prev
                res += prev/curr
                prev = prev * curr
            curr = 0
        elif curr_char != "":
            curr_opa = curr_char
        i += 1
    return res





def main():
    query = input('[USER] ')
    print(f"[RESULT] {calculate(query)}")

main()