 #1
#s = 'shalom'
#def print_string_reverse(s):
    #if s == 'none' or s==(" ") or s.strip() =="":
        #print ('wrong string')
    #else : print(s[::-1])
#print_string_reverse(s)

#2
phone="0537998547"
def is_isr_phone_number(phone):
     if phone[0] =="0" and len(phone) ==10 and phone.isdigit():
         return True
     else:
         return False
print (is_isr_phone_number("0537889999"))

#3


s ='Hello my nice world'
print(" ".join(s.split()[::-1]))







