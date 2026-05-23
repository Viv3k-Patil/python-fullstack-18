class Mobile:
  def __init__(self,
  mobile_name,             
  mobile_color,
  mobile_RAM,
  mobile_ROM,
  mobile_price,
  mobile_battery
                ):
     self.mobile_name=mobile_name
     self.mobile_color=mobile_color
     self.mobile_RAM=mobile_RAM
     self.mobile_ROM=mobile_ROM
     self.mobile_price=mobile_price
     self.mobile_battery=mobile_battery

  def __str__(self):
     return f"mobile name:{self.mobile_name},\nmobile color:{self.mobile_color},\nmobile RAM:{self.mobile_RAM},\nmobileROM:{self.mobile_ROM},\nmobile price:{self.mobile_price},\nmobile battery:{self.mobile_battery}"
        
  def grret( ):
     print("this is example of grret")


  grret()     
a=Mobile(
          [
          "redmi",
           "oppo", 
          " vivo",
          "samsung",
          "iphone"
          ],
   "Red",
   "8GB",
   "256 ROM",
    25999,
   "5500Mph"
    )   



print(a)