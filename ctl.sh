#!/bin/bash
#===============================================================================
#
#          FILE:  ctl.sh
# 
#         USAGE:  ./ctl.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  chenbaiheng (), 465299904@qq.com
#       COMPANY:  x
#       VERSION:  1.0
#       CREATED:  2014年03月17日 22时12分44秒 CST
#      REVISION:  ---
#===============================================================================
start_num=10090
end_num=10100
server_name="tornadotest"

start()
{
	supervisorctl update
}

restart()
{
	for((i=${start_num};i<${end_num};i++))
	do
		num=`printf ":%02d" $i`
		supervisorctl restart ${server_name}${num}
	done
}

update()
{
	supervisorctl update
}

status()
{
	for((i=${start_num};i<${end_num};i++))
	do
		num=`printf ":%02d" $i`
		supervisorctl status ${server_name}${num}
	done
}

kill()
{
	for((i=${start_num};i<${end_num};i++))
	do
		num=`printf ":%02d" $i`
		supervisorctl kill ${server_name}${num}
	done
}

if [ $# -eq 0 ];then
	printf "params (start|restart|update|status|kill) \n"
else
	"$1"
fi
