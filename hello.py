#1. kiểu dữ liệu
ten="bui tuan nhat" # chuỗi
print(ten[1:])
print(ten[:7])
print(ten[1:3])

tuoi= 20 # interger
print(type(tuoi)) # tìm kiểu dữ liệu


chieucao=1.75 # float(mét)
print(int(chieucao)) #ép kiểu: int,float,str,dict,tuple


ans=[1,2,3,4]
ds = ['nhat','dep','zai',20,1.75,ans] # list
ds[2]='trai'
print(ds[5]) # list lồng
del ds[2]
print(ds[0:4])
del ds # xóa list


day=('mon','tus','wed','thur','fri','sat','sun') # tuple
print(day[1:3]) #in như string
ngay = ()
thang =(1,)
# tuple không thể thay đổi, chỉ có thể ghép hoặc xóa cả
nam = thang + day
print(nam)


person = {
    'name': 'Vũ Thanh Tài',
    20: {
            'age': 22,
            'male': True,
            'status': 'alone'
        }        
}

print(person[20]['age'])
person.clear()
del person

# switch-case
a = 'ba'
dic = {
    'mot': 1,
    'hai': 2,
    'ba': 3,
}
print(dic.get('hai','khong ro'))

#if-else 
a = 100
if a==100:
    print("nhat dz")
else:
    print("nhat xz")


num = 4
if num < 100:
    print(num)
    if num % 2 == 0 and num > 5:
        print("Số chẵn")
    elif num < 5:
        print("nhat dz")
    hieu = num - 2
    print("hiệu số đã cho với 2 bằng", hieu)

ten = "buituannhat"
dem=0
for i in range(1,10): # i= 1->9
    dem+=1
    for j in ten:
        print(j,end =" ")
    print("") # xóa bỏ end để xuống dòng
print(dem)

for i in range(10,0,-1): # vòng lặp lùi
    print(i)

i=1
while(i<=10):
    j=0
    while(j<=10 - i):
        print(j, end = ' ')
        j+=1
    print('')
    if i % 2 == 1: break
    i+=1

ten= ('bui','tuan','nhat')
ngaysinh = [14,2,2002]
def doiten(haha,hihi):
    print(haha)
    print(hihi)
    hihi[0]=15
    haha="vui"
    print(haha)
    print(hihi)
doiten(ten,ngaysinh)

a="bui tuan nhat"
def doi():
    global a
    print(a)
    a="nguyen thi thanh tam"
doi()
print(a)

def sum(a, b):
   return a+ b

c = sum(4, 5)
print("Tong cua 4 va 5 = " ,c)