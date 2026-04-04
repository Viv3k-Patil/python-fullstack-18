print("_____Welcome To The Movie Booking Application_____")

print("1.Saiyara(400rs)")
print("2.Dhurandhar(300rs)")
print("3.Sairat(250rs)")
print("4.Bahubali(350rs)")
print("5.KGF(200rs)")
print("6.EXIT")


movieName=""
total_price=0
discount=0
final_price=0
choice=int(input("enter your choice:"))
qty=int(input("how many wants:"))


if choice==1:
    movieName="Saiyara"
    total_price=400*qty
    
elif choice==2:
    movieName="Dhurandhar"
    total_price=300*qty
    

elif choice==3:
    movieName="Sairat"
    total_price=250*qty
    

elif choice==4:
    movieName="Bahubali"
    total_price=350*qty
    

elif choice==5:
    movieName="KGF"
    total_price=200*qty


else:
    print("Invalid Choice")



if qty>=5:
    discount=total_price*0.10
    final_price=total_price-discount
else:
    final_price=total_price



print("_____*****MOVIE BOOKED SUCCESSFULLY******_____")
print("Your Bill👇")
print("Tickets",qty)
print("Movie Name:",movieName)
print("Total Price",total_price)
print("Discount",discount)
print("Final_Price",final_price)