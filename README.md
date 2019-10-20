# Thud
A repository for the game Thud.

## **Game Rules**

### **Game Board:**
	The octagonal playing area consists of a 15 by 15 square board
	from which a triangle of 15 squares in each corner has been
	removed.
	The Thudstone is placed on the centre square of the
	board.
	The eight trolls are placed onto the eight
	squares adjacent to the Thudstone.
	The thirty-two dwarfs are
	placed so as to occupy all the perimeter spaces except for the
	four in the same horizontal or vertical line as the Thudstone.

### **Game Start:**
	One player takes control of the dwarfs, the other controls the trolls. The dwarfs move first.

### **Game End Conditions:**
	The battle is over when both players agree that no more captures can be made by continuing to play, or
	when one player has no more valid moves to make. At this point the players count score: the dwarfs score 4
	point for each captured troll, and the trolls score 1 for each captured dwarf, with the difference being the
	'final' score. The players should then swap sides to play another round, and the sum of their final scores for
	the two battles determines the overall victor.


### **On the dwarfs' turn, they may either move or hurl one dwarf:**
	- Move: any one dwarf is moved like a chess queen, any number of squares in any orthogonal or
		diagonal direction, but not onto or through any other piece, whether Thudstone, dwarf, or troll; or
	- Hurl: anywhere there is a straight (orthogonal or diagonal) line of adjacent dwarfs on the board, they
		may hurl the front dwarf in the direction continuing the line, as long as the space between the lead
		dwarf and the troll is less than the number of dwarfs in the line. This is different from a normal move
		in that the dwarf is permitted to land on a square containing a troll, in which case the troll is removed
		from the board and the dwarf takes his place. This may only be done if the endmost dwarf can land
		on a troll by moving in the direction of the line at most as many spaces as there are dwarfs in the
		line. Since a single dwarf is a line of one in any direction, a dwarf may always move one space to
		capture a troll on an immediately adjacent square.

### **On the trolls' turn, they may either move or shove one troll:**
	- Move: one troll is moved like a chess king, one square in any orthogonal or diagonal direction onto
		an empty square. After the troll has been moved, only a single dwarf on the eight squares adjacent to
		the moved troll may optionally be immediately captured and removed from the board, at the troll
		player's discretion; or
	- Shove: anywhere there is a straight (orthogonal or diagonal) line of adjacent trolls on the board, they
		may shove the endmost troll in the direction continuing the line, up to as many spaces as there are
		trolls in the line. As in a normal move, the troll may not land on an occupied square, and any (all)
		dwarfs in the eight squares adjacent to its final position may immediately be captured. Trolls may
		only make a shove if by doing so they capture at least one dwarf.
