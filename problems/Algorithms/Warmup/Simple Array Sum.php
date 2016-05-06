<?php

$handle = fopen ("php://stdin","r");
$totalNum = fscanf($handle,"%d");
$arr_temp = fgets($handle);
$arr = explode(" ",$arr_temp);
//array_walk($arr,'intval');

echo array_sum($arr);

?>
