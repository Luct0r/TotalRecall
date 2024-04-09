`xfreerdp /u: /p: /size:1600x1000 /v:`

`git clone https://luct0r@<PROJECT>`

`grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" file.txt`

`cat bloodhound_users.json | jq '.users[].Properties | select(.enabled=true) | .email' | tr -d '"' > users.txt`

`cat dehashed.json | jq '.[].fullName' > names.txt`

`while read line; do grep "${line//\"/}" FileToSearch; done < FileToRead | grep "Something"`

`grep -oE ".{0,15}@emaildomain.com.{0,1}" file.txt`

`socat TCP4-LISTEN:1234,fork TCP4:127.0.0.1:5678`
