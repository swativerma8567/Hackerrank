<?php

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$n);

for ($i=1;$i<=$n;$i++)
    {
    $x=str_repeat('#',$i);
    $y = sprintf("%".$n."s",$x);
    echo  $y."\n";
}


 

?>
