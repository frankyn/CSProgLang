#lang racket
(define (maximum lis)
  (cond
    [(null? (cdr lis)) (car lis)]
    [(> (car lis) (car (cdr lis))) (cons (car lis) (cdr (cdr lis)))]
    [else (maximum (cdr lis))]
  )
)

(define (count_zeros lis)
  (cond
    [(null? lis) 0]
    [(eq? (car lis) 0) (+ 1 (count_zeros (cdr lis)))]
    [else (+ 0 (count_zeros (cdr lis)))])
)

(define (delete_zeros lis)
  (cond
    [(null? lis) lis]
    [(eq? (car lis) 0) (delete_zeros (cdr lis))]
    [else (cons (car lis) (delete_zeros (cdr lis)))]
  )
)

(define (change_the_zeros lis)
  (cond
    [(null? lis) lis]
    [(eq? (car lis) 0) (cons -1 (change_the_zeros (cdr lis)))]
    [else (cons (car lis) (change_the_zeros (cdr lis)))]
  )
)