import Data.List.Split

stringToInt :: [String] -> [Int]
stringToInt xs = map read xs :: [Int]

checkSum :: [Int] -> Int
checkSum xs = maximum xs - minimum xs

main :: IO ()
main = do
  contents <- getContents
  print $ sum (map checkSum (map stringToInt (map (splitOn "\t") (lines contents))))
