#Project GOTO
##Synopsis
An efficient alternative to the cd command in unix based systems
##Installation
<ol>
<li>Clone the Github repo<br></li>
<li>Run initdata.py:<br>
<script>$python3 initdata.py</script><br></li>
<li>Append the path of the project folder to PATH variable in /etc/environment:<br>
<script>sudo gedit /etc/environment</script><br></li>
<li>Run it!<br>
<script>$goto NameOfFolder</script><br></li>
<li>You're good to go!</li>
</ol>
##Positional Arguments
<script>$goto < -dk | --dont-kill > < DirName ></script><br>
<ul>
<li>< DirName >: Name of Directory you want to visit</li>
<li>< -dk | --dont-kill >: pass it if you don't want current terminal window to be killed</li>
</ul>
##Enjoy!
