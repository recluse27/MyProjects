::for /f "tokens=1 delims=." %%d in ('dir /b /d *tar.gz') do (
::md %%d
::@echo Directory %%~nd Created
::"C:\Program Files\7-Zip\7z.exe"  x %%d.tar.gz
::"C:\Program Files\7-Zip\7z.exe"  x -o%%~nd %%d.tar
::del /S %%d.tar
::@echo Archive %%~nd %%d.tar.gz uncompressed
::)

cd LE71820252015239NSG00
gdal_merge.py -o output.tif -separate LE71820252015239NSG00_B1.TIF LE71820252015239NSG00_B2.TIF LE71820252015239NSG00_B3.TIF LE71820252015239NSG00_B4.TIF LE71820252015239NSG00_B5.TIF 
gdalwarp.exe -tr 80 -80 -t_srs "+proj=utm +zone=36" output.tif projected.tif
cd ..

cd LE71820262015239NSG00
gdal_merge.py -o output.tif -separate LE71820262015239NSG00_B1.TIF LE71820262015239NSG00_B2.TIF LE71820262015239NSG00_B3.TIF LE71820262015239NSG00_B4.TIF LE71820262015239NSG00_B5.TIF 
gdalwarp.exe -tr 80 -80 -t_srs "+proj=utm +zone=36" output.tif projected.tif
cd ..

gdal_merge.py -ps 10 10 -o merged.tif LE71820252015239NSG00\LE71820252015239NSG00_B1.TIF LE71820262015239NSG00\LE71820262015239NSG00_B1.TIF
gdalwarp -tr 10 10 -r bilinear LE71820252015239NSG00\LE71820252015239NSG00_B1.TIF LE71820262015239NSG00\LE71820262015239NSG00_B1.TIF merged11.tif 


gdalwarp -dstnodata 0 -q -cutline shp\polygon.shp -crop_to_cutline -of GTiff merged11.tif cutted.tif
pause 