# coding: utf-8
words = [
  "ああー",
  "そっかそか",
  "なるほど",
  "確かに",
  "マジっすか！",
  "いやいやいや..."
  ]

while true
  word = words.sample
  puts word
  `echo #{word} | say -v 'kyoko'`
  sleep 0.1
end
