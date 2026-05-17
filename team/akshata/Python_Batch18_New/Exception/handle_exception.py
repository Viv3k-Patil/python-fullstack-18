

try:
    a = 1/0
    
except Exception as e:
   print("Error is occured..!")

else:
    print("Code run sccussfully..!")

finally:
    print("Cleanup code")