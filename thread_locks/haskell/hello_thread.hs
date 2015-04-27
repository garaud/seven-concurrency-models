-- Compile with ghc -o hello_thread hello_thread.hs
import Control.Concurrent
import Control.Monad
import System.IO

main = do
  forkIO (putStrLn "Hello from new thread")
  putStrLn "Hello from Main"
