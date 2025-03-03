# Metasploitable 2 on Docker
Setup for running Metasploitable 2 on Mac Mini M2.

## Run Command
```bash
docker run -d -p 2222:22 --platform linux/amd64 --name metasploitable2 tleemcjr/metasploitable2 /bin/bash -c "service ssh start && tail -f /dev/null"
