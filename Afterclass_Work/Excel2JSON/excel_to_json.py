# -*- coding: UTF-8 -*-
# Function: 把Excel表单转化为json文件
import xlrd
import json
import codecs
import os


# 把excel表格中指定的sheet转为json
def Excel2Json(file_path):
	# 打开excel文件
    if get_data(file_path) is not None:
        book = get_data(file_path)
        #抓取所有sheet页的名称
        worksheets = book.sheet_names()
        print ("该Excel包含的表单列表为：\n")
        for sheet in worksheets:
            print('%s,%s' %(worksheets.index(sheet),sheet))
        inp = input(u'请输入表单名对应的编号，对应表单将自动转为json:\n')
        sheet = book.sheet_by_index(int(inp))
        row_0 = sheet.row(0)   # 第1行是表单标题
        col_0 = sheet.col(0)   # 第1列是类别
        nrows = sheet.nrows   # 行号
        ncols = sheet.ncols   # 列号

        result = {}    # 定义json对象

        # 遍历所有行将excel转化为json
        for i in range(1, nrows):
            # 第一层字典的key
            name = str(sheet.row_values(i)[0])
            # 定义第二层字典
            result[name] = {}
            for j in range(1, ncols):
                # 第二层字典的key
                year = str(sheet.row_values(0)[j])
                # 第二层字典的value
                result[name][year] = sheet.row_values(i)[j]
        # ensure_ascii=False保证中文编码不乱码
        json_data = json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False)

        saveFile(os.getcwd(),worksheets[int(inp)],json_data)
        print (json_data)


def get_data(file_path):
	try:
		data = xlrd.open_workbook(file_path)
		return data
	except Exception as e:
		print (u'excel表格数据读取失败：%s' %e)
		return None

def saveFile(file_path, file_name, data):
	output = codecs.open(file_path+"/"+file_name+".json","w","utf-8")
	output.write(data)
	output.close()

if __name__=='__main__':
	file_path = input(u'请输入excel文件路径：\n')
	json_data = Excel2Json(file_path)