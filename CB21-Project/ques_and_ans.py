import transformers
from transformers import AutoModelForSeq2SeqLM
from pipelines1 import pipeline

nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl")

# text = "Forrest Gump is a 1994 American comedy-drama film directed by Robert Zemeckis and written by Eric Roth. \
# It is based on the 1986 novel of the same name by Winston Groom and stars Tom Hanks, Robin Wright, Gary Sinise, \
# Mykelti Williamson and Sally Field. The story depicts several decades in the life of Forrest Gump (Hanks), \
# a slow-witted but kind-hearted man from Alabama who witnesses and unwittingly influences several defining \
# historical events in the 20th century United States. The film differs substantially from the novel.Gravity (from Latin gravitas, meaning 'weight'), or gravitation, is a natural phenomenon by which all \
# things with mass or energy—including planets, stars, galaxies, and even light—are brought toward (or gravitate toward) \
# one another. On Earth, gravity gives weight to physical objects, and the Moon's gravity causes the ocean tides. \
# The gravitational attraction of the original gaseous matter present in the Universe caused it to begin coalescing \
# and forming stars and caused the stars to group together into galaxies, so gravity is responsible for many of \
# the large-scale structures in the Universe. Gravity has an infinite range, although its effects become increasingly \
# weaker as objects get further away"

def generate(text):
  print(nlp(text))
  return nlp(text)
# generate(text)