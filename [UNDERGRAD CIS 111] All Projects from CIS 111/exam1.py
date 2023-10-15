big_radius = float(input("Enter the radius of big cylinder: "))
big_height = float(input("Enter the height of big cylinder: "))
pi = 3.142
big_volume = pi*big_radius*big_radius*big_height
print()
small_radius = float(input("Enter the radius of small cylinder: "))
small_height = float(input("Enter the height of small cylinder: "))
small_volume = pi*small_radius*small_radius*small_height
differ = big_volume-small_volume
print()
print("Volume of big cylinder: ",big_volume,"cubic units")
print("Volume of small cylinder:",small_volume,"cubic units")
print("The two cylinders differ in volume by %.3f " %differ ,"cubic units") 