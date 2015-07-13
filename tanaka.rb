words = [
  "あぁ〜",
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
  sleep 1
end
