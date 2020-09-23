#!/usr/bin/perl

use JSON;
use LWP::UserAgent;
use CGI;
use HTML::Entities;
my $q = CGI->new;
my $ua = LWP::UserAgent->new;
my $JSON = JSON->new;
do "./qeddit-config.cgi";
#$ua->agent("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:74.0.1) Gecko/20100101 Firefox/74.0.1");
$ua->agent($useragent);
print $q->header;
my $destination = $q->param("destination");
$destination = encode_entities($destination);
print "<!DOCTYPE html>\n";
print "<html>\n";
print "<head>\n";
print "<title>$destination</title>\n";
print "<meta name='viewport' content='width=device-width, initial-scale=1' />\n";
print "<link rel='stylesheet' href='/style.css' />\n";
print "</head>";
print "<body>\n";
print $q->h1("r/".$destination);
print "<ul>\n";
my $json_data = $JSON->decode($ua->get("https://old.reddit.com/r/$destination/.json?&limit=20")->content);
for (my $i = 0; $i<20;$i++) {
  my $title = encode_entities($json_data->{data}->{children}->[$i]->{data}->{title});
  my $author = encode_entities($json_data->{data}->{children}->[$i]->{data}->{author});
  # my $content = $json_data->{data}->{children}->[$i]->{data}->{selftext_html};
  my $url = $json_data->{data}->{children}->[$i]->{data}->{url};
  my $link = $json_data->{data}->{children}->[$i]->{data}->{permalink};
  $link =~ s/\///;
  my $proxy_url = "proxy.cgi?url=$url";
  my $is_image;

  if ($url =~ /.*(jpg|jpeg|png|gif|webm|mp4)/i) {
    $is_image = 1;
  }
  if($i % 5 == 0) {
    if($x > 0)
      {
        print "</div>\n<p />";
      }
  }
  print "<li>\n<h2>$title A:$author</h2>\n";
  if ($is_image) {
    if ($useproxy == 1) {
      $url = $proxy_url;
    }
    print "<a href='printpost.cgi?post=$link'>\n<img src='$url' alt='Click to view post'>\n</a>";
  }
  else {
    print "<a href='$url'>$url</a>\n<br/>\n<a href='printpost.cgi?post=$link'>Click to view comments</a>\n";
  }
  print "</li>\n";
  }

print "</body>\n";
print "</html>";
