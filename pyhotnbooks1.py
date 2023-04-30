B1=int(input('''Introdutctionn of Python Programming Book cost : Rs"499"
              enter the how many Introduction to python programing books do you want:'''))
B2=int(input('''Python Libraries Cookbook : Rs "855"
                enter the how many Introduction to python programing books do you want:'''));
B3=int(input('''Data Science in Pyhton : Rs"645"
             enter the how many Introduction to python programing books do you want:'''))
total_books_cost=(B1*499)+(B2*855)+(B3*645);
print("total_books_cost =  ",total_books_cost)
GST_on_total_books=(12/100)*total_books_cost;
print("GST_on_total_books = ",GST_on_total_books)
transport_charge=250;
total_cost=total_books_cost+GST_on_total_books+transport_charge;
print("total_cost = ",total_cost)

       
       
