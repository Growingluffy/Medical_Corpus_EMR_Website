#构建词典
import codecs
#文件及地址定义
datadir = './medical_dict'
filename1 = datadir+'/'+'disease_dict_col.txt'
filename2 = datadir+'/'+'treatment_dict_col.txt'
filename3 = datadir+'/'+'symptom_dict_col.txt'
filename4 = datadir+'/'+'body_dict_col.txt'
filename5 = datadir+'/'+'check_dict_col.txt'
def read_line_file():
    #文件定义
    file = 'medical_labeled_manual.txt'

    #分类写入
    with open(file,'r',encoding='utf-8') as f:
        line = f.readlines()
        for i in range(len(line)):
            word = line[i].strip().split('\t')
            #print(word)
            if word[3] == "疾病和诊断":
                d = codecs.open(filename1,'a',encoding='utf-8')
                d.writelines(word[0])
                d.write('\n')
            if word[3] == "身体部位":
                d = codecs.open(filename4,'a',encoding='utf-8')
                d.write(word[0])
                d.write('\n')
            if word[3] == "治疗":
                d = codecs.open(filename2,'a',encoding='utf-8')
                d.write(word[0])
                d.write('\n')
            if word[3] == "检查和检验":
                d = codecs.open(filename5,'a',encoding='utf-8')
                d.write(word[0])
                d.write('\n')
            if word[3] == "症状和体征":
                d = codecs.open(filename3,'a',encoding='utf-8')
                d.write(word[0])
                d.write('\n')
                  
    print("Dict build success!")
#写入一个字典文件
def write_one():
    file = datadir+'/'+'EMR_dict.txt'
    with open(file,'a',encoding='utf-8') as f:
        with open(filename1,'r',encoding='utf-8') as f1,open(filename2,'r',encoding='utf-8') as f2, \
        open(filename3,'r',encoding='utf-8') as f3, open(filename4,'r',encoding='utf-8') as f4, \
        open(filename5,'r',encoding='utf-8') as f5:
            line = f1.readlines()
            for i in range(len(line)):
                word = line[i].strip().split('\t')[0]
                #print(word)
                f.write(word)
                f.write('\n')
            print("疾病和诊断 Dict Build Success!")
            line = f2.readlines()
            for i in range(len(line)):
                word = line[i].strip().split('\t')[0]
                #print(word)
                f.write(word)
                f.write('\n')
            print("身体部位 Dict Build Success!")
            line = f3.readlines()
            for i in range(len(line)):
                word = line[i].strip().split('\t')[0]
                #print(word)
                f.write(word)
                f.write('\n')
            print("治疗 Dict Build Success!")
            line = f4.readlines()
            for i in range(len(line)):
                word = line[i].strip().split('\t')[0]
                #print(word)
                f.write(word)
                f.write('\n')
            print("检查和检验 Dict Build Success!")
            line = f5.readlines()
            for i in range(len(line)):
                word = line[i].strip().split('\t')[0]
                #print(word)
                f.write(word)
                f.write('\n')
            print("症状和体征 Dict Build Success!")
    print("EMR Dict Build Success!")
    
                
if __name__=="__main__":
    write_one()