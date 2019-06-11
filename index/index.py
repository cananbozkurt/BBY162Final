

class Kitap() :
    def __init__(self,writer,bookname,date):
        self.bookname = bookname
        self.writer = writer
        self.date = date
def main():
    Booklist = []

    with open("input.txt","r") as file:
        content=file.readlines()
        for i in content:
            case=i.strip().split("\t")
            Booklist.append(Kitap(case[0].strip("\t"),case[1].strip("\t"),case[2].strip("\t")))
    file.close()
    f=open("input.txt","w")
    bool=True
    while(bool==True):
        print(
              "1.Yeni Kayıt Oluştur\n2.Kitabın Adına Göre Arama\n3.Yazarın Adına Göre Arama\n4.Kitabın Tarihine Göre Arama\n5.Çıkış\n")
        myinput=input("Lütfen yapmak istediğiniz işlemi seçiniz:")
        ex=int(myinput)
        if(ex==1):
            authorname=input("Please enter the author name for new register :")
            namebook=input("Please enter the book name for new register :")
            registerdate=input("Please enter the book name for new register :")
            for info in Booklist:
                if(info.date==registerdate and info.bookname==namebook and info.writer==authorname):
                    print ("Bu bilgiler kayıtlı olan bir kitaba aittir")
                    continue
            Booklist.append(Kitap(authorname,namebook,registerdate))
        elif(ex==2):
            count=0
            serachauthor=input("Please enter the author name for search : ")
            for i in Booklist:
                if i.writer==serachauthor:
                    print ("writer name :",i.writer, "Book name :",i.bookname, " Date : ",i.date,sep="\t")
                    count+=1
            if(count==0):
                print (serachauthor+" isimli yazara ait bilgi bulunmamaktadır ")

        elif (ex==3):
            counter=0
            serachbook=input("Please enter the book name for search: ")
            for i in Booklist:
                if i.bookname == serachbook:
                    print ("writer name :" , i.writer, "Book name :" , i.bookname, " Date : " ,i.date, sep="\t")
                    counter+=1
            if(counter==0):
                print (serachbook+" isimli kitaba ait bilgi bulunmamaktadır !!!")

        elif(ex==4):
            count2=0
            serachdate=input("Please enter the date for search : ")
            for i in Booklist:
                if i.date == serachdate:
                    print ("writer name :" ,i.writer, "Book name :" , i.bookname, " Date : " ,i.date, sep="\t")
                    count2+=1
            if(count2==0):
                print ("Bu tarihe ait bilgi nulunmamaktadır")
        elif(ex==5):
            bool=False
        else:
            print ("Lütfen geçerli bir numara giriniz!!!")
    for i in Booklist:
        Str=""
        Str+=i.writer+"\t"+i.bookname+"\t"+i.date+"\n"
        f.writelines(Str)

if __name__ == '__main__':

    main()