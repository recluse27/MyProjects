import numpy
import pandas
import gdal
import tarfile
import os


#-------------------------EXTRACTING-------------------------	
tar1 = tarfile.open("LC81810252015208LGN01.tar.gz", "r:gz")
filelist=tar1.getnames()
path2="/home/jack/lab4_spec_prog/"+str(filelist[2])+"/"+str(filelist[2])
#os.mkdir("/home/jack/lab4_spec_prog")
# for j in filelist:
# 	path="/home/jack/lab4_spec_prog/"+str(j)
# 	os.mkdir(path)
# 	tar1.extract(j, path)
tar2 = tarfile.open("LC81820242016138LGN00.tar.gz", "r:gz")
filelist=tar2.getnames()
#for j in filelist:
	# path="/home/jack/lab4_spec_prog/"+str(j)
	# os.mkdir(path)
	# tar2.extract(j, path)
#-------------------------EXTRACTING-------------------------	
#-------------------------REPROJECTION-------------------------	
path="/home/jack/lab4_spec_prog/"+str(filelist[2])+"/"+str(filelist[2])
# command='gdalwarp -tr 1000 1000 -t_srs "+proj=utm +zone=36" '+path+' reproject.tif'
# print(command)
# os.system(command)
#-------------------------REPROJECTION-------------------------	
#-------------------------VEKTOR-------------------------	
#command="gdalwarp -tr 1000 1000 -te 10 10 900 900 "
#command=command+path+" vektor.tif"
#-------------------------VEKTOR-------------------------	
#-------------------------CONCATENATION-------------------------
command='gdalwarp -of GTIFF -ot Uint16 -srcnodata 5 -dstnodata 5 '+path+' '+path2+' concat.tif'
print(command)
os.system(command)
#-------------------------CONCATENATION-------------------------	