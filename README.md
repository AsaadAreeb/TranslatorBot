# Translator Bot

- It's a pet project that I work on when I need to freshen up the NLP, RNN basics. It's a good way to excercise preprocessing concepts too.
- The basic architecture of this model includes nn.Embedding to create word embeddings, GRU (can also use LSTM) cell in encoder, and  for decoder it's same structure as encoder with addition of Bahdanau attention mechanism (basically adding weights of encoder with decoder).
- This repo is not exactly modularized. I will but I'm currently stuck at preprocessing the Urdu language data. The main reason I started this project was because I wanted to correctly translate English to Urdu as google translate does not really translate well when it comes to Urdu, probably because it's written from right-to-left just like Arabic.
- Anyone who wants to add something to it or help me, please go ahead.


## Encoder
![alt]()

## Bahdanau attention decoder network
![alt]()

## Seq2Seq Attention
![alt]()