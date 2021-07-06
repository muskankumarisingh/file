a=open("saral3.text","w")
bank_list=["kotak","HDFC","RBL","SBI","Bank of Baroda"]
i=0
while i<len(bank_list):
    a.write(bank_list[i])
    a.write("\n")
    i=i+1
a.close()
