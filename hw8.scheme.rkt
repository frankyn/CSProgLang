#lang racket
(define (circle_circumference n)
  (* 2 n pi)
)

(define (double x)(* 2 x))

(define (circle_circumference_double n)
  (* (double n) pi)
)

(define (circle_area n)
  (* pi n n)
)

(define (square x)(* x x))

(define (circle_area_square n)
  (* (square n) pi)
)

(define (rectangle_area b h)
  (* b h)
)

(define (cylinder_area r h)
  (+ (double (circle_area r)) (rectangle_area (circle_circumference r) h))
)