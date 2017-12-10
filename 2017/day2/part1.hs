-- convert an integer to list of the digits of that integer
integerToListOfDigits :: Integer -> [Integer]
integerToListOfDigits n
  | n < 10 = [n]
  | otherwise = integerToListOfDigits (div n 10) ++ [mod n 10]

returnValueIfEqual :: Integer -> Integer -> Integer
returnValueIfEqual a b
  | a == b = a
  | otherwise = 0

-- "circularly" shifts elements in the list one step
shiftListByOne :: [Integer] -> [Integer]
shiftListByOne [] = []
shiftListByOne (x:[]) = [x]
shiftListByOne (x:xs) = xs ++ [x]

-- "circularly" shifts a list n times
shiftListByN :: [Integer] -> Int -> [Integer]
shiftListByN xs n = iterate shiftListByOne xs !! n

genericShiftSolver :: [Integer] -> Int -> Integer
genericShiftSolver xs n = sum (zipWith returnValueIfEqual xs (shiftListByN xs n) )

solvePart1 :: Integer -> Integer
solvePart1 n = genericShiftSolver (integerToListOfDigits n) 1

solvePart2 :: Integer -> Integer
solvePart2 n = genericShiftSolver (integerToListOfDigits n) (div (length (integerToListOfDigits n) ) 2)
