(setq sum 0)
(loop
   (if (listen)
       (setq sum (+ sum (read)))
       (return 0))
   )

(write sum)
