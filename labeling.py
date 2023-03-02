import sys
import glob
import os

# process sequence get a number of files in folder
# be cautious except folder only files
# sort the files and get a name of first files name
# copy from first file name ~ rnage(number of files in folder)


def get_files_count(folder_path):
	filelist = os.listdir(folder_path) #경로에있는 파일 리스트 만들기
	jpegfile=[file for file in filelist if file.endswith(".jpeg")] #확장자명이르 끝나는 파일들만 생성
	jpegfile.sort() #오름차순으로 정렬
	print(jpegfile)
	print('first name:',jpegfile[0]) 
	firstn=jpegfile[0]	#첫번째 이미지 파일 이름
	a=firstn.split('_')[0] #'_'기준으로 쪼개기
	print('qweqwe:',a)
	firstn=int(a)		#첫순자만 가져오기
	endnum=firstn+len(jpegfile)-1
	return firstn,endnum,jpegfile


def lblgen(jpegfile):
	for i in jpegfile:#jpegfile list
	
		txtname=i.split('.') #for getting except .jpeg
		
		
		txtname=txtname[0]+'.txt' #define text file new name
		pathandname=lblpath+txtname #link path and txtname
		#pathandname=os.path.join(lblpath,txtname)
		fwr=open(pathandname,'w') #open txt file
		fwr.write("5") # write class number
		fwr.close # close & save
	return


	

imgpath='/home/N'
lblpath='/home/'


stn,endnum,jpegfile=get_files_count(imgpath)
lblgen(jpegfile)





