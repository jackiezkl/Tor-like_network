VOLUMES = \
	--volume=`pwd`/docker_home_folder/results:/home/results\
	--volume=`pwd`/docker_home_folder/results/regular/screenshots:/home/results/regular/screenshots\
	--volume=`pwd`/docker_home_folder/results/tor/screenshots:/home/results/tor/screenshots\
	--volume=`pwd`/docker_home_folder/results/tor-like/screenshots:/home/results/tor-like/screenshots\
	--volume=`pwd`/docker_home_folder/Entrypoint.sh:/home/Entrypoint.sh\
	--volume=`pwd`/docker_home_folder/etc:/home/etc\
	--volume=`pwd`/docker_home_folder/action.py:/home/action.py\
	--volume=`pwd`/docker_home_folder/tor_action.py:/home/tor_action.py\
	--volume=`pwd`/docker_home_folder/tor_like_action.py:/home/tor_like_action.py
	
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
