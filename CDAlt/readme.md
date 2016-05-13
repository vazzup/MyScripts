#Project GOTO
##Synopsis
An efficient alternative to the cd command in unix based systems
##Installation
<ol>
<li>Clone the Github repo<br></li>
<li>Run initdata.py:<br>
<code>$python3 initdata.py</code><br></li>
<li>Append the path of the project folder to PATH variable in /etc/environment:<br>
<code>sudo gedit /etc/environment</code><br></li>
<li>Run it!<br>
<code>$goto NameOfFolder</code><br></li>
<li>You're good to go!</li>
</ol>
##Positional Arguments
<code>$goto < -dk | --dont-kill > < DirName ></code><br>
<ul>
<li>< DirName >: Name of Directory you want to visit</li>
<li>< -dk | --dont-kill >: pass it if you don't want current terminal window to be killed</li>
</ul>
##Enjoy!
