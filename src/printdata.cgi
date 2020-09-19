#!/usr/bin/perl

use JSON;
use LWP::UserAgent;
use CGI;

my $q = CGI->new;
my $ua = LWP::UserAgent->new;
my $JSON = JSON->new;
$ua->agent("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:74.0.1) Gecko/20100101 Firefox/74.0.1");

my $destination = $q->param("destination");
print "<meta name='viewport' content='width=device-width, initial-scale=1' />";
print "<style>
img {
    width: 50%;
    height: auto;
}
</style>";
print $q->header;
print $q->h1("r/".$destination);
print "<ul>\n";
my $json_data = $JSON->decode($ua->get("https://old.reddit.com/r/$destination/.json?&limit=20")->content);
for (my $i = 0; $i<20;$i++) {
  my $title = $json_data->{data}->{children}->[$i]->{data}->{title};
  my $author = $json_data->{data}->{children}->[$i]->{data}->{author};
  my $content = $json_data->{data}->{children}->[$i]->{data}->{selftext_html};
  my $url = $json_data->{data}->{children}->[$i]->{data}->{url};
  my $link = $json_data->{data}->{children}->[$i]->{data}->{permalink};
  $link =~ s/\///;
  my $proxy_url = "proxy.cgi?url=$url";
  my $is_image;

  if ($url =~ /.*(jpg|png)/i) {
    $is_image = 1;
  }
  if($i % 5 == 0) {
    if($x > 0)
      {
	print "</div>\n<p />";
      }
  }
  print "<li><h2>$title</h2><br/>";
  print "<a href='/printpost.cgi?post=$link'><img src='$proxy_url' alt='Click to view post'></a>";
  print "</li>"
  }
