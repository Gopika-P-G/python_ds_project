data="gopika93@gmail.com"

comp_start_letter=data.find("@")
print(comp_start_letter)

comp_end_letter =data.find(".",comp_start_letter)
print(comp_end_letter)

company_name = data[comp_start_letter + 1:comp_end_letter]
print(company_name)
