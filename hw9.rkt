#lang racket

(define (cylinder_area r h)
  (+ (* 2 pi r r) (* 2 pi r h))
)

(define (T n)
  (cond 
    [(eq? n 1) 2]
    [(> n 1) (+(* 2 (T (- n 1))) 2)]
  )
)

(define (fibonacci n) 
  (cond 
    [(< n 1) (error "wtf dude.")]
    [(= n 1) 1]
    [(= n 2) 1]
    [else (+ (fibonacci (- n 1)) (fibonacci (- n 2)))]
  )
)
(define e 2.7182)

(define (e_to_the_power_x_easy n)
  (exp n)
)

(define (e_to_the_power_x n)
  (cond
    [(< n 1) (error "wtf dude...")]
    [(= n 1) e]
    [else (* e (e_to_the_power_x (- n 1)))]
  )
)