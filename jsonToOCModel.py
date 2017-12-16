#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

import datetime

import os

descroptionTemplate = """
/**
 <#Description#>
 */
"""

path = "/Users/yoser/Desktop/temp.json"

modelPath = "/Users/yoser/Desktop/"

floatProperty      = "@property (nonatomic, assign) CGFloat "

integerProperty    = "@property (nonatomic, assign) NSInteger "

boolProperty       = "@property (nonatomic, assign) BOOL "

stringProperty     = "@property (nonatomic, copy, nullable) NSString *"

arrayProperty      = "@property (nonatomic, strong, nullable) NSArray *"

dictionaryProperty = "@property (nonatomic, strong, nullable) NSDictionary *"

# 依次填入
# 1.Model文件名
# 2.项目名称
# 3.创建时间
# 4.Model名
model_hTemplateStart = """
//
//  %s.h
//  %s
//
//  Created by yoser on %s.
//  Copyright © 2017年 yoser. All rights reserved.
//


#import <Foundation/Foundation.h>

@interface %s : NSObject


"""

model_hTemplateEnd = """
@end

"""


model_mTemplate = """
//
//  %s.m
//  %s
//
//  Created by yoser on %s.
//  Copyright © 2017年 yoser. All rights reserved.
//

#import "%s.h"

@implementation %s

@end

"""

def addDesc(content):
    content += descroptionTemplate
    return content


def getCurrentDate():
    currentDate = datetime.datetime.now()
    currentDateStr = currentDate.strftime("%Y/%m/%d")
    return currentDateStr


def writeStringToFile(filePath,string):

    with open(filePath,"w", encoding="utf-8") as file:
        file.write(string)

def jsonToOCModel(jsonPath, modelPath, modelName, projectName ,needDesc = False):

    # write .h

    h_file_content = ""

    h_modelPath = modelPath + modelName + ".h"

    with open(jsonPath, encoding="utf-8") as jsonFile:

        jsonModel = json.load(jsonFile)

        h_file_content = model_hTemplateStart + "\n"

        for key,value in jsonModel.items():

            if type(value) is int:
                h_file_content = addDesc(h_file_content)
                h_file_content += (integerProperty + key + ";\n\n")
            if type(value) is float:
                h_file_content = addDesc(h_file_content)
                h_file_content += (floatProperty + key + ";\n\n")
            if type(value) is str:
                h_file_content = addDesc(h_file_content)
                h_file_content += (stringProperty + key + ";\n\n")
            if type(value) is dict:
                h_file_content = addDesc(h_file_content)
                h_file_content += (dictionaryProperty + key + ";\n\n")
            if type(value) is list:
                h_file_content = addDesc(h_file_content)
                h_file_content += (arrayProperty + key + ";\n\n")
            if type(value) is bool:
                h_file_content = addDesc(h_file_content)
                h_file_content += (boolProperty + key + ";\n\n")

        h_file_content += model_hTemplateEnd

    currentDateStr = getCurrentDate()

    h_file_content = h_file_content % (modelName,projectName,currentDateStr,modelName)

    writeStringToFile(h_modelPath, h_file_content)

    # write .m

    m_model_Path = modelPath + modelName + ".m"

    m_file_content = model_mTemplate % (modelName,projectName,currentDateStr,modelName,modelName)

    writeStringToFile(m_model_Path, m_file_content)

    print("Json to Model Success")


if __name__ == "__main__":

    print("1.请输入Json文件的路径")
    jsonPath = input()

    print("2.请输入Model名称")
    modelName = input()

    print("3.请输入项目名称")
    projectName = input()

    print("4.请输入Model的输出路径")
    modelPath = input()

    jsonToOCModel(jsonPath, modelPath, modelName, projectName, needDesc = True)