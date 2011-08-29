#!/usr/bin/perl -w
%mark_deduction = (
    "Ate library book"=>5,  
    "Attended lecture in underpants" => 10, 
    "Urinated on CSE lab computer" => 15,   
    "Stole VC's car" => 20, 
    "Didn't listen to Andrew" => 3, 
    "Fell asleep in tute" => 2, 
    "Disappointed their mother" => 4,   
    "Bit another student" =>  7,    
    "Obscene word on t-shirt" => 1, 
    "Runs Windows on laptop" => 4,  
    "Kesha found on their ipod" => 9,"Caught fighting in Unibar"=>1,    
    "Doesn't play nice" => 1,   
    "Wore mismatched socks" => 1
    );
@reasons = keys %mark_deduction;
while (<>) {
        /^COMP[29]041/ or next;
        my $name = (split /\|/)[2];
        $name =~ s/(.*),\s*(.*\S).*/$2 $1/;
        push @names,  $name;
}
foreach (1..1000) {
    my $name = $names[rand @names];
    my $reason = $reasons[rand @reasons];
    printf '"%s","%s","%02d/%02d/11", "%d marks deducted"'."\n",
    	$name, $reason, (rand 30)+1, (rand 2)+7, $mark_deduction{$reason};
}
