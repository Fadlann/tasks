class nilai_matkul:
    nim = None
    nama = None
    nilai = None

class element:
    def __init__(self):
        self.container = nilai_matkul()
        self.next = None
        
    def get_container(self):
        return self.container
    
    def set_next(self, nextt):
        self.next = nextt
    
    def get_next(self):
        return self.next
    
class list:
    def __init__(self):
        self.first = None
        self.data = []
        
        for i in range(0,10):
            self.data.append([])
            self.data[i] = element()
            
    def set_first(self, first):
        self.first = first
    
    def get_first(self):
        return self.first
    
    def create_list(self):
        self.first = -1
        for i in range(0, len(self.data)):
            self.data[i].set_next(-2)
            
    def count_element(self):
        result = 0
        if(self.first != -1):
            assist = self.first
            
            while assist != -1:
                result = result + 1
                assist = self.data[assist].get_next()
        return result
    
    def empty_element(self):
        result = -1
        
        if(self.count_element() < len(self.data)):
            found = False
            i=0
        
            while(found == False) and (i < len(self.data)):
                if(self.data[i].get_next() == -2):
                    result = i
                    found = True
                else:
                    i = i+1
            return result
        
    def add_first(self, nim, nama, nilai):
        if(self.count_element() < len(self.data)):
            new = self.empty_element()
            self.data[new].get_container().nim = nim
            self.data[new].get_container().nama = nama
            self.data[new].get_container().nilai = nilai
            
            if(self.first == -1):
                self.data[new].set_next(-1)
            else:
                self.data[new].set_next(self.first)
            self.first = new
        else:
            print('Sudah tidak dapat ditambah')
    
    def add_after(self, prev, nim, nama, nilai):
        if((self.count_element() < len(self.data)) and (prev != -1)):
            new = self.empty_element()
            self.data[new].get_container().nim = nim
            self.data[new].get_container().nama = nama
            self.data[new].get_container().nilai = nilai
            
            if(self.data[prev].get_next() == -1):
                self.data[new].set_next(-1)
            else:
                self.data[new].set_next(self.data[prev].get_next())
            self.data[prev].set_next(new)
            
        else:
            print('Sudah tidak dapat ditambah')
        
    def add_last(self, nim, nama, nilai):
        if(self.first == -1):
            self.add_first(nim, nama, nilai)
        else:
            last = self.first
            while self.data[last].get_next() != -1:
                last = self.data[last].get_next()
            self.add_after(last, nim, nama, nilai)
            
    def del_first(self):
        if(self.first != -1):
            delete = self.first
            if(self.count_element() == 1):
                self.first = -1
            else:
                self.first = self.data[self.first].get_next()
            self.data[delete].set_next(-2)
        else:
            print('List is empty!')
        
    def del_after(self, prev):
        if(prev != -1):
            delete = self.data[prev].get_next()
            if(delete != -1):
                if(self.data[delete].get_next() == -1):
                    self.data[prev].set_next(-1)
                else:
                    self.data[prev].set_next(self.data[delete].get_next())
                    
                self.data[delete].set_next(-2)
                
    def del_last(self):
        if(self.first != -1):
            if(self.count_element() == 1):
                self.del_first()
            else:
                last = self.first
                before_last = -1
                
                while self.data[last].get_next() != -1:
                    before_last = last
                    last = self.data[last].get_next()
                self.del_after(before_last)
        else:
            print('List is empty!')
    
    def print_element(self):
        if(self.first != -1):
            assist = self.first
            i = 1
            while assist != -1:
                print('Elemen [',i,'] : ')
                print('NIM \t: ', self.data[assist].get_container().nim)
                print('Nama \t: ', self.data[assist].get_container().nama)
                print('Nilai \t: ', self.data[assist].get_container().nilai)
                print('Next \t: ', self.data[assist].get_next())
                print(23*'-')
                assist = self.data[assist].get_next()
                i = i+1
        else:
            print('List is empty!')
            
    def del_all(self):
        for i in range(self.count_element(), 1, -1):
            self.del_last()

L = list()

L.create_list()
L.print_element()

print(23*'=')
print('    ADDING ELEMENTS')
print(23*'=')
L.add_first('048', 'Ajeng', 'A')
L.add_after(L.get_first(), '222', 'Granger', 'A-')
L.add_after(1, '190', 'Weasley', 'B+')
L.add_last('321', 'Brown', 'C')

L.print_element()

print(23*'=')
print('   REMOVING ELEMENTS')
print(23*'=')
L.del_last()
L.del_after(L.get_first())
L.del_first()
L.print_element()