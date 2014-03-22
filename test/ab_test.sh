#!/bin/bash
#===============================================================================
#
#          FILE:  test.sh
# 
#         USAGE:  ./test.sh 
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
#       CREATED:  2014年03月17日 22时04分00秒 CST
#      REVISION:  ---
#===============================================================================

ab -n $1 -c $2 "http://localhost:8080/tornadotest/"
