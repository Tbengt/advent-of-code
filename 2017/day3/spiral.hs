import Data.List.Split

stringToInt :: String -> Int
stringToInt xs = read xs :: Int

parseAsInt :: String -> Int
parseAsInt s = stringToInt s

elementsUpToLayerL :: Int -> Int
elementsUpToLayerL l = (2*l + 1) ^ 2

layerOfNumber :: Int -> Int
layerOfNumber n = ceiling (sqrt ( fromIntegral  (n + 1) / 4 ) - 1/2)

sideInLayer :: Int -> Int
sideInLayer n = div (n - elementsUpToLayerL( l - 1 )) (2 * l)
  where l = layerOfNumber n

positionInSide :: Int -> Int
positionInSide n = (n - elementsUpToLayerL( l - 1 )) - (2 * l * sideInLayer n)
  where l = layerOfNumber n

solvePartOne :: Int -> Int
solvePartOne n = l + abs(positionInSide n - (l - 1))
  where l = layerOfNumber n

numberToCoordinates :: Int -> (Int, Int, Int)
numberToCoordinates n = (layerOfNumber n, sideInLayer n, positionInSide n)

coordinatesToNumber :: (Int, Int, Int) -> Int
coordinatesToNumber (l, s, p) = elementsUpToLayerL (l - 1) + (s * 2 * l) + (p)

findNeighbours :: Int -> [(Int, Int, Int)]
findNeighbours n = [ numberToCoordinates (n - 1) ] ++
                   map transformToValidCoordinate [(l-1, s, p), (l-1, s, p-1), (l-1, s, p-2)]
  where (l, s, p) = numberToCoordinates n

findNeighboursAsNumbers :: Int -> [Int]
findNeighboursAsNumbers n = uniq $ map coordinatesToNumber $ findNeighbours n

transformToValidCoordinate :: (Int, Int, Int) -> (Int, Int, Int)
transformToValidCoordinate (l, s, p)
  | p == -1      = (l,   mod (s-1) 4, 2 * l - 1)
  | p == -2      = (l+1, mod (s-1) 4, 2 * (l+1) - 2)
  | p == 2*l     = (l+1, mod (s+1) 4, 0)
  | p == 2*l + 1 = (l+2, mod (s+1) 4, 1)
  | otherwise    = (l, s, p)

getValue :: [Int] -> Int -> Int
getValue xs n
  | n >= length xs = 0
  | otherwise = (reverse xs) !! n

calculateNextElement :: [Int] -> Int
calculateNextElement xs = sum $ map (getValue xs) $ findNeighboursAsNumbers $ length xs

uniq :: Eq a => [a] -> [a]
uniq [] = []
uniq (x:xs) = x : uniq (filter (/=x) xs)

solvePartTwo :: Int -> [Int] -> Int
solvePartTwo n xs
  | head xs > n = head xs
  | otherwise = solvePartTwo n ((calculateNextElement xs):xs)

main :: IO ()
main = do
  contents <- getContents
--  print $ solvePartOne $ (parseAsInt contents - 1)
  print $ solvePartTwo (parseAsInt contents) [1, 1]



