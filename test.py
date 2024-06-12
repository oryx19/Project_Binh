class inf:
    def __init__(self, mahv = None, hoten = None, namsinh = None, sex =None, bomon = None, so_thang_no =None, namthamgia = None):
        self.mahv = mahv
        self.hoten = hoten
        self.namsinh = namsinh
        self.sex = sex
        self.bomon = bomon
        self.so_thang_no =  so_thang_no
        self.namthamgia = namthamgia
        self.next = None

class menu:
    def __init__(self):
        self.head = inf()

    def them(self, mahv, hoten, namsinh, sex, bomon, so_thang_no, namthamgia):
        new_node = inf( mahv, hoten, namsinh, sex, bomon, so_thang_no, namthamgia)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
 
    def xoaten(self, hoten):
        cur_node = self.head
        while cur_node.next:
            if cur_node.next.hoten == hoten:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
    
    def xoamahv(self, mahv):
        cur_node = self.head
        while cur_node.next:
            if cur_node.next.mahv == mahv:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next

    def xoatheono(self, so_thang_no):
        cur_node = self.head
        while cur_node.next:
            if cur_node.next.so_thang_no == so_thang_no:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
            

    def timten(self, hoten):
        cur_node = self.head
        dem = 0
        while cur_node:
            if cur_node.hoten == hoten:
                dem += 1
                print(cur_node.mahv, cur_node.hoten, cur_node.namsinh, cur_node.sex, cur_node.bomon, "So thang no: ", cur_node.so_thang_no, "Nam tham gia:", cur_node.namthamgia) 
            cur_node = cur_node.next 
        if dem == 0:
            print(f"'{hoten}' khong co trong danh sach")   

    def timmahv(self, mahv):
        cur_node = self.head 
        dem = 0
        while cur_node: 
            if cur_node.mahv == mahv:
                dem += 1
                print("Thong tin cua",f"'{mahv}':",cur_node.mahv, cur_node.hoten, cur_node.namsinh, cur_node.sex, cur_node.bomon, "So thang no: ", cur_node.so_thang_no, "Nam tham gia:", cur_node.namthamgia) 
            cur_node = cur_node.next
        if dem == 0:
            print( f"'{mahv}' khong co trong danh sach" )
    def timmbomon(self, bomon):
        cur_node = self.head
        dem = 0
        while cur_node: 
            if cur_node.sex == sex:
                dem += 1
                print(cur_node.mahv, cur_node.hoten, cur_node.namsinh, cur_node.sex, cur_node.bomon, "So thang no: ", cur_node.so_thang_no, "Nam tham gia:", cur_node.namthamgia) 
            cur_node = cur_node.next
        if dem == 0:
            print( f"Danh sach khong co {bomon}" )

    def timmgioitinh(self, sex):
        cur_node = self.head
        dem = 0
        while cur_node: 
            if cur_node.sex == sex:
                dem += 1
                print(cur_node.mahv, cur_node.hoten, cur_node.namsinh, cur_node.sex, cur_node.bomon, "So thang no: ", cur_node.so_thang_no, "Nam tham gia:", cur_node.namthamgia) 
            cur_node = cur_node.next
        if dem == 0:
            print( f"Danh sach khong co {sex}" )

    def printbomon(self, bomon):
        cur_node = self.head
        dem = 0
        print("Danh sach mon",f"'{bomon}':")
        while cur_node: 
            if cur_node.bomon == bomon:
                dem += 1
                print(dem,cur_node.hoten) 
            cur_node = cur_node.next
        print("Danh sach co tong cong",f"{dem}","nguoi")

    def printbomon(self):
        list = set()
        cur_node = self.head.next
        while cur_node:
            list.add(cur_node.bomon)
            cur_node = cur_node.next
        for bomon in list:
            cur_node = self.head
            dem = 0
            print("Danh sach mon",f"'{bomon}':")
            while cur_node: 
                if cur_node.bomon == bomon:
                    dem += 1
                    print(dem,cur_node.hoten) 
                cur_node = cur_node.next
            print("Danh sach co tong cong",f"{dem}","nguoi")

    def printtheothoigian(self):
        cur_node = self.head.next
        list = set()
        while cur_node:
            list.add(cur_node.namthamgia)
            cur_node = cur_node.next
        tg = []
        for i in list:
            tg.append(int(i))
        print(tg)
        for i in range(len(list)-1):
            for t in range(i,len(list)):
                if tg[i]>tg[t]:
                    bien = tg[i]
                    tg[i] = tg[t]
                    tg[t] = bien
        print(tg)
        
        for nam in tg:
            cur_node = self.head.next
            print(nam)
            while cur_node: 
                if cur_node.namthamgia == nam:
                    print(cur_node.mahv, cur_node.hoten,"Nam tham gia:", cur_node.namthamgia) 
                cur_node = cur_node.next
        
    def printList(self):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next 
            print(cur_node.mahv, cur_node.hoten, cur_node.namsinh, cur_node.sex, cur_node.bomon,"So thang no: ", cur_node.so_thang_no, "Nam tham gia:", cur_node.namthamgia)

my_list = menu()


my_list.them("T1910","Dang Dinh Ngoc","2006","Nam","Toan",2,2020)

my_list.them("Ti1112","Van Ngoc Binh","2005","Nam","Tin",3,2021)

my_list.them("Li0903","Tran Phuong Thao","2006","Nu","Li",1,2020)

my_list.them("T1211","Phan Cong Dang Khoa","2006","Nam","Toan",3,2020)

my_list.them("V0902","Vo Thi Hong Anh","2006","Nu","Van",2,2019)

my_list.them("Ti0502","Phan Cong Dang Khoa","2007","Nam","Tin",4,2024)

#my_list.xoamahv("Ti1112")

#my_list.xoaten("Dang Dinh Ngoc")

#my_list.xoatheono(3)

#my_list.printList()

#my_list.timten("Dang Dinh Ngoc")

#my_list.timten("Phan Cong Dang Khoa")

#my_list.timmgioitinh("Nam")

#my_list.printbomon()

my_list.printtheothoigian()