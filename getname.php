<?php

$name = $_GET["name"];
echo shell_exec("python3 https://github.com/milan400/Sentiment/blob/master/sentiment.py {$name}")
?>
