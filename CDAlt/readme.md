#Project GOTO
##Synopsis
An efficient alternative to the cd command in unix based systems
##Installation
<ol>
<li>Clone the Github repo<br></li>
<li>Run initdata.py:<br>
```$python3 initdata.py```<br></li>
<li>Append the path of the project folder to PATH variable in /etc/environment:<br>
```$sudo gedit /etc/environment```<br></li>
<li>Run it!<br>
```$goto NameOfFolder```<br></li>
<li>You're good to go!</li>
</ol>
##Positional Arguments
```$goto < -dk | --dont-kill > < DirName >```
<ul>
<li>< DirName >: Name of Directory you want to visit</li>
<li>< -dk | --dont-kill >: pass it if you don't want current terminal window to be killed</li>
</ul>
##Enjoy!
