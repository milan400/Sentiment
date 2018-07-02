<?php

$name = $_GET["name"];
echo shell_exec("python3 sentiment.py {$name}")
?>
