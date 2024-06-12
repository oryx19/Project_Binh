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

    def hienmenu(self):
        print()
        print("--MENU--")
        print("•Them")
        print("•Xoa")
        print("•Tim")
        print("•In")
        print("•Thoat")
        lenh = input("Nhap thao tac muon su dung: ")
        return lenh

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
    def timbomon(self, bomon):
        cur_node = self.head
        dem = 0
        while cur_node: 
            if cur_node.bomon == bomon:
                dem += 1
                print(cur_node.mahv, cur_node.hoten, cur_node.namsinh, cur_node.sex, cur_node.bomon, "So thang no: ", cur_node.so_thang_no, "Nam tham gia:", cur_node.namthamgia) 
            cur_node = cur_node.next
        if dem == 0:
            print( f"Danh sach khong co {bomon}" )

    def timgioitinh(self, sex):
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

        for i in range(len(list)-1):
            for t in range(i,len(list)):
                if tg[i]>tg[t]:
                    bien = tg[i]
                    tg[i] = tg[t]
                    tg[t] = bien
        
        for nam in tg:
            cur_node = self.head.next
            print(nam)
            while cur_node: 
                if cur_node.namthamgia == nam:
                    print(cur_node.mahv, cur_node.hoten,"Nam tham gia:", cur_node.namthamgia) 
                cur_node = cur_node.next
        
    def printdanhsach(self):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next 
            print(cur_node.mahv, cur_node.hoten, cur_node.namsinh, cur_node.sex, cur_node.bomon,"So thang no: ", cur_node.so_thang_no, "Nam tham gia:", cur_node.namthamgia)
    
def main():
    while True:
        ds = menu()
        dlvao = ds.hienmenu()
        print()

        #Them
        if dlvao == "Them":
            print("--THEM HOI VIEN--")
            print()
            mahv = input("  Nhap ma hoi vien: ")
            hoten = input(" Nhap ho va ten: ")
            namsinh = input(" Nhap nam sinh: ")
            sex = input(" Nhap gioi tinh: ")
            bomon = input(" Nhap bo mon: ")
            namthamgia = int(input(" Nhap nam tham gia: "))
            so_thang_no = int(input(" Nhap so thang no phi: "))
            ds.them(mahv, hoten, namsinh, sex, bomon, so_thang_no, namthamgia)
            print()
            print("**DA THEM HOI VIEN**")

        #Xoa
        elif dlvao == "Xoa":
            print()
            print("--XOA HOI VIEN--")
            print()
            print("Xoa theo ?") 
            print("Ho ten, MaHV, No phi")
            xoa =input("Nhap: ")
            if xoa == "Ho ten":
                hotenxoa = input("Nhap Ho ten: ")
                ds.xoaten(hotenxoa)
                print("**DONE**")
            elif xoa == "MaHV":
                mahvxoa = input("Nhap MaHV: ")
                ds.xoamahv(mahvxoa)
                print("**DONE**")
            elif xoa == "No phi":
                nophixoa = input("Nhap so thang no phi: ")
                ds.xoatheono(nophixoa)
                print("**DONE**")
            else:
                print()
                print("!!VUI LONG NHAP THEO CU PHAP!!")
                continue
        
        #Tim 
        elif dlvao == "Tim":
            print("--TIM KIEM VA IN THONG TIN HOI VIEN--")
            print()
            print("Tim theo ?")
            print("Ho ten, Bo mon, MaHV, Gioi tinh")
            tim =input("Nhap: ")
            if tim == "Ho ten":
                hotentim = input("Nhap Ho ten: ")
                print("Tim kiem va in thong tin cua",f"'{hotentim}'")
                ds.timten(hotentim)
                print("**DONE**")
            elif tim == "MaHV":
                mahvtim = input("Nhap MaHV: ")
                print("Tim kiem va in thong tin cua",f"'{mahvtim}'")
                ds.timmahv(mahvtim)
                print("**DONE**")
            elif tim == "Bo mon":
                bomontim = input("Nhap Bo mon: ")
                print("Tim kiem va in thong tin theo bo mon",f"'{bomontim}'")
                ds.timbomon(bomontim)
                print("**DONE**")
            elif tim == "Gioi tinh":
                gioitinhtim = input("Nhap Bo mon: ")
                print("Tim kiem va in thong tin theo gioi tinh",f"'{gioitinhtim}'")
                ds.timgioitinh(gioitinhtim)
                print("**DONE**")
            else:
                print()
                print("!!VUI LONG NHAP THEO CU PHAP!!")

        #In
        elif dlvao == "In":
            print("--IN DANH SACH--")
            print()
            print("In danh sach theo ?")
            print("Bo mon, Lau nam, Toan bo")
            inds = input("Nhap: ")
            if inds =="Bo mon":
                print()
                print("IN DANH SACH BO MON")
                print()
                ds.printbomon()
                print("**DONE**")
            elif inds == "Lau nam":
                print()
                print("IN DANH SACH TOAN BO HOI VIEN THEO THU TU LAU NAM NHAT XUAT HIEN TRUOC NHAT")
                print()
                ds.printtheothoigian()
            elif inds == "Toan bo":
                print()
                print("IN TOAN BO DANH SACH")
                ds.printdanhsach()
                print("**DONE**")
            else:
                print()
                print("!!VUI LONG NHAP THEO CU PHAP!!")

        #Thoat
        elif dlvao == "Thoat":
            print("Ban muon thoat chuong trinh (Y/N) ?")
            thoat = input()
            if thoat == "Y":
                break
            elif thoat =="N":
                continue
            else:
                print()
                print("!!VUI LONG NHAP THEO CU PHAP!!")
        else:
            print()
            print("!!VUI LONG NHAP THEO CU PHAP!!")
    
#Run
if __name__ == '__main__':
    main()





