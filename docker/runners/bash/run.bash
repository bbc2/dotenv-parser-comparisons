sed -i '1s/^/export /' .env
source .env
python3 env_util/print_env.py
