# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:40:36 2019

@author: h
"""

import jieba
sentence = '患者缘于5小时前不慎摔伤，伤及右髋部。伤后患者自感伤处疼痛，呼我院120接来我院，查左髋部X光片示：左侧粗隆间骨折。给予补液等对症治疗。患者病情平稳，以左侧粗隆间骨折介绍入院。患者自入院以来，无发热，无头晕头痛，无恶心呕吐，无胸闷心悸，饮食可，小便正常，未排大便。4.查体：T36.1C，P87次/分，R18次/分，BP150/93mmHg,心肺查体未见明显异常，专科情况：右下肢短缩畸形约2cm，右髋部外旋内收畸形，右髋部压痛明显，叩击痛阳性,右髋关节活动受限。右足背动脉波动好，足趾感觉运动正常。5.辅助检查：本院右髋关节正位片：右侧股骨粗隆间骨折'
def segment_word_test():

    list0 = jieba.cut(sentence, cut_all=True)
    print('全模式'+':\n'+'/'.join(list0))

    list1 = jieba.cut(sentence, cut_all=False)
    print('精准模式', list(list1))

    list2 = jieba.cut_for_search(sentence)
    print('搜索引擎模式', list(list2))

#加载用户词典方式
    #jieba.load_userdict('./medical_dict/disease_dict_col.txt')
    jieba.load_userdict('./medical_dict/EMR_dict.txt')

#jieba分词应用
import re
def segment_word_real():
      stopwords ={}
      fstop = open('stop_word.txt','r',encoding='utf-8',errors='ingnore')
      for eachWord in fstop:
          stopwords[eachWord.strip()] = eachWord.strip() #停用词典
      fstop.close()
      file_unsegment = open('./medical_ublabeled.original.txt','r',encoding='utf-8',errors='ignore')
      file_segment = open('./segment_word2vec/medical_segment.txt','w',encoding='utf-8')
      line = file_unsegment.readline()
      while line:
          line = str(line)
          line = line.strip()
          line = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+"," ", line)
          seg_list = jieba.cut_for_search(line)
          outStr = ""
          print("开始分词.....")
          for word in seg_list:
              if word not in stopwords:
                  outStr += word
                  #print(outStr)
                  outStr +=" "
          
          #print('Segment: ',outStr)
          file_segment.write(outStr)
          line = file_unsegment.readline()
      print("Segment Success!")

#对分此后的未标注电子病历数据进行词向量训练
from gensim.models import word2vec
import logging 
file = './segment_word2vec/medical_segment.txt'
def EMR_word2vec():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
    sentences = word2vec.Text8Corpus(file)
    model = word2vec.Word2Vec(sentences,size=300)
    #print(model)
    #model.save("./segment_word2vec/EMR_100.model")
    #print("Word2Vec Train Success!")
#计算词的相似度
def word2vec_apply():
    model = word2vec.Word2Vec.load("./segment_word2vec/EMR_300.model")
    #计算两个词的相似度，相关程度
    try:
        m1 = model.wv.similarity("高血压","心脏病")
    except KeyError:
        m1 =0
    print("高血压与心脏病的相似度为:",m1)
    print("***************************\n")
    #计算某个词的相关词列表
    m2 = model.wv.most_similar("疾病",topn=20)#topn个最相关的
    print("与疾病最相关的词有: \n")
    for item in m2:
        print(item[0],item[1])
    print("***************************\n")
    #寻找对应关系
    m3 = model.wv.most_similar([u'慢性病',u'胃炎'],[u'急性'],topn=3)
    print("对应关系如:\n")
    for item in m3:
        print(item[0],item[1])
    print("***************************\n")
    #寻找不合群的词
    m4 = model.wv.doesnt_match("先天性 慢性 急性 治疗 检查 ".split())
    print("不合群的词有:\n")
    print(m4)
    print("***************************\n")    
    
    
    
if __name__=="__main__":
    word2vec_apply()
    