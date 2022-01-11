`xfreerdp /u: /p: /size:1600x1000 /v:`

`git clone https://luct0r@<PROJECT>`

`grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" file.txt`

cat bloodhound_users.json | jq '.users[].Properties | select(.enabled=true) | .email' > users.txt

cat dehashed.json | jq '.[].fullName' > names.txt
