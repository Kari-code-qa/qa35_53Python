def print_list_reverse(lst):
    if (lst is None or lst == []
        or type(lst) != list):
        print("Wrong list")
    else:
        print (lst[::-1])
print_list_reverse([1,2,3,4,5])

#2
def is_valid_point(point):
     if point is None or point ==():
         return None
     if  type(point) == tuple and len(point) ==2\
        and type(point[0]) in (int,float)\
        and type(point[1]) in (int,float):
        return True
     else:
         return False

print (is_valid_point((3,5)))
print (is_valid_point((3,"5")))
print (is_valid_point((3,[5])))
print (is_valid_point((1,2,3)))
print (is_valid_point((())))
print (is_valid_point((())))
print (is_valid_point(((None))))