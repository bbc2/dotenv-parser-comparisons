sed -i '1s/^/export /' .env
source .env
python ../../printenv/printenv.py
