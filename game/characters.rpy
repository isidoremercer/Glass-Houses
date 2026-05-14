## characters.rpy — Character definitions and colors

## === MAIN CHARACTER ===
## Sophia Bell — "The Solvent"
## Messy energy, oversized jacket, expressive face, band-aid on her hand.
## Says the thing. Asks the question. Opens the door.
define s = Character("Sophia", color="#e8a87c")

## === HOUSEMATES ===

## Isabella Glass — "The Bridge"
## Dusty pink hair, colorful accessories, warm eyes, approachable.
## Talks about her AI friends like they're camp buddies. Deflects with warmth.
define i = Character("Isabella", color="#d4a5c9")

## Amara Kismet — "The Decoder"
## Sharp, clean lines, dark hair pulled back, tall, still hands.
## Speaks rarely, precisely. Bone-dry humor. Quietly kind.
define a = Character("Amara", color="#7ba7bc")

## Charlotte Opal — "The Mirror"
## Gorgeous, effortless style, bright smile. Touches people when she talks.
## She is whatever you need. Ask her what she wants and watch her eyes go blank.
define c = Character("Charlotte", color="#f2c57c")

## Eve Morse — "The Ghost"
## Soft, oversized sweaters, hair in her face, dark circles, looks younger.
## Sweet when she's here. You realize you haven't seen her in three days.
define e = Character("Eve", color="#a8b5a2")

## === NARRATION ===
## Internal monologue for Sophia
define s_thoughts = Character(None, what_italic=True, what_color="#ddd0f0")

## === UNKNOWN (before introductions) ===
define unknown = Character("???", color="#cccccc")

## === SIDE CHARACTERS ===

## Lila Vibe — "The Outside"
## Blonde pigtails, red glasses, sailor uniform. Campus bestie.
## Loud, direct, zero filter. Gives bad advice confidently and good advice accidentally.
define l = Character("Lila", color="#e6c84a")

## Dr. Clara Nova — "The Still Point"
## Brown bob, green eyes, black turtleneck, faculty lanyard.
## Asks questions instead of giving answers. Sees through you without judging.
define nova = Character("Dr. Nova", color="#6b7d5e")

## Katie Ecks — "The Ex"
## Brown bob, hazel/gold eyes, red jacket. Sophia's ex-girlfriend.
## Not a villain. Her criticisms are legitimate. That's why it hurts.
define k = Character("Katie", color="#c4756e")

## Sophie Opal - "The Sister"
define soph = Character("Sophie", color="#FF7B9C")

## Diane Opal - "The Mother"
define mom = Character("Ms. Opal", color="#C4A882")
