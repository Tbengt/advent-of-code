import Data.List.Split

main :: IO ()
main = do
  contents <- getContents
  print $ length contents
  print $ map (splitOn "\t") (lines contents)