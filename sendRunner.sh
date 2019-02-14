
echo $1 > temp.nc
python gcodesender.py -p COM4 -f temp.nc