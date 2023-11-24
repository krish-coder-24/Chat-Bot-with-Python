import os, re, sys, time
from textblob import TextBlob


""" Simple Bot Function """
while True:
  user = input("You: ")
  text = TextBlob(user)
  print(text.tags)

