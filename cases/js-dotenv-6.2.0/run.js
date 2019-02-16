require('dotenv').config()
const { execSync } = require('child_process');

process.stdout.write(execSync('python ../../printenv/printenv.py').toString())
