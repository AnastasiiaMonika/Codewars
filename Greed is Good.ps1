    
    $dies = @(4, 6, 2, 2, 3)
    $dies
    $dies = $dies | sort

    $i = 2 #middle of the array
    $result = 0
    $leftdies = @()
    if ((($dies[2] -eq $dies[1]) -and (($dies[2] -eq $dies[0]) -or ($dies[2] -eq $dies[3]))) -or (($dies[2] -eq $dies[3]) -and (($dies[2] -eq $dies[1]) -or ($dies[2] -eq $dies[4])))){
        Write-Output  "Combo found"
        if ($dies[2] -eq 1){
            $result = 1000
        } else {
            $result = $dies[2]*100
        }
        $i = 3
        
        foreach ($die  in $dies){
            if ($die -ne $dies[2]){
                $leftdies += $die
            } elseif ($i -ge 1){
                $i = $i -1
            }else{
               $leftdies += $die
            }
        }
    } else { #No combo
        Write-Output  "No Combo"
        $leftdies = $dies
    }
    foreach($i in $leftdies){
        if ($i -eq 1){
           $result += 100
        } elseif($i -eq 5){
            $result += 50
        } 
    }
    $result 