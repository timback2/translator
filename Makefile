all: create_env

create_env:
	conda create --name py310translator python=3.10

enable_env: 
	conda activate py310translator

install_dependencies:
	pip install -r requirements.txt
