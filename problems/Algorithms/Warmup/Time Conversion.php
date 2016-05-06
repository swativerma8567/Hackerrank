<?php

$handle = fopen ("php://stdin","r");
fscanf($handle,"%s",$time);

$tobj=new Datetime($time);
echo $tobj->format("H:i:s");
?>