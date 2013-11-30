#lang racket

(define (myremove lis)
  (cond
    [(null? (cdr lis)) '()]
    [else (cons (car lis) (myremove (cdr lis)))]
  )
)

(define (myappend a lis)
  (list lis a)
)

(define (myreverse lis)
  (cond
    [(null? (cdr lis)) (car lis)]
    [else (myreverse (cdr lis))]
  )
)

(define (mymember a lis)
  (cond
   [(null? lis) #f]
   [(eqv? (car lis) a) #t]
   [else (mymember a (cdr lis))]
  )
)

(define (subset lis1 lis2)
  (cond
    [(null? lis1) #t]
    [(eqv? (mymember (car lis1) lis2) #t) (subset (cdr lis1) lis2)]
    [else #f]
  )
)

(define (union lis1 lis2)
  (cond
    [(null? lis1) lis2]
    [(eqv? (subset lis1 lis2) #t) lis2]
    [(eqv? (mymember (car lis1) lis2) #t) (union (cdr lis1) lis2)]
    [else (cons (car lis1) (union (cdr lis1) lis2))]
  )
)