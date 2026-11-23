#1
def remove_spaces(s):
    return ''.join(s.split())

print(remove_spaces("he llo\twor ld"))
#2
t2="hello"
print(t2[::-1])
#3
def reverse_remove(s):
    cleaned = ''.join(s.split())
    return cleaned[::-1]

print(reverse_remove("he llo world"))

#4
text = "my_variable_name"

parts = text.split("_")

print(parts)

result = parts[0]

for word in parts[1:]:
    result +=word.capitalize()
print(result)

#5
def snake_to_pascal(s):
    words = s.split("_")
    result = ""

    for word in words:
        result += word.capitalize()

    return result

print(snake_to_pascal("my_variable_name"))

#6
def camel_to_snake(s):
    result=""

    for ch in s:
        if ch.isupper():
            result += "_" + ch.lower()
        else:
            result+=ch

    return result
print(camel_to_snake("myVariableName"))

#7
def camel_to_pascal(s):
    return s[0].upper() + s[1:]

print(camel_to_pascal("myVariable"))

#8
def pascal_to_camel(s):
    return s[0].lower() + s[1:]

print(pascal_to_camel("MyVariable"))

#9
def pascal_to_snake(s):
    result=""

    for ch in s:
        if ch.isupper():
            result += "_" + ch.lower()
        else:
            result +=ch
    return result.lstrip("_").lower()

print(pascal_to_snake("MyVariable"))

#10
def text_to_camel(s):
    words = s.split()
    return words[0].lower() + "".join(word.title() for word in words[1:])

print(text_to_camel("hello word example"))

#11
def text_to_snake(s):
    words = s.lower().split()
    return "_".join(words)   

print(text_to_snake("hello World example"))

#12
def text_to_pascal(s):
    words = s.split()
    result = ""

    for word in words:
        result += word.capitalize()

    return result

print(text_to_pascal("hello world example"))  

#13
def swap_case(s):
    return text.swapcase()

print(swap_case("HeLLo"))

#14
def extract_digits(s):
    result=""

    for ch in s:
        if  ch.isdigit():
            result +=ch
    return result      
print(extract_digits("abc123d4"))

#15
def separate_char(text):

    upper = ""
    lower = ""
    digit = ""
    Special = ""

    for ch in text:

        if ch.isupper():
            upper += ch

        elif ch.islower():
            lower += ch

        elif ch.isdigit():
            digit += ch

        else:
            Special += ch

    print("Upper:", upper)
    print("Lower:", lower)
    print("Digit:", digit)
    print("Special:", Special)


separate_char("AAbcc@123//")

#16
def count_char(text):

    upper = 0
    lower = 0
    digit = 0
    Special = 0

    for ch in text:

        if ch.isupper():
            upper += 1

        elif ch.islower():
            lower += 1

        elif ch.isdigit():
            digit += 1

        else:
            Special += 1

    print("Upper:", upper)
    print("Lower:", lower)
    print("Digit:", digit)
    print("Special:", Special)


count_char("AAbcc@123//")

#17 password strength check
def check_password(password):

    upper=False
    lower=False
    digit=False
    special=False

    for i in password:
        if i.isupper():
            upper=True
        elif i.islower():
            lower=True
        elif i.isdigit():
            digit=True
        else:
            special=True

    if upper and lower and digit and special:
        return "strong password"
    else:
        return "weak password"

print(check_password("Pass123!"))

#18 remove duplicates
def remove_duplicates(text):
    result=""

    for i in text:
        if i not in result:
            result +=i
    return result
print(remove_duplicates("abbcad"))

#19
def print_duplicates(text):
    result=""

    for i in text:
        if text.count(i)>1 and i not in result:
            result += i + " "

    return result
print(print_duplicates("aabbcadd"))

def next_ch(text):
    result=""

    for i in text:
        result += chr(ord(i) + 1)

    return result
print(next_ch("abcd"))     

##List manipulation in string
print("list manipulation in string");

def add(list,value):
   list.append(value)
   return list

print(add([1,2,3],4))

def remove(list,value):
   list.remove(value)
   return list

print(remove([1,2,3,4],3))

list=[1,2,3,4]

list.pop(1)

print(list)

def first_max(list):
 l=list[0]
 for i in list:
   if i>l: #change > to < for min 
      l=i
 return l
print(first_max([4,7,1,9]))   

l=[1,2,3]
print(sum(l))

def sum_list(list):
   s=0
   for i in list:
      s+=i
   return s
 
print(sum_list([1,2,3]))

def count_list(list,value):
   a=list.count(value)
   return a 

print(count_list([1,2,3,2,3,2],2))

l=[2,3,4]
print(l[::-1])

def rev(list):
   list.reverse()
   return list
print(rev([10,20,30]))   

lst =[1,2,2,3,4,5,1]

uni=[]

for i in lst:
   if i not in uni:
      uni.append(i)

print(uni)

def dup(list):
   l=[]
   for i in list:
      if i not in l:
         l.append(i)
   return l

print(dup([1,2,3,4,4,5,5]))

l1=[1,2,3]
l2=[4,5,6]

print(l1 + l2)

def merge(l1,l2):
   l1.extend(l2)
   return l1

print(merge([1,2,3,4],[5,6,7]))   

def common(l1,l2):
   l=[]
   for i in l1:
      if i in l2 and i not in l:
         l.append(i)
   return l     

print(common([1,2,4,7,8],[1,2,5,4,6]))

def even(l1):
   l=[]
   for i in l1:
      if i%2==0:
         l.append(i)
   return l

print(even([1,4,1]))

def pali(l1):
   if l1==l1[::-1]:
     print("palindome")
   else:
        print("not")

print(pali([1,2,1]))

def pal(l1):
   if l1 == l1[::-1]:
      return True
   else:
      return False   

print(pal([1,4,1]))  

#15 count +ve,-ve,0
def even(l1):
   p=0
   n=0
   z=0
   for i in l1:
      if i>0:
         p+=1
      elif i<0:
         n+=1
      else:
         z+=1
   return p,n,z

print(even([1,4,-2,-4,0,5,0]))   

#16

#16
lt = [0, 3, 5, 2, 4]

lt.sort()

print(lt[-2])

#17
lt = [0, 3, 5, 2, 4]

lt.sort()

print(lt[1])  

#18
def copy_list(lst):
   new_list = lst.copy()
   return new_list

print(copy_list([1,2,3]))

#19
def prime_no(lst):
   result=[]

   for num in lst:
      if num > 1:
         count = 0

         for i in range(1,num+1):
            if num%i==0:
               count +=1
         if count==2:
            result.append(num)

   return result

print(prime_no([1,2,3,4,5]))                  

#20 Replace all zeros wirh give number
def replace_zero(lst,value):
   for i in range(len(lst)):
      if lst[i] ==0:
         lst[i] = value
   return lst

print(replace_zero([0,2,0,4],-1))

#21
def check_same(lst):
   return len(set(lst)) == 1

print(check_same([5,5,5,5]))

lst=[5,5,5,5]

if lst.count(lst[0]) == len(lst):
   print(True)
else:
   print(False) 

#22
def freq(lst):
   result={}

   for i in lst:
      if i in result:
         result[i] +=1
      else:
         result[i] =1

   return result              

print(freq([1,2,2,3,1]))

#23
def flatten_list(lst):
   result=[]

   for i in lst:
      for j in i:
         result.append(j)
   return result

print(flatten_list([[1,2],[3,4]]))




#24 split list into even and odd

def even_odd(list):
   even=[]
   odd=[]

   for i in list:
      if i%2==0:
         even.append(i)
      else:
         odd.append(i)
   print("Even:",even)
   print("Odd:",odd)

even_odd([1,2,3,4,5])         

#25 find pair of elements with given sum
def summ(list,t):
   l=[]
   for i in list:
      for j in list:
         if i != j and (i+j)==t:
            pair=(i,j)
            if  pair not in l and (i,j) not in l:
               l.append(pair)
   return l

print(summ([1,2,3,4],5))    

#26 remove all odd numbers
def remove_odd(lst):
   result=[]

   for i in lst:
      if i%2==0:
         result.append(i)

   return result       

print(remove_odd([1,2,4,5,6]))

#27 remove all odd numbers
def remove_even(lst):
   result=[]

   for i in lst:
      if i%2!=0:
         result.append(i)

   return result       

print(remove_even([1,2,4,5,6]))

#28 multiply all elements with number
def multiply_list(lst,number):
   result=[]

   for i in lst:
      result.append(i*number)

   return result

print(multiply_list([1,2,3],2))

#29 diff b/w max and min 
def diff(lst):
   return max(lst)-min(lst)

print(diff([1,2,3,4,9]))

#30 
def check_empty(lst):
   return len(lst)==0
print(check_empty([])) 

#31
def insert_element(lst,index,value):
   lst.insert(index,value)
   return lst

print(insert_element([1,2,3,4,5],2,6))

#32
def remove_all(lst,value):
   result=[]

   for i in lst:
      if i!= value:
         result.append(i)

   return result                

print(remove_all([1,2,5,2,6],2))

#33
def find_index(lst,value):
   return lst.index(value)
print(find_index([10,20,30],20))

#34
def square_list(lst):
   result=[]

   for i in lst:
      result.append(i*i)

   return result
print(square_list([2,3,4]))

#35
def negative_ot(lst):
   result=[]

   for i in lst:
      if i<=0:
         result.append(i)

   return result
print(negative_ot([1,34,-3,12,0]))    

#36
def greater_value(lst,value):
   result=[]

   for i in lst:
      if i>value:
         result.append(i)
   return result
print(greater_value([1,3,5,7,9,5],6))      

#37
def find_duplicates(lst):
   result=[]

   for i in lst:
      if lst.count(i)>1 and i not in result:
         result.append(i)
   return result
print(find_duplicates([1,3,5,7,9,10,5,7]))

#39
def check_value(lst,value):
   return value in lst
print(check_value([1,2,3,4,6],4))

#40
def small_list(lst,size):
   result=[]

   for i in range(0,len(lst),size):
      result.append(lst[i:i+size])

   return result
print(small_list([1,2,3,4,5,6],2))


#set and dict problems
print("set and dict problems")

s={1,2,3,2,4}
print(s)

#1 add element
def add_element(s,value):
    s.add(value)
    return s
print(add_element({1,2,3},4))    

#2 remove element
def remove_element(s,value):
    s.remove(value)
    return s
print(remove_element({1,2,3,4,5},3))


#3 union a,b sets
def union_sets(a,b):
   return a | b
print(union_sets({28,8},{19,1}))

#4 intersection of a,b sets
def intersection_sets(a,b):
   return a & b
print(intersection_sets({1,2},{2,3}))

#5 difference  b/w sets
def difference_sets(a,b):
   return a - b
print(difference_sets({1,2,3},{2,3}))

#6 
def check_subset(a,b):
   return a.issubset(b)
print(check_subset({1,2},{1,2,3,4}))

#7 
def find_len(s):
   return len(s)
print(find_len({1,2,3}))   

#8
def clear_set(s):
    s.clear()
    return s
print(clear_set({1,3,4}))   

s={1,2,3}
print(s)
s.clear()
print(s)

#9
def symm_diff(a,b):
   return a ^ b

print(symm_diff({1,2,3},{2,3,4}))   

#10
def list_to_set(lst):
   return set(lst)

print(list_to_set([1,2,3,4,4,2]))

#Dictionary 
print("Dictionary questions")

#1
def create_dicts(keys,values):
   return dict(zip(keys,values))
print(create_dicts(["a","b"],[1,2]))  

#2
def update(d,key,value):
   d[key] = value
   return d
print(update({"a":1},"a",2))  

#3
def remove_key(d,key):
   d.pop(key)
   return d
print(remove_key({"a":1,"b":2},"b"))

#4
def check_key(d,key):
   return key in d

print(check_key({"x":1},"x"))

#5
def iterate_dict(d):
   for key,value in d.items():
      print(key,value)
iterate_dict({"a":10,"b":20})

#6
def dict_len(d):
   return len(d)

print(dict_len({"x":1,"y":2}))

#7
def merge_dict(a,b):
   a.update(b)
   return a
print(merge_dict({"a":1},{"b":2}))

#8
def get_value(d,key,default):
   return d.get(key,default)

print(get_value({"a":1},"b",0))

#9
def frequency(lst):
   result={}

   for i in lst:
      if i in result:
         result[i] +=1
      else:
         result[i]=1
   return result

print(frequency({1,2,3,3}))    

#10
def invert_dictionary(d):
    result = {}

    for key, value in d.items():
        result[value] = key

    return result

print(invert_dictionary({"a": 1, "b": 2}))

#11
def maximum_value_key(d):
    return max(d, key=d.get)

print(maximum_value_key({"a": 10, "b": 20, "c": 15}))

#12
def sort_dictionary(d):
    return sorted(d.items(), key=lambda x: x[1])

print(sort_dictionary({"a": 3, "b": 1, "c": 2}))

#13
def square_dictionary(numbers):
    result = {}

    for i in numbers:
        result[i] = i * i

    return result

print(square_dictionary(range(1, 4)))

#14
def filter_dictionary(d):
    result = {}

    for key, value in d.items():
        if value > 10:
            result[key] = value

    return result

print(filter_dictionary({"a": 10, "b": 5, "c": 15}))

#15
def combine_dictionaries(a, b):
    result = a.copy()

    for key, value in b.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result

print(combine_dictionaries(
    {"a": 1, "b": 2},
    {"a": 3, "c": 4}
))

#16
def word_frequency(text):
    result = {}

    words = text.split()

    for i in words:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result

print(word_frequency("apple banana apple"))

#17
def remove_duplicate_values(d):
    result = {}

    for key, value in d.items():
        if value not in result.values():
            result[key] = value

    return result

print(remove_duplicate_values({"a": 1, "b": 2, "c": 1}))

#18
def common_keys(a, b):
    result = []

    for key in a:
        if key in b:
            result.append(key)

    return result

print(common_keys({"a": 1, "b": 2}, {"b": 3, "c": 4}))

#19
def safe_invert(d):
    result = {}

    for key, value in d.items():
        if value in result:
            return "Values are not unique"

        result[value] = key

    return result

print(safe_invert({"x": 1, "y": 2}))

#20
def delete_by_value(d, value):
    result = {}

    for key, val in d.items():
        if val != value:
            result[key] = val

    return result

print(delete_by_value({"a": 1, "b": 2, "c": 1}, 1))
