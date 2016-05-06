<?php

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$n);
$a = array();

$primaryDiag=0;
$secondDiag=0;

$j=0; //counter for the correct index in the row

for($a_i = 0; $a_i < $n; $a_i++) {
   $a_temp = fgets($handle);
   $a[] = explode(" ",$a_temp);

    $primaryDiag += $a[$a_i][$j];
    $secondDiag += $a[$a_i][($n-1)-$j];
   
    $j++;
  array_walk($a[$a_i],'intval');
}

echo abs($primaryDiag - $secondDiag);


?>
