#!/usr//bin/perl
#
# Play the Bulls and Cows game
#
# This script has three states:
# - "" (initial state before we start playing the game)
# - Guessing (state for making guess/processing previous guess)
# - Won (state when the player guesses correctly)
#
# States are implemented via the State data item
#
# Other data items that are carried from state to state:
# - Answer (what we're trying to guess)
# - Guesses (comma-separated list of guesses made so far)
# - Box1,Box2,Box3,Box4 (most recent colours guessed for boxes)
#
# All data items are initially null ("")
#

use CGI qw/:all/;

# Information for the current state

$state   = param('State');
$guesses = param('Guesses');
$answer  = param('Answer');

# Constants (colour list and welcome message)

%colours = ("r"=>"Red","y"=>"Yellow","g"=>"Green","b"=>"Blue");

$welcome = <<WELCOME
Welcome to the Bulls and Cows guessing game. <p>
There are four colours "hidden" under the squares. <p>
<table border=1 cellpadding=10>
<tr>
  <td>&nbsp; &nbsp; &nbsp; ? &nbsp; &nbsp; &nbsp;</td>
  <td>&nbsp; &nbsp; &nbsp; ? &nbsp; &nbsp; &nbsp;</td>
  <td>&nbsp; &nbsp; &nbsp; ? &nbsp; &nbsp; &nbsp;</td>
  <td>&nbsp; &nbsp; &nbsp; ? &nbsp; &nbsp; &nbsp;</td>
</tr>
</table> <p>
In each turn you can guess colours for as many squares as you like. <br>
I will then tell you how many "bulls" and "cows" you scored. <br>
A "bull" means that you guessed the correct colour in the correct square. <br>
A "cow" means that you guessed the correct colour but in the wrong square. <br>
Each guess will be counted only once, and bulls are counted before cows. <p>
The aim of the game is for you to work out the colours <br>
in the least number of guesses.
WELCOME
;

# Start off each page with a standard header

print(
	header,
	start_html(-bgcolor=>'white',-title=>'Bulls\'n\'Cows Game'),
	"<center>\n",
	h1("Bulls\'n\'Cows Guessing Game")
);

if ($state eq "")
# Initial state: print welcome/instruction message
{
	# Generate a random sequence of four colours
	@cols = keys %colours;
	foreach $i (1..4) {
		$c = $cols[int(rand($#cols+1))];
		$answer .= $c;
	}

	# Print message, set initial state and display button to start game
	print(
		$welcome,
		start_form,
		"<input type=hidden name='State' value='Guessing'>",
		"<input type=hidden name='Guesses' value=''>",
		"<input type=hidden name='Answer' value='$answer'>",
		submit("Start the game"),
		end_form
	);
}
elsif ($state eq "Guessing")
# Check previous guess (if any)
# If won, then print a message and click to scoreboard page
# If not won, print the guessing table, plus previous guesses
{
	# Process previous guess

	$guess = param('Box1').param('Box2').param('Box3').param('Box4');
	($bulls, $cows) = &bullcow($guess, $answer);
	$guesses = "$guess,$guesses";
	$guesses =~ s/,$//;

	# We won! So set up for winning state

	if ($bulls == 4)
	{
		@g = split(/,/,$guesses);
		$ng = $#g+1;
		print(
			"Congratulations! You guessed it.",
			p,
			"It took you $ng guesses.",
			p,
			start_form,
			"<input type=hidden name='State' value='Won'>",
			"<input type=hidden name='Score' value='$ng'>",
			"Enter your name:",
			"<input type=text name='Player'>",
			p,
			submit("Click for ScoreBoard"),
			end_form,
			end_html
		);
		exit 0;
	}

	# Set up table containing pull-down colour menus
	#  for collecting the next guess

	print(
		start_form,
		"<input type=hidden name='State' value='Guessing'>",
		"<input type=hidden name='Guesses' value='$guesses'>",
		"<input type=hidden name='Answer' value='$answer'>",
		"<table border=1 cellpadding=5><tr>"
	);
	foreach $i (1..4) {
		print "<td><select name='Box$i' default='?'>\n";
		print "<option value='?'>?\n";
		foreach $c (keys %colours) {
			print "<option value='$c'>$colours{$c}\n";
		}
		print "</select></td>\n";
	}
	print(
		"</tr></table>\n",
		p,
		submit("Submit guess"),
		end_form,
		p
	);

	# Iterate over previous guesses, displaying
	#  each guess along with the score it obtained

	print h3("Previous Guesses");
	foreach $guess (split(/,/,$guesses)) {
		print "<p><table border=1 cellpadding=5><tr>";
		foreach $c (split(//, $guess)) {
			if ($c eq "?") {
				print "<td> &nbsp; ? &nbsp; &nbsp; </td>";
			}
			else {
				print(
					"<td bgcolor='$colours{$c}'>",	
					"&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;",
					"</td>"
				);
			}
		}
		($bulls, $cows) = &bullcow($guess, $answer);
		print "<td>$bulls Bulls, $cows Cows</td>";
		print "</tr></table>\n";
	}
}
elsif ($state eq "Won")
{
	# Update the scoreboard

	$score = param('Score');
	$score =~ s/[^\d]//g;             # remove all but expected characters
	$score = substr $score, 0, 4;    # limit score to 4 characters
	$player = param('Player');
	$player =~ s/[^\w\s-_]//g;        # remove all but expected characters
	$player = substr $player, 0, 256; # limit player to 256 characters
	if (!open(SCORES, ">>ScoreBoard")) {
		print h3(font({-color=>'red'},"Can't write Scoreboard"));
	}
	else {
		print SCORES "$score;$player;".localtime()."\n";
		close(SCORES);
	}

	# Fetch the scoreboard information

	if (!open(SCORES, "<ScoreBoard")) {
		print( 
			h3(font({-color=>'red'},"Can't read Scoreboard")),
			end_html
		);
		exit 0;
	}
	$i = 0;
	while ($line = <SCORES>) {
		$lines[$i++] = $line;
	}
	close(SCORES);

	# Display the scoreboard

	print h3("Best Scores");
	print(
		"<table border=1>\n",
		"<tr><th>Score</th><th>Player</th><th>Date</th></tr>\n"
	);
	foreach $line (sort @lines) {
		@bits = split(/;/,$line);
		print "<tr><td>$bits[0]</td><td>$bits[1]</td><td>$bits[2]</td></tr>\n";
	}
	print "</table>\n";

	# Print button for starting a new game

	print(
		start_form,
		"<input type=hidden name='State' value=''>",
		submit("Play another game?"),
		end_form,
	);
}

print "</center>",end_html;

# BullCow subroutine:
#   Takes two strings (each of four chars) and computes the
#   number of direct (Bull) matches and indirect (Cow) matches

sub bullcow()
{
	my @guess  = split(//,$_[0]);
	my @answer = split(//,$_[1]);
	my $bulls = 0;
	my $cows  = 0;

	# Count bulls

	for $i (0..3) {
		if ($guess[$i] eq $answer[$i]) {
			$bulls++;
			$guess[$i] = "?";
			$answer[$i] = "#";
		}
	}

	# Count cows

	foreach $i (0..3) {
		foreach $j (0..3) {
			if ($guess[$i] eq $answer[$j]) {
				$cows++;
				$guess[$i] = "?";
				$answer[$j] = "#";
			}
		}
	}

	return ($bulls,$cows);
}
