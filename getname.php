<?php

$name = $_GET["name"];
echo shell_exec("python3 /opt/lampp/htdocs/ptop/sentiment.py {$name}")
?>