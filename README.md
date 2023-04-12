<h1>Introduce</h1>
A server was injected a backdoor program, but the server manager can't find it,
and since there have some reasons, so can not change the server temporarily.
<br/>
So the temporary solution is auto detect the directory which have evil code, and move it to the other place or remove it.

<h2>Execution</h2>

auto execute per 60 minutes over the root privileges with the crontab： `sudo crontab -e`  : `*/60 * * * * python3 /xxx/check_hack.py`
