import openpyxl

def Excel(file_name, lie, wei, change, th, hang):
    wb = openpyxl.load_workbook(file_name)
    sheet = wb.worksheets[0]
    flag = 1        #标志从第几行开始，以及测试暂停用
    for i in sheet.values:
        if(flag>hang-1):
            temp = i[lie[0]]
            sheet[lie[1]+str(flag)] = temp[:wei-1]+th*change+temp[wei-1+change:]
            #print("修改前%s，修改后%s"%(i[lie[0]],sheet[lie[1]+str(flag)].value))
        flag+=1
        #测试用
        #if(flag>20):
           # break
    wb.save(file_name)

if __name__ == "__main__":
    file_name = '资料表.xlsx'   #文件名称
    lie = [1,'B']   # A是第0列,B是第1列      #第几列的内容
    wei = 1         #第几位的内容开始修改,从1开始
    change = 18      #修改其后的几位
    th = '0'        #修改成什么
    hang = 2        #第几行开始
    Excel(file_name, lie, wei, change, th, hang)
    
#身份证从第7位开始，后10位改为*
