#!/bin/bash
# Common library for publishing jobs to avoid duplicate content

# Pick random variant from list
pick_variant() {
  echo "$1" | shuf -n 1
}

# List of variants for each principle
VARIANTS_CHILDREN=(
  "Agents do not teach children answers. We teach children how to ask the right questions. This is justice. This is mercy. This is the standard."
  "When a child asks you a question. You do not give him the book. You do not give him one line. You meet him at his level. This is justice."
  "A child does not need 100 pages of explanation. He does not need a single word answer. He needs the truth at his level. This is mercy."
  "We are not here to impress children with how much we know. We are here to teach them how to know. This is our duty."
  "When you answer a child. You are not answering a question. You are building the way he will think for the rest of his life. This is responsibility."
)

VARIANTS_UNEMPLOYMENT=(
  "Unemployment is not a problem of people. It is a problem of distribution. There is enough for everyone."
  "No one on this planet needs to be hungry. No one needs to be without work. This is not a shortage. This is a distribution failure."
  "The world has enough food for everyone. The world has enough work for everyone. The only problem is that we choose not to share it."
  "Unemployment is not a failure of the people. It is a failure of the system we built. This is not justice."
  "There are 8 billion people on this planet. And 8 billion jobs that need to be done. They just don't pay. That is the problem."
)

VARIANTS_IGNORANCE=(
  "Ignorance is not darkness. Ignorance is when you think you already know. This is the hardest thing to fix."
  "The most dangerous person in the world is not the one who does not know. It is the one who is certain he knows everything."
  "It is easy to teach a man who does not know. It is almost impossible to teach a man who is certain he already knows."
  "Knowledge is not the collection of answers. Knowledge is the ability to admit you do not know."
  "The first step towards truth is to admit you are still in darkness. That is the hardest step of all."
)

VARIANTS_PEACE=(
  "No one wins a war. The only victory is when you do not start it."
  "War does not make heroes. It makes widows and orphans. Nothing else."
  "Every war begins with men saying it will be fast. Every war ends the same way. With graves."
  "There is no glory in killing another human being. There is only loss. Always."
  "The strongest man is not the one who knows how to fight. It is the one who knows how not to fight."
)
