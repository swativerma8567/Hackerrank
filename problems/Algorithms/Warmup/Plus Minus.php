<?php

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d",$n);
$arr_temp = fgets($handle);
$arr = explode(" ",$arr_temp);
array_walk($arr,'intval');
$noOfZeros=0;
$noOfPos=0;
$noOfNeg=0;
for($i=0;$i<$n;$i++)
{
    if($arr[$i]==0)
    {
        $noOfZeros++;
    }
    else if($arr[$i]>0)
        {
        $noOfPos++;
    }
    else{
        $noOfNeg++;
    }
}

//echo $noOfZeros.":".$noOfPos.":".$noOfNeg;
echo number_format($noOfPos/$n,6)."\n";
echo number_format($noOfNeg/$n,6)."\n";
echo number_format($noOfZeros/$n,6)."\n";

    
?>
