#!/bin/bash

# fast git
if [[ $1 == 'fg' ]];then
	#git add *
	git commit -am "update"
	git push origin master
    git push heroku master
fi
