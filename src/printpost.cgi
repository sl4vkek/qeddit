#!/usr/bin/perl

use JSON;
use LWP::UserAgent;
use CGI;
use HTML::Entities;
do "./qeddit-config.cgi";
my $q = CGI->new;
my $ua = LWP::UserAgent->new;
my $JSON = JSON->new;
$ua->agent($useragent);
print $q->header;
my $post = $q->param("post");
my $json_data = $JSON->decode($ua->get("https://old.reddit.com/$post/.json")->content);
my $num_comments = $json_data->[0]->{data}->{children}->[0]->{data}->{num_comments};
print $q->h2(encode_entities($json_data->[0]->{data}->{children}->[0]->{data}->{title}));
my $post = encode_entities($json_data->[0]->{data}->{children}->[0]->{data}->{selftext_html});
# my $post_img = $json_data->[0]->{data}->{children}->[0]->{data}->{url_overridden_by_dest};

# print "<img src=\"$post_img\" alt=\"image\"/>" if $post_img;
print "<link rel='stylesheet' href='/style.css'>";
$post =~ s/&gt;/>/g;
$post =~ s/&lt;/</g;
#print decode_entities($post);
print $post;
print $q->h3("comments");

for (my $i = 1;$i<$num_comments;$i++) {
  print encode_entities("<b>$json_data->[1]->{data}->{children}->[$i]->{data}->{author} :</b>  ");
  print encode_entities($json_data->[1]->{data}->{children}->[$i]->{data}->{body});
  #print "<b>$json_data->[1]->{data}->{children}->[$i]->{data}->{author} :</b>  ";
  #print $json_data->[1]->{data}->{children}->[$i]->{data}->{body};
  print "<br/><br/>";

}
