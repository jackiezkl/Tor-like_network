VOLUMES = \
	--volume=`pwd`/docker_home_folder/results:/home/results\
	--volume=`pwd`/docker_home_folder/Entrypoint.sh:/home/Entrypoint.sh\
	--volume=`pwd`/docker_home_folder/etc:/home/etc\
	--volume=`pwd`/docker_home_folder/action.py:/home/action.py
	
build:
	@docker build -t seleniumnode --rm .

run:
	@docker run -it --rm --privileged --name selenium ${VOLUMES} seleniumnode /home/Entrypoint.sh $(arg1) $(arg2)

destroy:
	@docker rmi seleniumnode

delete:
	@docker rm `docker ps -a -q`
	
stop:
	@docker stop `docker ps -a -q`

cmd:
	@docker run -it --rm --entrypoint /bin/sh seleniumnode
