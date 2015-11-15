echo "Enter question number"
read qno
echo $qno > temp.txt
#./ini < temp.txt
gnome-terminal -e "python ini.py "
#if [ ! -d "$qno" ]
#then 
#   exit
#fi
chmod -R 777 $qno
subl ./$qno
subl $qno/prog.cpp
alias xdg-open="xdg-open 2>/dev/null"
xdg-open http://acm.timus.ru/problem.aspx?num=$qno
