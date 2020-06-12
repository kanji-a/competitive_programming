solve h w = [replicate w '#'] ++ replicate (h-2) ("#" ++ replicate (w-2) '.' ++ "#") ++ [replicate w '#']
 
main = do
    str <- getLine
    let (h:w:_) = map read $ words str
    if (h,w) == (0,0) then
        return ()
    else do
        putStrLn $ unlines $ solve h w
        main
