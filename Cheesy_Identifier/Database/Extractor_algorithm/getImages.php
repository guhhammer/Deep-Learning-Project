<?php 

    include('simple_html_dom.php');

    function start_html(){  echo "<html><head></head><body style=\"background-color: white; overflow-x: hidden;\"></body></html>"; }

    function display_as_p($show, $size){
        echo "<p style=\"position: relative; display: inline-block; text-align: center; width: 100%; align: center; margin: 0 auto; color: green; font-size: $size;\">";
        echo $show."</p><br>";
    }

    $values_link = explode("_BR_", $_GET["link"]);

    $cheese_name = str_replace("_", " ", $values_link[0]);     $related_query = str_replace("_", " ", $values_link[1]);
    
    $step_start = $values_link[2];   $step_stop = $values_link[3];
    
    $clean_database = $values_link[4];    $database_folder = $values_link[5]."\\cheese_photos";


    # Clean database.
    if($clean_database === "yes" && file_exists($database_folder)){
        foreach (glob($database_folder . '/*' , GLOB_ONLYDIR) as $files) { array_map('unlink', glob($files."/*.*")); }
        foreach (glob($database_folder.'/*')  as $dir_) { rmdir($dir_);   }
    }

    # Make a database folder.
    if (!file_exists($database_folder)) {  mkdir($database_folder, 0777, true); }

    # Page layout display.
    start_html();  display_as_p("<br>Extraction tool:", "250%");

    display_as_p("<br><br>Extracting following queries: ".$cheese_name.".<br><br><br>", "180%");

    error_reporting(E_ERROR | E_PARSE);


    $search_query = urlencode($related_query);

    $image_count = $step_stop;  $steps = $step_start; $k = 0; $l = $step_start;

    display_as_p(($step_stop-$step_start)."<br>","500%");

    
    $root = str_replace(" ","_",$cheese_name);

    if (!file_exists($database_folder."/".$root)) { 
    
        mkdir($database_folder."/".$root, 0777, true);

        $fp = fopen($database_folder."/".$root."/label.txt","wb");
        fwrite($fp, $root);
        fclose($fp);

    }

    $directory = str_replace("\\", "\\\\", $database_folder."\\".str_replace(" ","_",$cheese_name)."\\");
    $filecount = 0; $files = glob($directory . "*");
    if ($files){ $filecount = count($files)-1; }

    $l = $filecount;

    do {
        
        $steps = $steps + 20;

        $html = file_get_html("https://www.google.com/search?q=$search_query&atb=v193-1&ia=web&tbm=isch&start=$steps");    

        $images = $html->find('img');

        foreach($images as $image){

            $link = $image->getAttribute("src");

            if(strlen($link) > 5){

                $arr_exclude_gif = explode(".",$link); $not_gif = true;  foreach($arr_exclude_gif as $ext){  if($ext == "gif"){ $not_gif = false; } }

                if($not_gif){               

                    $name = "image_".$l.".png";
                    #$ll = imagepng(imagecreatefromstring(file_get_contents($link)), $name);
                    file_put_contents($database_folder."/".$root."/".$name, file_get_contents($link));
                    $l++;

                }

            }

        }

    } while($image_count >= $steps);

    unset($images);
    unset($html);
    
    $directory = str_replace("\\", "\\\\", $database_folder."\\".str_replace(" ","_",$cheese_name)."\\");
    $filecount = 0; $files = glob($directory . "*");
    if ($files){ $filecount = count($files)-1; }

    display_as_p($filecount." photos of ".$cheese_name." were extracted and saved into ".$directory.".","140%;");



?>
