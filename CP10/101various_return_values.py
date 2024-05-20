
def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "you didn't provide valid inputs"

    formated_generated_f  = f_name.title()
    formated_generated_l = l_name.title()
    return (f"first : {formated_generated_f} Last : {formated_generated_l}")

print(format_name(input("what's U first name?"),input("what tis your last name?")))