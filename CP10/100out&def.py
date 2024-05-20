# def my_function():
#     return 3 * 2
# output = my_function() 
# print(output)

# def format_name(f_name,l_name):
#     print(f_name.title())
#     print(l_name.title())
# format_name("aim","jana")

def format_name(f_name,l_name):
    formated_generated_f  = f_name.title()
    formated_generated_l = l_name.title()
    return (f"first : {formated_generated_f} Last : {formated_generated_l}")
print(format_name("sexy","girl"))