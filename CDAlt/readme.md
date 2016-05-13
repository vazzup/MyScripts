#Project GOTO
##Synopsis
An efficient alternative to the cd command in unix based systems. No more typing /This/is/one/hell/of/a/long/path!<br>
Just goto DirectoryName!<br>
Note: The script opens a new terminal at the mentioned directory. If you've added new folders since running the initdata.py script, you should run it again to update the database.<br>
##Installation
<ol>
<li>Clone the Github repo<br></li>
<li>Run initdata.py:<br>
<code>$python3 initdata.py</code><br></li>
<li>Append the path of the project folder to PATH variable in /etc/environment:<br>
<code>$sudo gedit /etc/environment</code><br></li>
<code>PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:PATH/TO/PROJECT/DIRECTORY"</code></li>
<li>Run it!<br>
<code>$goto NameOfFolder</code><br></li>
<li>You're good to go!</li>
</ol>
##Additional Instructions:
<ol>
<li>If there are multiple directories of the same name, It'll ask to enter ID of required directory from given options.<br></li>
<li>Directory names with spaces can be passed with:<br>
<code>$goto "Directory Name"</code><br>
OR<br>
<code>$goto Directory\ Name</code><br><li>
##Positional Arguments
<code>$goto < -dk | --dont-kill > < DirName ></code><br>
<ul>
<li>< DirName >: Name of Directory you want to visit</li>
<li>< -dk | --dont-kill >: pass it if you don't want current terminal window to be killed</li>
</ul>
##Enjoy!
