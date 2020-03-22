require('dotenv').config()
const { execSync } = require('child_process');

process.stdout.write(execSync('python3 env_util/print_env.py').toString())
