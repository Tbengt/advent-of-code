import Data.List.Split

stringToInt :: [String] -> [Int]
stringToInt xs = map read xs :: [Int]

checkSum :: [Int] -> Int
checkSum xs = maximum xs - minimum xs

divideBiggerBySmaller :: Int -> Int -> Int
divideBiggerBySmaller x y
  | x < y = div y x
  | otherwise = div x y

isDivisableBy :: Int -> Int -> Bool
isDivisableBy x y
  | x < y = (mod y x) == 0
  | otherwise = (mod x y) == 0

elementsDivisibleBy :: Int -> [Int] -> [Int]
elementsDivisibleBy n xs = filter (isDivisableBy n) xs

findTwoDivisableElements :: [Int] -> Int
findTwoDivisableElements (x:xs)
  | not $ null $ y = divideBiggerBySmaller x (head y)
  | otherwise = findTwoDivisableElements xs
  where y = elementsDivisibleBy x xs

parseAsListsOfInt :: String -> [[Int]]
parseAsListsOfInt s = map stringToInt (map (splitOn "\t") (lines s))

main :: IO ()
main = do
  contents <- getContents
  print $ sum (map checkSum (parseAsListsOfInt contents))
  print $ sum (map findTwoDivisableElements (parseAsListsOfInt contents))
