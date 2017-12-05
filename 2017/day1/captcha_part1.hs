integerToListOfDigits :: Integer -> [Integer]
integerToListOfDigits n
  | n < 10 = [n]
  | otherwise = integerToListOfDigits (div n 10) ++ [mod n 10]

returnValueIfEqual :: Integer -> Integer -> Integer
returnValueIfEqual a b
  | a == b = a
  | otherwise = 0

calculateCaptcha :: [Integer] -> Integer
calculateCaptcha [] = 0
calculateCaptcha (x:[]) = 0
calculateCaptcha (x:xs) = returnValueIfEqual x (head xs) + calculateCaptcha xs

appendFirstElementOfListToEndOfList :: [a] -> [a]
appendFirstElementOfListToEndOfList [] = []
appendFirstElementOfListToEndOfList (xs) = xs ++ [head(xs)]

solveDay1 :: Integer -> Integer
solveDay1 n = calculateCaptcha ( appendFirstElementOfListToEndOfList (integerToListOfDigits n))
