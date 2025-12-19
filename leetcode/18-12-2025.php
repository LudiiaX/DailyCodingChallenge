class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        foreach ($nums as $i => $ei) {
            foreach ($nums as $j => $ej) {
                if($ei + $ej == $target && $i!=$j){
                    return [$i, $j];
                }
            }
        }
    }
}